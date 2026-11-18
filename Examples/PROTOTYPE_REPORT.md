# Predator Prototype — Head-to-Head Report

**Date:** 2026-10-20 · **Code:** `predator_prototype.py` (this folder) · **Status:** run complete, results below are from the actual run, unedited.

## What was built

One toy 2D world (200×200 plane, seeded, pure stdlib Python): a 12-prey herd, a ravine hazard zone that injures predators inside it, a den, 300-tick days. Two predators live in **separate, identically-seeded copies** of that world:

- **ScriptedPredator** — the conventional baseline: fixed waypoint patrol, chase nearest visible prey at one fixed speed, fixed give-up (120 ticks / 70 units), no memory, no drives, no hazard awareness.
- **BrainKitWolf** — same body and offered speeds, but decisions come from BrainKit parts: drives (hunger/fear/fatigue, all labeled DESIGN CHOICE), category perception (prey/packmate/hazard/den are distinct kinds), a MemoryLedger-style memory adapted to **places** (kill spots attract, injury spots repel, half-life decay) and **tactics** (solo stalk vs pack hunt each keep a sliding-window success record; the wolf follows its own record), and the verified **Muro et al. 2011** two-rule pack hunt (as in `group_tactics.py`).

**The test:** 6,000 ticks per run, 6 seeds (11, 23, 37, 42, 58, 71). At tick 3,000 the world changes: prey flee speed rises 0.72 → 0.97 (~35% faster) and the herd's grazing centre moves to the ravine's fringe. Metrics are split pre/post shift.

## Results (actual run output)

### Scripted predator

| seed | pre SR | post SR | delta | pre kills/att | post kills/att | injuries | pre dist/kill | post dist/kill |
|---|---|---|---|---|---|---|---|---|
| 11 | 1.00 | 0.20 | −0.80 | 24/24 | 4/20 | 10 | 106.3 | 638.3 |
| 23 | 1.00 | 0.18 | −0.82 | 25/25 | 3/17 | 13 | 102.8 | 835.7 |
| 37 | 1.00 | 0.20 | −0.80 | 25/25 | 3/15 | 10 | 101.8 | 825.8 |
| 42 | 0.97 | 0.37 | −0.60 | 28/29 | 7/19 | 11 | 94.5 | 358.5 |
| 58 | 0.96 | 0.27 | −0.70 | 27/28 | 4/15 | 15 | 95.7 | 604.6 |
| 71 | 1.00 | 0.28 | −0.72 | 30/30 | 5/18 | 11 | 87.6 | 496.6 |
| **mean** | **0.988** | **0.250** | **−0.738** | 26.5/26.8 | 4.3/17.3 | 3.7 → 8.0 per phase | **97.6** | **575.0** |

Decision cost: **7.25 µs/tick**.

### BrainKit predator

| seed | pre SR | post SR | delta | pre kills/att | post kills/att | injuries | pre dist/kill | post dist/kill |
|---|---|---|---|---|---|---|---|---|
| 11 | 0.67 | 0.50 | −0.17 | 4/6 | 4/8 | 2 | 582.1 | 594.2 |
| 23 | 0.57 | 0.55 | −0.03 | 4/7 | 6/11 | 2 | 567.4 | 337.7 |
| 37 | 0.57 | 0.50 | −0.07 | 4/7 | 5/10 | 2 | 562.0 | 397.9 |
| 42 | 0.71 | 0.67 | −0.05 | 5/7 | 6/9 | 1 | 456.8 | 334.5 |
| 58 | 0.71 | 0.36 | −0.35 | 5/7 | 4/11 | 3 | 461.7 | 507.4 |
| 71 | 0.50 | 0.50 | +0.00 | 4/8 | 5/10 | 2 | 558.7 | 407.9 |
| **mean** | **0.619** | **0.508** | **−0.111** | 4.3/7.0 | 5.0/9.8 | 0.7 → 1.3 per phase | **525.9** | **415.6** |

