# Agent brief - shared by every fan-out page of learn-yoga-course-design-with-phoebe

Filled from `~/.claude/skills/course-builder/references/agent-brief.template.md` on 2026-10-12.
Internal build document: never link it from an audience page.

You are writing ONE static HTML session page. No servers, no npm. **If your target file already
exists on disk, do not write it; report that and stop.** Write the file, return its path and one
line of coverage. No HTML in your reply.

## Read first, in this order

1. The template page. Copy its structure, classes, SVG grammar and quiz markup EXACTLY, including
   4 options per question:
   `/Users/phoebe.fu/Documents/claude_work/github_repo/learn-yoga-course-design-with-phoebe/courses/01-a-programme-not-eight-classes.html`
   (also look at `04-the-programme-bench.html` in the same folder for a second example; never edit either.)
2. The source map: every verified number, its evidence tier, per-session coverage, the seams, the
   bench canon. Use ONLY its numbers; never invent a statistic; if a fact is missing, teach the
   uncertainty.
   `/Users/phoebe.fu/Documents/claude_work/github_repo/learn-yoga-course-design-with-phoebe/materials/official-course-map.md`
   Fuller quotes, if you need wording: `materials/research-notes.md` in the same repo (grep it, do not read it whole).
3. The stylesheet `:root` block for the palette tokens (first 30 lines only):
   `/Users/phoebe.fu/Documents/claude_work/github_repo/learn-yoga-course-design-with-phoebe/assets/style.css`
4. Pose data if you name a pose's prerequisites or flags (they must match):
   `/Users/phoebe.fu/Documents/claude_work/github_repo/learn-yoga-course-design-with-phoebe/materials/build_yc_data.py` (POSES list and the WAVE plan).

## Page skeleton (keep every component)

