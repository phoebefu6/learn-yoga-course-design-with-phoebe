"""Build assets/yc-data.js for the programme bench (learn-yoga-course-design-with-phoebe).

CONSTRUCTED, end to end. The pose library, its load and complexity levels, prerequisites,
caution flags, the Juniper Studio cohort and every plan are invented for teaching. Levels are
a teaching scale (1 to 5), not a measurement. Flags are referral and caution tags, never a
diagnosis. Run:  python3 materials/build_yc_data.py   (writes assets/yc-data.js with json.dumps)
yc_reference.py imports the same objects, so Python and the browser read one source.
"""
import json
import os
import random

# code, name, family, load 1-5, complexity 1-5, prerequisites, flags, regression to offer
POSES = [
    ("mtn", "Mountain", "standing", 1, 1, [], [], ""),
    ("hfold", "Half forward fold", "standing", 1, 1, ["mtn"], [], ""),
    ("fold", "Standing forward fold", "standing", 2, 1, ["mtn"], ["headdown"], "half fold, hands on the thighs, head above the heart"),
    ("chair", "Chair", "standing", 3, 1, ["mtn"], ["knee"], "shallow bend, back against a wall"),
    ("war2", "Warrior II", "standing", 3, 2, ["mtn"], [], ""),
    ("lowlunge", "Low lunge", "standing", 2, 2, ["table"], ["knee"], "pad under the back knee, or a short standing lunge"),
    ("lunge", "High lunge", "standing", 3, 2, ["lowlunge"], ["balance"], "back heel down, one hand on a wall"),
    ("war1", "Warrior I", "standing", 3, 2, ["lunge"], [], ""),
    ("tri", "Triangle", "standing", 2, 3, ["war2"], [], ""),
    ("side", "Extended side angle", "standing", 3, 3, ["war2"], [], ""),
    ("pyr", "Pyramid", "standing", 2, 3, ["hfold"], ["headdown"], "hands on blocks, spine long, head above the heart"),
    ("tree", "Tree", "balance", 2, 2, ["mtn"], ["balance"], "toes on the floor, hand on a wall"),
    ("war3", "Warrior III", "balance", 4, 4, ["war1", "tree"], ["balance"], "hands on a wall, standing leg soft"),
    ("halfmoon", "Half moon", "balance", 4, 5, ["tri", "tree"], ["balance"], "back against a wall, block under the hand"),
    ("eagle", "Eagle", "balance", 3, 4, ["tree", "chair"], ["balance", "knee"], "seated, arms only"),
    ("table", "Tabletop", "kneeling", 1, 1, [], ["wrist", "knee"], "forearms on blocks, pad under the knees"),
    ("catcow", "Cat-cow", "kneeling", 1, 1, ["table"], ["wrist", "knee"], "seated cat-cow, hands on the knees"),
    ("child", "Child's pose", "kneeling", 1, 1, [], ["knee"], "lie on the back, knees hugged in"),
    ("dog", "Downward dog", "arm support", 3, 2, ["table"], ["wrist", "headdown"], "hands on a wall or a chair seat"),
    ("plank", "Plank", "arm support", 3, 2, ["table"], ["wrist"], "plank against a wall"),
    ("sideplank", "Side plank", "arm support", 4, 4, ["plank"], ["wrist", "balance"], "forearm down, bottom knee down"),
    ("chat", "Low push-up", "arm support", 5, 4, ["plank"], ["wrist"], "knees down, or rest in child's pose"),
    ("squat", "Garland squat", "standing", 2, 2, ["chair"], ["knee"], "sit on a block"),
    ("crow", "Crow", "arm support", 5, 5, ["squat", "plank"], ["wrist", "headdown"], "squat with hands down, feet stay on the floor"),
    ("dolphin", "Dolphin", "inversion", 4, 3, ["dog"], ["headdown"], "forearms on a chair seat, head above the heart"),
    ("headstand", "Supported headstand", "inversion", 5, 5, ["dolphin"], ["headdown"], "legs up the wall"),
    ("legsup", "Legs up the wall", "rest", 1, 1, [], [], ""),
    ("sphinx", "Sphinx", "backbend", 1, 1, [], [], ""),
    ("cobra", "Low cobra", "backbend", 2, 2, ["sphinx"], ["back"], "sphinx, small range"),
    ("locust", "Locust", "backbend", 3, 2, ["sphinx"], ["back"], "one leg at a time, chest down"),
    ("bridge", "Bridge", "backbend", 2, 2, [], [], ""),
    ("updog", "Upward dog", "backbend", 4, 3, ["cobra", "plank"], ["wrist", "back"], "sphinx or low cobra"),
    ("camel", "Camel", "backbend", 4, 4, ["cobra", "bridge"], ["knee", "back"], "hands on the low back, small range"),
    ("wheel", "Wheel", "backbend", 5, 5, ["bridge", "updog"], ["wrist", "back"], "bridge, or a block under the sacrum"),
    ("staff", "Seated staff", "seated", 1, 1, [], [], ""),
    ("sfold", "Seated forward fold", "seated", 2, 2, ["staff"], ["back"], "sit on a block, knees bent"),
    ("twist", "Seated twist", "seated", 2, 2, ["staff"], [], ""),
    ("stwist", "Lying twist", "seated", 1, 1, [], [], ""),
    ("boat", "Boat", "seated", 4, 3, ["staff"], ["back"], "hands behind the thighs, feet down"),
    ("fig4", "Lying figure four", "seated", 1, 1, [], [], ""),
    ("pigeon", "Pigeon", "seated", 3, 3, ["fig4", "lowlunge"], ["knee"], "lying figure four"),
    ("rest", "Rest", "rest", 1, 1, [], [], ""),
]

