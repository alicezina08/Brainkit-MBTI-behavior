# Predator Prototype — Ablation Report

**Date:** 2026-10-20 · **Code:** `ablation.py` + `predator_prototype.py` (BrainKitWolf `ablate=` switch) · **Status:** run complete, results below are from the actual run, unedited.

## The question

The head-to-head (PROTOTYPE_REPORT.md) showed the full BrainKit wolf adapts when the world changes (success 0.619 -> 0.508, delta -0.111) while the scripted predator collapses (0.988 -> 0.250, delta -0.738). This run removes ONE component at a time and replays the identical world on the identical six seeds (11, 23, 37, 42, 58, 71), to find which component the adaptation is made of.

## The variants

- **full** — the complete BrainKit wolf, unmodified (control).
- **no-tactic-memory** — tactic choice by coin flip instead of the wolf's own success record; both tactics stay available (DESIGN CHOICE control).
- **no-place-memory** — no kill-spot or injury-spot recording or lookup; injury still spikes fear (a drive, kept).
- **no-drives** — hunger/fear/fatigue pinned (0.6/0.0/0.0): always hungry enough to hunt, never desperate, never afraid, never tired; hunts on sight + cooldown like the scripted baseline, but keeps its memory machinery (DESIGN CHOICE off-state).
- **no-stalk** — the solo tactic's stalk-and-pounce machinery is replaced by a straight scripted-style chase (same 120-tick / 70-unit give-up as the baseline); drives, memories, and tactic routing all kept.

## Results (means of 6 seeds)

| variant | pre-shift SR | post-shift SR | adaptation delta | kills/run pre→post | injuries/run pre→post | dist/kill pre→post | tactics post-shift (solo/pack attempts) |
|---|---|---|---|---|---|---|---|
| full | 0.619 | 0.508 | -0.111 | 4.3→5.0 | 0.7→1.3 | 525.9→415.6 | 8.7/1.2 |
| no-tactic-memory | 0.632 | 0.520 | -0.112 | 4.0→4.3 | 0.2→2.7 | 570.6→548.6 | 4.2/4.2 |
| no-place-memory | 0.872 | 0.773 | -0.099 | 5.7→5.7 | 2.5→6.3 | 401.6→391.4 | 4.5/2.8 |
| no-drives | 0.947 | 0.851 | -0.095 | 32.7→24.8 | 0.0→8.7 | 75.9→94.5 | 28.5/0.7 |
| no-stalk | 0.455 | 0.521 | +0.066 | 4.2→4.2 | 0.7→2.7 | 605.5→630.2 | 0.8/7.2 |

## Reading the table (written after the run)

**The headline: no single component owns the adaptation.** Remove the
tactic memory, the place memory, the drives, or even the stalk-and-pounce
machinery itself — the success-rate stability across the world shift
survives in every variant (−0.111, −0.112, −0.099, −0.095, +0.066), while
the scripted baseline collapses (−0.738). The adaptation is not a feature
of one module. It is a property of the architecture: multiple tactics,
a router that tracks which one works, and hazard-aware perception shared
by every variant.

**The surprise inside the surprise:** in the no-stalk variant, the
tactic-learning layer did exactly what the first report celebrated — it
noticed its own solo tactic was broken (straight chase: 0.455 pre-shift
success) and rerouted nearly everything to pack hunts post-shift
(0.8 solo vs 7.2 pack attempts; per-seed post-shift solo use falls to
0–2). Post-shift success held at 0.521 — matching the full wolf's 0.508.
The learning layer is a *router*, not just an optimizer: it finds
whichever mechanism still works. Remove the router (no-tactic-memory)
and the wolf still adapts, but it can no longer shift volume to the
working tactic (post-shift solo/pack 4.2/4.2; kills flat 4.3 vs the
full wolf's recovery to 5.0).

**What each component actually owns** — the robust findings are the
profile differences, not the deltas:

- **Tactic memory** → kill-volume recovery and tactic routing. Without
  it the wolf holds its success rate but cannot concentrate effort where
  it works.
- **Place memory** → injury avoidance. Without it, post-shift injuries
  jump 1.3 → 6.3 per run; the wolf kills slightly more (5.7 vs 5.0) but
  bleeds for it. Caution has a price and the memory pays it.
- **Drives** → the satiety economy and fear caution. Without them the
  wolf becomes a memory-guided killing machine: 32.7 pre-shift kills
  (vs 7.0 — it hunts on sight, never stops when fed) at 0.947 success,
  but post-shift injuries of 8.7 per run — essentially the scripted
  predator's injury profile (8.0) with a better chase algorithm. The
  drives are what make it a *creature* instead of a weapon.
- **Stalk machinery** → stable-world competence. Without it the wolf is
  mediocre before the shift (0.455 vs 0.619) — the stealth approach is
  what wins the easy world — and the pack hunt plus the router carry
  the recovery.

**Honest limits.** Six seeds, and the per-seed deltas swing ±0.2 even
within one variant (no-stalk seeds range −0.12 to +0.22), so the small
differences *between* variant means sit inside seed noise — this run
cannot crown one component, and it does not try to. The injury and
volume differences are an order of magnitude larger than the noise and
are the findings to trust. As before: toy 2D world, one predator, design
choices labeled in the code — evidence about this architecture, not
about wolves or shipped games.

**Named next experiment (owed):** an arms-race shift — prey that learn
the wolf's habits across phases, instead of a one-time scripted change —
to test whether the router keeps working when the world adapts back.

