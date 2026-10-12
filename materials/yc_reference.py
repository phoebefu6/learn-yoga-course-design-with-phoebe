"""Python reference for the programme bench. Must agree EXACTLY with assets/yc-live.js.

  python3 materials/yc_reference.py          human-readable ladder
  python3 materials/yc_reference.py --json   canon JSON (compare with node materials/yc-node.js)

All integer arithmetic; complexity means are tenths, rounded half up with integers.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_yc_data import DATA  # one source for the library, cohort and plans

POSE = {p["code"]: p for p in DATA["poses"]}


def tenths(total, n):
    return (total * 20 + n) // (2 * n) if n else 0


def with_peaks(plan):
    out = []
    for i, wk in enumerate(plan):
        pk = DATA["peaks"][i]
        if pk in wk:
            out.append(list(wk))
        elif wk and wk[-1] == "rest":
            out.append(wk[:-1] + [pk, "rest"])
        else:
            out.append(wk + [pk])
    return out


def analyse(plan_in, peak=False, late=False):
    plan = with_peaks(plan_in) if peak else [list(w) for w in plan_in]
    cohort = dict(DATA["cohort"]["flags"])
    lj = DATA["lateJoiner"]
    met = set()
    ceiling = DATA["ceilingStart"]
    weeks, weeks_of = [], {}
    prev_total = None
    late_list = []
    for w, wk in enumerate(plan):
        seen = set()
        gaps, new = [], 0
        total = top = cxs = clash = 0
        cnt = dict(cohort)
        if late and w + 1 >= lj["week"]:
            cnt[lj["flag"]] = cnt.get(lj["flag"], 0) + 1
        for c in wk:
            p = POSE[c]
            if any(q not in met and q not in seen for q in p["pre"]):
                gaps.append(c)
            if c not in met:
                new += 1
            seen.add(c)
            total += p["load"]
            top = max(top, p["load"])
            cxs += p["cx"]
            clash += sum(cnt.get(f, 0) for f in p["flags"])
            weeks_of.setdefault(c, []).append(w + 1)
            if late and w + 1 >= lj["week"] and lj["flag"] in p["flags"]:
                late_list.append([w + 1, c])
        spike = top >= ceiling + DATA["spikeJump"]
        ceiling = max(ceiling, top)
        deload = prev_total is not None and total < prev_total
        prev_total = total
        met |= seen
        weeks.append({"week": w + 1, "n": len(wk), "load": total, "top": top, "cx": tenths(cxs, len(wk)),
                      "gaps": gaps, "spike": spike, "deload": deload, "clash": clash, "new": new})
    reps = {c: len(v) for c, v in weeks_of.items()}
    return {
        "gaps": sum(len(x["gaps"]) for x in weeks),
        "spikes": sum(1 for x in weeks if x["spike"]),
        "deloads": sum(1 for x in weeks if x["deload"]),
        "oneOffs": sum(1 for v in reps.values() if v == 1),
        "spaced": sum(1 for v in reps.values() if v >= 3),
        "distinct": len(reps),
        "clash": sum(x["clash"] for x in weeks),
        "cxFirst": weeks[0]["cx"], "cxLast": weeks[-1]["cx"], "cxMax": max(x["cx"] for x in weeks),
        "topMax": max(x["top"] for x in weeks),
        "late": late_list,
        "weeks": weeks,
    }


def canon():
    out = []
    for r in DATA["rungs"]:
        out.append({"id": r["id"], "plain": analyse(r["plan"]), "peak": analyse(r["plan"], peak=True),
                    "late": analyse(r["plan"], late=True)})
    return out


if __name__ == "__main__":
    c = canon()
    if "--json" in sys.argv:
        sys.stdout.write(json.dumps(c, sort_keys=True, separators=(",", ":")))
        sys.exit(0)
    keys = ["gaps", "spikes", "deloads", "oneOffs", "spaced", "distinct", "clash", "cxFirst", "cxLast", "cxMax", "topMax"]
    for r in c:
        for mode in ("plain", "peak", "late"):
            a = r[mode]
            print("rung", r["id"], mode.ljust(5), " ".join("%s=%s" % (k, a[k]) for k in keys))
            if mode == "plain":
                print("    load ", [w["load"] for w in a["weeks"]], " top", [w["top"] for w in a["weeks"]],
                      " cx", [w["cx"] for w in a["weeks"]], " clash", [w["clash"] for w in a["weeks"]],
                      " gaps", [len(w["gaps"]) for w in a["weeks"]])
            if mode == "peak":
                print("    gaps by week", [w["gaps"] for w in a["weeks"]], " spikes", [w["week"] for w in a["weeks"] if w["spike"]])
            if mode == "late":
                print("    late joiner:", a["late"])