FLAGS = ["wrist", "knee", "balance", "back", "headdown"]
FLAG_LABEL = {
    "wrist": "wrist: weight on the hands is uncomfortable",
    "knee": "knee: kneeling or deep bending is uncomfortable",
    "balance": "balance: unsteady on one leg",
    "back": "back: told to go easy on deep back bends and loaded folds",
    "headdown": "head below heart: advised by their doctor to avoid it",
}

# The Juniper Studio beginner cohort (constructed): 12 students, one flag at most each.
COHORT = {"size": 12, "flags": {"wrist": 3, "knee": 2, "balance": 1, "back": 1, "headdown": 0}}
# Break button: one student joins in week 5 with a referral flag the plan did not expect.
LATE_JOINER = {"week": 5, "flag": "headdown"}

CEILING_START = 2   # loads a first-night beginner meets comfortably (teaching assumption)
SPIKE_JUMP = 2      # a week whose top load exceeds everything met so far by 2+ levels

FOUNDATION = ["mtn", "hfold", "war2", "tree", "table", "catcow", "sphinx", "bridge", "staff", "stwist", "rest"]

LINEAR = [
    FOUNDATION,
    ["mtn", "chair", "war2", "tri", "tree", "table", "dog", "cobra", "bridge", "twist", "rest"],
    ["mtn", "chair", "lowlunge", "lunge", "war1", "side", "dog", "plank", "locust", "boat", "rest"],
    ["chair", "war1", "war3", "pyr", "dog", "plank", "sideplank", "updog", "boat", "sfold", "rest"],
    ["chair", "war3", "halfmoon", "eagle", "dog", "dolphin", "chat", "updog", "camel", "boat", "rest"],
    ["war3", "halfmoon", "eagle", "dolphin", "chat", "updog", "squat", "crow", "camel", "boat", "rest"],
    ["halfmoon", "war3", "dolphin", "headstand", "chat", "updog", "crow", "sideplank", "camel", "wheel", "rest"],
    ["halfmoon", "eagle", "headstand", "chat", "crow", "sideplank", "wheel", "camel", "boat", "updog", "rest"],
]