toolbar (crumb EXACTLY "learn-yoga-course-design-with-phoebe / Session N of 6", #toggle-all,
#zoom-toggle) · masthead (eyebrow "Learn Yoga Course Design with Phoebe · Session N of 6", h1 with
one `<span class="accent">`, .sub, .chip-row with the level chip (🟢 Foundations for session 2,
🟡 Core for session 3, 🟠 Deeper for sessions 5 and 6), then audience chip "Aspiring and new yoga
teachers", one more audience chip as in the template, and the time chip "45 min", .agenda a1-a4) ·
main.wrap · section#intro (Part 0: kicker, .lede, .legend pills, .callout.win "★ What you walk out
with tonight") · 3 Parts, each `section.section#part-N` with section-kicker (klabel "Part N ·
covers ...", h2, `.tag.concept "N min live"`), a `.lede`, ONE figure, `details.card` accordions
(summary: `.mode.live` or `.mode.self`, title, `.mini`, `.caret ▶`), at least one
`.callout.example` with `span.ex-pill` "Real world" on the page · section#demo-1 Build-along
(kicker `.tag.demo "★ 22 min · everyone builds"`, .lede, ONE figure, `.steps > .step`, each with a
`.prompt-box.good` carrying a `span.label`; the build-along content is given in your file outline)
· section#exercise Homework (ol, 4 items) · section#quiz (3 x `.quiz-q data-answer="0-based"`,
`p.qtext`, 4 x `button.qopt` "A · ...", `p.qwhy`; one `p.quiz-score` after the last) ·
section#official, h2 EXACTLY "What this session teaches, and where it came from", `.covered >
.covered-row` (pill solid ✓ / light ◐ + name + note), then the `.mono` line EXACTLY "Every fact on
this page, and its verification tier, is recorded in the course's source map." ·
section.cheat#cheatsheet (h3 "Session N cheat sheet <span>· pin this</span>", .grid-2 of six
.cheat-item) · `.callout.next` with `.nx-pill` "Next session" · footer.pagefoot ·
`<script src="../assets/app.js?v=1"></script>`.

Head: the template's social meta block with this page's own title/description/url;
`<title>Session N · <Title> - learn yoga course design with phoebe</title>`;
`<link rel="stylesheet" href="../assets/style.css?v=1">`. Nothing else external.

First `details.card` in the FIRST Part is `open`; no other. Sentence case headings. Warm
practitioner voice, concrete, never dry. Inside prompt-boxes escape `&` `<` `>` (write `-&gt;`).
450 to 650 lines is guidance about depth, never a target: never collapse whitespace, dissolve a list
into a paragraph, or drop a component to fit.

## Hard rules (a violation is rework)

- NEVER an em dash or en dash, anywhere (prose, code, aria-labels, comments). Hyphen only.
- No meta text: never "this course", "in this course", "the course teaches", "banned here". State
  the professional norm directly with its reason. The two exact phrases above are the only
  self-references; "session 5" cross-references are fine.
- Attribution "by Phoebe Fu". Never "built with" a tool.
- Every number comes from the map or is labelled constructed. For constructed data print "your
  numbers will differ", never invented outputs as if run.
- Contested or missing evidence: teach the disagreement; never resolve what the literature has not.
- Citations in the exact short form of the map's appendix; anything tier R is "reported" on the page;
  tier X is never cited with a number.
- NEVER "lottery" or "lotteries"; say the mechanism.
- Default to the English word. Pose names in English (as in build_yc_data.py). Any non-English term
  (Sanskrit included) carries its English in brackets right after it, every occurrence. Better: just
  use the English word.
- Titles, widget ids and class names must not collide with siblings: do not use "A system you
  keep", "The one-page marketing plan", "Is it worth the time?", "Where your week actually goes",
  or any id/class starting `yc-` (reserved for the bench widget). Figure prefixes are yours (below).
- **Seams.** Never re-teach Yoga Theory sessions 5 to 8 (functional anatomy, asana theory,
  sequencing ONE class incl. the peak-pose method and sun salutations, cueing) or its lineage /
  eight limbs / pranayama; link them as inputs. General course design (backwards design, cognitive
  load, assessment, needs analysis) belongs to Course Design; borrow with a link. Verbal spacing
  research (Cepeda) belongs to Reading; cite only the motor-learning sources in the map.
- **Health rules.** NOT medical advice: never diagnose, never dose, never promise a symptom outcome
  ("this programme fixes back pain" is forbidden; "the trial reported" is fine). A caution flag is a
  referral tag, never a diagnosis; the teacher adapts and refers, never assesses. Name when to see a
  professional using the NHS list in the map. Every movement you SHOW has: a hand-drawn stick-figure
  SVG labelled "guide" (never an AI image, never "demo"), seconds or breaths, a safe range in words,
  and a "Stop if" line. Learner data stays in the browser (you should not need any widget).
- Quiz `data-answer` values for YOUR page are given in your outline. Use exactly those.

## Figure grammar (hand-drawn, every figure)

Palette, ONLY these hexes (no invented greys): ink `#2B1E21` · muted `#6B5A5E` · dusty rose
primary `#A14D5E` · deep `#6E2F3C` · mid `#8A3F4F` · soft `#E8C5CC` · tint `#FBF0F2` · faint
`#DCCBCF` · hairline `#EFE4E6` · olive `#6B7A2E` · olive-ink `#4A5520` · olive tint `#F2F4E6` ·
`#FFFFFF` · universal reds `#991B1B` `#FEF2F2` `#FCA5A5` only for a wrong-way panel.

- `<figure class="zoomable">` > `<svg viewBox="0 0 880 H" xmlns="http://www.w3.org/2000/svg"
  role="img" aria-label="the data, not the shape">` > `<defs>` + `<style>` + content, then
  `<figcaption>🔍 Click to zoom - takeaway</figcaption>`. Grow H, never W.
- Prefix unique per figure, used for every class and id: `y<session><letter>` (session 2 uses
  y2a, y2b, y2c, y2d; session 3 y3a...; 5 y5a...; 6 y6a...).
- `<defs>` holds with the figure prefix P: a wobble filter `id="PSk"`
  (`feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="<int>"` +
  `feDisplacementMap scale="2.4" xChannelSelector="R" yChannelSelector="G"`, `x="-3%" y="-3%"
  width="106%" height="106%"`), optionally a hachure pattern `id="PHc"` (7x7 userSpaceOnUse,
  rotate(-38), one `#A14D5E` line, opacity .5), optionally an open arrowhead `id="PAr"` (path
  `M1 1 L9 5 L1 9`, fill none, ink stroke 1.6). ALL shapes sit inside ONE `<g filter="url(#PSk)"
  fill="none" stroke="#2B1E21" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">`;
  rects carry a tiny rotation (-4 to 4 degrees for hand-placed items, under 1 for panels). Fills:
  white, tint, the hachure for "the pile" or "the data", and olive tint with olive stroke ONLY for
  the one thing the figure is about. Never put text directly on the hachure: give it a white rect
  behind, or use tint. One doodle anchor per figure, simple strokes, never a mascot.
