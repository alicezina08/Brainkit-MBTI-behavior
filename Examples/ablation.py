# ablation.py — which BrainKit component earns the adaptation?
#
# The prototype (PROTOTYPE_REPORT.md) showed the full BrainKit wolf adapts
# when the world changes while the scripted predator collapses. This run
# switches OFF one component at a time — tactic memory, place memory,
# drives — and replays the identical world + seeds, to isolate what the
# adaptation is made of. Every "off" state is a labeled DESIGN CHOICE in
# predator_prototype.py (BrainKitWolf.__init__ ablate=...).
#
# WHAT THIS IS: the same toy 2D world, same 6 seeds, one component
#              removed per variant. WHAT THIS IS NOT: evidence about real
#              wolves, shipped games, or any production system.

import sys
import time

import predator_prototype as P

VARIANTS = [
    (None, "full"),
    ("tactics", "no-tactic-memory"),   # coin-flip tactic choice, both tactics available
    ("places", "no-place-memory"),     # no kill/injury spot recording or lookup
    ("drives", "no-drives"),           # hunger/fear/fatigue pinned; hunts on sight+cooldown
    ("stalk", "no-stalk"),             # solo tactic = straight scripted-style chase
]


def run_variant(ablate):
    rows = []
    for seed in P.SEEDS:
        world = P.World(seed)
        if ablate is None:
            pred = P.BrainKitWolf(seed * 1000 + 7)
        else:
            pred = P.BrainKitWolf(seed * 1000 + 7, ablate=ablate)
        for t in range(P.TICKS):
            world.tick = t
            if t == P.SHIFT_TICK:
                world.apply_shift()
            pred.phase = "pre" if t < P.SHIFT_TICK else "post"
            start = time.perf_counter_ns()
            pred.act(world)
            pred.act_ns += time.perf_counter_ns() - start
            world.step_prey(pred.threats())
            if world.in_hazard(pred.x, pred.y) and world.rng.random() < P.INJURY_P_PER_TICK:
                pred.injure()
            for m in getattr(pred, "packmates", []):
                if world.in_hazard(m[0], m[1]) and world.rng.random() < P.INJURY_P_PER_TICK:
                    m[2] = P.INJURY_SLOW_TICKS
        rows.append((seed, pred.stats, pred.tactic_use))
    return rows


def summarize(rows):
    n = len(rows)
    mpre = {k: sum(r[1]["pre"][k] for r in rows) / n for k in ("attempts", "kills", "injuries", "distance")}
    mpost = {k: sum(r[1]["post"][k] for r in rows) / n for k in ("attempts", "kills", "injuries", "distance")}
    sr_pre = mpre["kills"] / mpre["attempts"] if mpre["attempts"] else 0.0
    sr_post = mpost["kills"] / mpost["attempts"] if mpost["attempts"] else 0.0
    dpk_pre = mpre["distance"] / mpre["kills"] if mpre["kills"] else float("nan")
    dpk_post = mpost["distance"] / mpost["kills"] if mpost["kills"] else float("nan")
    tot = {ph: {"solo": [0, 0], "pack": [0, 0]} for ph in ("pre", "post")}
    for _s, _st, tu in rows:
        for ph in ("pre", "post"):
            for tac in ("solo", "pack"):
                tot[ph][tac][0] += tu[ph][tac][0]
                tot[ph][tac][1] += tu[ph][tac][1]
    solo_post = tot["post"]["solo"][0] / n
    pack_post = tot["post"]["pack"][0] / n
    return dict(sr_pre=sr_pre, sr_post=sr_post, delta=sr_post - sr_pre,
                kills_pre=mpre["kills"], kills_post=mpost["kills"],
                inj_pre=mpre["injuries"], inj_post=mpost["injuries"],
                dpk_pre=dpk_pre, dpk_post=dpk_post,
                solo_post=solo_post, pack_post=pack_post)