WAVE = [
    FOUNDATION,
    ["mtn", "hfold", "chair", "war2", "tree", "table", "catcow", "dog", "sphinx", "cobra", "bridge", "staff", "fig4", "rest"],
    ["mtn", "chair", "table", "lowlunge", "war2", "tri", "tree", "dog", "plank", "cobra", "bridge", "fig4", "twist", "rest"],
    ["mtn", "hfold", "war2", "tri", "tree", "table", "catcow", "sphinx", "bridge", "staff", "fig4", "stwist", "rest"],
    ["chair", "table", "lowlunge", "lunge", "war1", "tri", "tree", "dog", "plank", "cobra", "locust", "pigeon", "twist", "rest"],
    ["chair", "lunge", "war1", "side", "tree", "war3", "dog", "plank", "cobra", "locust", "pigeon", "twist", "rest"],
    ["mtn", "war2", "tri", "side", "tree", "table", "catcow", "sphinx", "bridge", "pigeon", "stwist", "rest"],
    ["mtn", "chair", "lunge", "war1", "side", "tree", "war3", "dog", "plank", "locust", "pigeon", "twist", "rest"],
]

# Anti-lever "peak pose every week": a different showcase pose closes every class.
PEAKS = ["crow", "wheel", "headstand", "halfmoon", "updog", "camel", "sideplank", "war3"]


def random_plan(seed=7, per_class=11):
    """Rung 1: eleven poses drawn at random from the library each week (seed 7), rest last."""
    rng = random.Random(seed)
    pool = [p[0] for p in POSES if p[0] != "rest"]
    return [rng.sample(pool, per_class - 1) + ["rest"] for _ in range(8)]


RUNGS = [
    {"id": 1, "label": "Random weekly classes", "note": "11 poses drawn at random each week (seed 7)", "plan": random_plan()},
    {"id": 2, "label": "Same class 8 times", "note": "the week 1 foundation class, repeated", "plan": [list(FOUNDATION) for _ in range(8)]},
    {"id": 3, "label": "Linear progression", "note": "harder every week, nothing repeated for long", "plan": LINEAR},
    {"id": 4, "label": "Wave-loaded, with deloads", "note": "foundation, build, integrate, consolidate; lighter weeks 4 and 7", "plan": WAVE},
]

DATA = {
    "note": "Constructed teaching data. Levels 1-5 are a teaching scale, flags are referral tags, not diagnoses.",
    "poses": [
        {"code": c, "name": n, "family": f, "load": l, "cx": x, "pre": pre, "flags": fl, "reg": r}
        for (c, n, f, l, x, pre, fl, r) in POSES
    ],
    "flags": FLAGS,
    "flagLabel": FLAG_LABEL,
    "cohort": COHORT,
    "lateJoiner": LATE_JOINER,
    "ceilingStart": CEILING_START,
    "spikeJump": SPIKE_JUMP,
    "peaks": PEAKS,
    "rungs": RUNGS,
}


def check():
    codes = {p[0] for p in POSES}
    assert len(codes) == len(POSES)
    for p in POSES:
        for q in p[5]:
            assert q in codes, (p[0], q)
        for f in p[6]:
            assert f in FLAGS
        assert (p[7] != "") == (len(p[6]) > 0), p[0]
    for r in RUNGS:
        assert len(r["plan"]) == 8
        for wk in r["plan"]:
            for c in wk:
                assert c in codes, c
            assert len(set(wk)) == len(wk), wk
    for c in PEAKS:
        assert c in codes


if __name__ == "__main__":
    check()
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "..", "assets", "yc-data.js")
    body = json.dumps(DATA, separators=(",", ":"), ensure_ascii=True)
    with open(out, "w") as fh:
        fh.write("/* yc-data.js - generated by materials/build_yc_data.py with json.dumps. Constructed teaching data. */\n")
        fh.write("(function (root) { var D = " + body + ";\n")
        fh.write("if (typeof module !== \"undefined\" && module.exports) module.exports = D; else root.YC_DATA = D; })(this);\n")
    print("wrote", os.path.normpath(out), len(body), "bytes;", len(POSES), "poses")