- Text classes: `.PH` 800 12px ink heading · `.PL` 600 12px ink label · `.PS` 400 11px muted ·
  `.PB` 800 11px olive-ink `#4A5520` · `.PV` 800 16-20px deep value · `.PW` 800 12px white on a
  primary or deep fill only · `.PA` 700 11px primary caption · `.PN` 400 12px muted note. A red
  wrong-way label may use 800 11px `#991B1B` on white or `#FEF2F2` only.
- ALL `<text>` outside the filtered group, sans stack, never below 10.5px.
- Fit: max chars ≈ (box width - 20) / 7 at 12px, 6.4px/char at 11px; full-width note under 110
  chars; 40px between neighbouring point labels; bottom note 22px below the last row, H clears it by
  8px. When in doubt, shorten.
- Geometry the gate rejects: two filled rects that PARTIALLY overlap (full containment is fine, or
  make pieces abut edge to edge); ANY path or line crossing a text label (gridlines, arrows, limbs,
  curves: route them around labels); text overlapping text; anything outside the viewBox.
- **Stick figures** (movement guides): head `<circle r="10-12" fill="#FFFFFF"/>`, body and limbs as
  paths inside the filtered group, an olive or primary arrow path for the direction of movement, a
  step label under each figure ("wall", "chair", "floor"). 3 or 4 figures across 880 for an options
  ladder. Heading or note says "guide". Each figure carries (in text under it, clear of limbs) a
  hold in breaths or seconds, a safe range, and a "Stop if" line in red-ink `#991B1B`, OR those
  lines appear in a table/prompt-box directly below the figure.
- Floor: one figure per Part plus one in the build-along. Draw the MECHANISM (the prerequisite
  chain, the referral route, the load curve, the options ladder, the decay of practice), never a
  metaphor literally, never decoration.

## Voice and honesty

Every Part gets a real-world story (a familiar studio pattern, stated as a pattern, never a
fabricated named studio or statistic). Constructed case: **Juniper Studio**, a fictional community
studio; owner **Mei**; an 8-week beginner programme, one 60-minute class a week, 12 students; cohort
flags wrist 3, knee 2, balance 1, back 1, none 5. Always say "constructed" the first time Juniper
appears on a page. You may invent first names for constructed students if labelled constructed.
Never use Phoebe's own work, employers or clients. Do not invent a statistic.

## Cross-links (absolute URLs)

- Yoga Theory: https://phoebefu6.github.io/learn-yoga-theory-with-phoebe/ (s5 courses/05-functional-anatomy.html, s6 courses/06-asana-theory.html, s7 courses/07-course-flow.html, s8 courses/08-cueing-analogy.html)
- Course Design: https://phoebefu6.github.io/learn-course-design-with-phoebe/ (courses/a2-backwards-design.html, a3-the-arc.html, a5-assessment-and-feedback.html, b1-needs-analysis.html, b5-measuring-change.html)
- Reading (verbal spacing): https://phoebefu6.github.io/learn-reading-with-phoebe/courses/05-spacing-and-forgetting.html
- Office Energy: https://phoebefu6.github.io/learn-office-energy-with-phoebe/
- Hub: https://phoebefu6.github.io/learn-with-phoebe/

## Footer chain and session titles

Footer left: "Session N of 6 · learn-yoga-course-design-with-phoebe · by Phoebe Fu &nbsp;·&nbsp; 📚 <a href="https://phoebefu6.github.io/learn-with-phoebe/">Learn with Phoebe ↗</a>"
Footer right: `<a href="PREV">← Prev: <title></a> &nbsp;·&nbsp; <a href="NEXT">Next: <title> →</a>`
(session 6: "← Prev: One room, many levels" and `<a href="../index.html">Course home</a>`).

Session titles and files (exact, sentence case, one accent span in h1):
1. A programme is not eight classes in a row - 01-a-programme-not-eight-classes.html
2. Intake: who is in the room - 02-intake-who-is-in-the-room.html
3. Progressions across weeks - 03-progressions-across-weeks.html
4. The programme bench - 04-the-programme-bench.html
5. One room, many levels - 05-one-room-many-levels.html
6. Finishing well, and what comes next - 06-finishing-well.html