def main():
    all_rows = {}
    for ablate, name in VARIANTS:
        t0 = time.time()
        rows = run_variant(ablate)
        all_rows[name] = (rows, summarize(rows))
        print(f"{name}: {time.time() - t0:.1f}s", file=sys.stderr)

    print("\n=== Ablation: adaptation delta per variant (mean of 6 seeds) ===")
    print(f"{'variant':>18} {'preSR':>6} {'postSR':>7} {'delta':>7} "
          f"{'kills pre->post':>15} {'inj pre->post':>13} {'dpk pre->post':>14} "
          f"{'tactics post (solo/pack)':>24}")
    table = []
    for _ablate, name in VARIANTS:
        _rows, s = all_rows[name]
        table.append((name, s))
        print(f"{name:>18} {s['sr_pre']:>6.3f} {s['sr_post']:>7.3f} {s['delta']:>+7.3f} "
              f"{s['kills_pre']:>6.1f}->{s['kills_post']:<6.1f} "
              f"{s['inj_pre']:>5.1f}->{s['inj_post']:<5.1f} "
              f"{s['dpk_pre']:>6.1f}->{s['dpk_post']:<6.1f} "
              f"{s['solo_post']:>10.1f}/{s['pack_post']:<5.1f}")

    # Write the report file.
    with open("ABLATION_REPORT.md", "w") as f:
        f.write("# Predator Prototype — Ablation Report\n\n")
        f.write("**Date:** 2026-10-20 · **Code:** `ablation.py` + `predator_prototype.py` "
                "(BrainKitWolf `ablate=` switch) · **Status:** run complete, "
                "results below are from the actual run, unedited.\n\n")
        f.write("## The question\n\n")
        f.write("The head-to-head (PROTOTYPE_REPORT.md) showed the full BrainKit wolf "
                "adapts when the world changes (success 0.619 -> 0.508, delta -0.111) "
                "while the scripted predator collapses (0.988 -> 0.250, delta -0.738). "
                "This run removes ONE component at a time and replays the identical "
                "world on the identical six seeds (11, 23, 37, 42, 58, 71), to find "
                "which component the adaptation is made of.\n\n")
        f.write("## The variants\n\n")
        f.write("- **full** — the complete BrainKit wolf, unmodified (control).\n")
        f.write("- **no-tactic-memory** — tactic choice by coin flip instead of the "
                "wolf's own success record; both tactics stay available (DESIGN "
                "CHOICE control).\n")
        f.write("- **no-place-memory** — no kill-spot or injury-spot recording or "
                "lookup; injury still spikes fear (a drive, kept).\n")
        f.write("- **no-drives** — hunger/fear/fatigue pinned (0.6/0.0/0.0): always "
                "hungry enough to hunt, never desperate, never afraid, never tired; "
                "hunts on sight + cooldown like the scripted baseline, but keeps its "
                "memory machinery (DESIGN CHOICE off-state).\n")
        f.write("- **no-stalk** — the solo tactic's stalk-and-pounce machinery is "
                "replaced by a straight scripted-style chase (same 120-tick / "
                "70-unit give-up as the baseline); drives, memories, and tactic "
                "routing all kept.\n\n")
        f.write("## Results (means of 6 seeds)\n\n")
        f.write("| variant | pre-shift SR | post-shift SR | adaptation delta | "
                "kills/run pre→post | injuries/run pre→post | dist/kill pre→post | "
                "tactics post-shift (solo/pack attempts) |\n")
        f.write("|---|---|---|---|---|---|---|---|\n")
        for name, s in table:
            f.write(f"| {name} | {s['sr_pre']:.3f} | {s['sr_post']:.3f} | "
                    f"{s['delta']:+.3f} | {s['kills_pre']:.1f}→{s['kills_post']:.1f} | "
                    f"{s['inj_pre']:.1f}→{s['inj_post']:.1f} | "
                    f"{s['dpk_pre']:.1f}→{s['dpk_post']:.1f} | "
                    f"{s['solo_post']:.1f}/{s['pack_post']:.1f} |\n")
        f.write("\n## Reading the table (written after the run)\n\n")
    print("\nResults table drafted; interpretation to be written from the actual numbers.")


if __name__ == "__main__":
    main()