Decision cost: **15.63 µs/tick** (~2.2× the scripted predator's; both are trivial for one agent, the multiplier would matter at population scale). Full suite (12 runs × 6,000 ticks, including prey/world updates): ~4.5 s wall on this machine.

### BrainKit tactic use (diagnostics — which tactic did the work)

| phase | tactic | attempts/run | kills/run | success |
|---|---|---|---|---|
| pre | solo stalk | 4.0 | 2.8 | 0.71 |
| pre | pack hunt | 3.0 | 1.5 | 0.50 |
| post | solo stalk | 8.7 | 4.5 | 0.52 |
| post | pack hunt | 1.2 | 0.5 | 0.43 |

## The honest verdict

**On the headline question — who adapts when the world changes — the BrainKit predator wins clearly.** Its success rate barely moves across the shift (−0.111) while the scripted predator's collapses (−0.738). Its absolute kills actually *rise* post-shift (4.3 → 5.0 per phase) while the scripted predator's fall off a cliff (26.5 → 4.3). It takes a fraction of the injuries in both phases (post-shift 1.3 vs 8.0 per phase — place memory + hazard caution working as designed), and its travel cost per kill *improves* after the shift while the scripted predator's worsens ~6×.

**Where the BrainKit predator lost, plainly:**

1. **In the original, stable world, the scripted predator is simply better.** Pre-shift it kills ~6× as many prey, at ~1/5 the travel per kill, with a higher per-attempt success rate (0.988 vs 0.619). When prey are slow and plentiful, fixed-speed chasing is close to optimal and the stalk-and-pounce machinery is overhead. Part of the kill gap is motivational, not capability — hunger gating means the wolf hunts to satiety (~7 attempts/phase) while the scripted predator attacks on sight (26.8 attempts/phase) — but even per attempt, the baseline wins the easy world. This architecture's value shows up under change, not under stability.
2. **The pack hunt was not the hero.** Post-shift recovery was carried by solo stalking volume (attempts 4.0 → 8.7 per run) — the stealth approach (small alarm radius) plus sprint doesn't depend on outlasting faster prey in a straight chase, which is exactly what kills the scripted predator. Pack hunts underperformed solo in both phases (0.50/0.43 success) and the wolf's own tactic memory correctly benched them (1.2 attempts/run post-shift). The Muro rules were implemented faithfully; in this world, at these speeds (wolves 1.0 vs prey 0.97), the ring rarely closes before timeout. The learning layer deserves the credit for *noticing* that — which is itself the architecture working — but anyone citing this prototype as "pack AI wins" would be misreading it.
3. **Adaptation was partial, not magic.** BrainKit success still declined on average, and on seed 58 it fell −0.35. It degrades gracefully; it does not shrug off the change entirely.
4. **It costs ~2.2× the decision time** of the baseline (15.6 vs 7.3 µs/tick in this Python reference implementation).

## What this prototype does NOT prove

- **Nothing about real wolves.** Drive constants, speeds, radii, and timeouts are DESIGN CHOICEs, hand-set for plausibility, not fitted to field data. The only literature-derived machinery is the Muro et al. two-rule pack model and the MemoryLedger mechanism.
- **Nothing about production games.** One herd configuration, one hazard layout, six seeds, a 2D plane with no terrain, no cover, no other predators, and prey with a two-rule brain of their own.
- **The comparison is architecture-vs-architecture, not equal-toolkit.** The BrainKit wolf has options the baseline lacks by design (stalk/sprint gears, packmates, rest) — that asymmetry *is* the proposal being tested, but it means the test cannot separate "memory/drives help" from "more tools help." An ablation run (BrainKit wolf with memory disabled, drives disabled, etc.) is the obvious next experiment and has not been run.
- **Measurement caveats:** distance/kill counts only the focal predator's travel — packmate travel during pack hunts is excluded, which flatters BrainKit efficiency on its (minority) pack kills. Hunts are tallied in the phase they *end*, so a rare hunt straddling tick 3,000 lands in "post." Injuries are counted for the focal predator only, though packmates can be slowed by the ravine. Per-tick decision timing is this machine, this load, Python — indicative, not a benchmark.

## The one-sentence version

In a world that stays the same, a scripted predator is cheaper and deadlier; in a world that changes — faster prey, food beside danger — the scripted predator breaks and the memory-and-drives predator bends, mostly by learning which of its own tactics still work and hunting *that* way more.

*Behavioral model built from published rules + BrainKit components. Not neural data. Not a measurement of anything real.*
