# group_tactics.py — group behavior for BrainKit packs and factions.
#
# Two verified models from the primary literature, and nothing else:
#   * WolfPackHunt  — Muro et al.'s two-rule wolf-pack model (2011).
#   * FactionPatrol — the Taï chimpanzee recon -> assess -> advance/retreat
#     loop (Lemoine et al. 2023), plus a qualitative fission-risk hook from
#     the Ngogo split (Sandel et al.).
#
# WHAT THIS IS:     behavioral rules for BrainKit's FactionSim and for pack
#                   creatures — simulation logic at layers 2 and 4 of the
#                   archive (cognition, simulation rules).
# WHAT THIS IS NOT: brain data. No wiring, no neurons, no connectome. These
#                   are published models of *behavior*, honestly labeled.
#
# SOURCES + LICENSES (verified at source, 2026-10-20; see
# research_notes/predator-brain-datasets.md, sections P1/P3 and W1):
#   * Muro C, Escobedo R, Spector L, Coppinger RP, "Wolf-pack (Canis lupus)
#     hunting strategies emerge from simple rules in computational
#     simulations", Behavioural Processes 88(3):192-197, 2011.
#     PMID 21963347, DOI 10.1016/j.beproc.2011.09.006. The paper is a
#     standard copyrighted journal article (NOT open access); the two-rule
#     model is implemented here in original code from the published
#     abstract, as is normal scientific practice.
#   * Lemoine S, Samuni L, Crockford C, Wittig RM, "Chimpanzees make
#     tactical use of high elevation in territorial contexts", PLoS Biology
#     21(11): e3002350, 2023. License CC-BY 4.0 (attribution required).
#   * Sandel et al., Ngogo community fission, Science (via the archive's
#     verified summary). Used qualitatively only — outcomes, not numbers.
#   * This code is Alice's, MIT-shareable per her ethic: everything free.

import math
import random


def _unit(dx, dy):
    d = math.hypot(dx, dy)
    if d == 0.0:
        return (0.0, 0.0)
    return (dx / d, dy / d)


# --- The wolf pack, hunting -------------------------------------------------
# Muro et al. (2011), abstract, verbatim in substance: two decentralized
# rules "(1) move towards the prey until a minimum safe distance to the prey
# is reached, and (2) when close enough to the prey, move away from the other
# wolves that are close to the safe distance to the prey" are enough to
# reproduce tracking, pursuit, and encircling the prey until it stops moving.
# No communication, no hierarchy — encirclement is emergent.

class WolfPackHunt:
    def __init__(self, n_wolves=6, seed=7):
        # All numeric parameters below are DESIGN CHOICEs — not from
        # literature. Muro et al. specify the rules; their simulation's
        # constants are not universal wolf constants, and neither are ours.
        self.safe_distance = 6.0   # DESIGN CHOICE — the ring radius (rule 1's threshold)
        self.wolf_speed = 1.0      # DESIGN CHOICE
        self.prey_speed = 0.5      # DESIGN CHOICE — prey at half wolf speed; at ~0.6+ the ring often never closes (tested)
        self.ring_band = 1.5       # DESIGN CHOICE — a wolf counts as "on the ring" within safe_distance * ring_band of the prey (rule 2's scope)
        rng = random.Random(seed)
        self.prey = [0.0, 0.0]
        self.wolves = [[rng.uniform(-30.0, 30.0), rng.uniform(-30.0, 30.0)]
                       for _ in range(n_wolves)]
        self.steps = 0

    def _encircled(self):
        # Encirclement metric — DESIGN CHOICE (the paper describes
        # encirclement qualitatively: wolves spread around the prey until
        # it stops). Here: every wolf on/near the ring, and no escape gap
        # wider than 150 degrees between neighboring wolves.
        px, py = self.prey
        bearings = []
        for wx, wy in self.wolves:
            if math.hypot(wx - px, wy - py) > self.safe_distance * 1.75:  # DESIGN CHOICE tolerance
                return False
            bearings.append(math.atan2(wy - py, wx - px))
        bearings.sort()
        gaps = [bearings[i + 1] - bearings[i] for i in range(len(bearings) - 1)]
        gaps.append(bearings[0] + 2.0 * math.pi - bearings[-1])
        return max(gaps) < math.radians(150.0)  # DESIGN CHOICE gap threshold

    def step(self):
        px, py = self.prey
        # Prey flees its NEAREST wolf — DESIGN CHOICE prey rule (the paper's
        # prey agents flee; the escape rule is ours). It matters: fleeing the
        # pack's centroid instead makes the prey run one straight line and
        # the pack settles into a trailing cone that never closes (tested).
        # Fleeing the nearest threat keeps turning the prey into the open
        # arcs, whose wolves repel each other around it — the ring closes.
        # An encircled prey stops moving, as in the paper.
        if not self._encircled():
            wx, wy = min(self.wolves, key=lambda w: math.hypot(w[0] - px, w[1] - py))
            ux, uy = _unit(px - wx, py - wy)
            self.prey = [px + ux * self.prey_speed, py + uy * self.prey_speed]
            px, py = self.prey
        # Wolves: velocities computed from the same snapshot, then applied
        # together — agents are interchangeable, nobody leads (Muro et al.).
        moves = []
        for i, (wx, wy) in enumerate(self.wolves):
            d = math.hypot(px - wx, py - wy)
            if d > self.safe_distance:
                # Rule 1: move towards the prey until the safe distance.
                ux, uy = _unit(px - wx, py - wy)
                moves.append((ux * self.wolf_speed, uy * self.wolf_speed))
            else:
                # Rule 2: at the safe distance, move away from the other
                # wolves that are also close to the safe distance.
                rx = ry = 0.0
                for j, (ox, oy) in enumerate(self.wolves):
                    if i == j:
                        continue
                    if math.hypot(px - ox, py - oy) <= self.safe_distance * self.ring_band:
                        ux, uy = _unit(wx - ox, wy - oy)
                        rx += ux
                        ry += uy
                if d < self.safe_distance:
                    # Never inside the minimum distance: rule 1's boundary.
                    ux, uy = _unit(wx - px, wy - py)
                    rx += ux
                    ry += uy
                ux, uy = _unit(rx, ry)
                moves.append((ux * self.wolf_speed, uy * self.wolf_speed))
        self.wolves = [[w[0] + m[0], w[1] + m[1]]
                       for w, m in zip(self.wolves, moves)]
        self.steps += 1

    def run(self, max_steps=2000):  # DESIGN CHOICE step cap
        while self.steps < max_steps:
            if self._encircled():
                return True, self.steps
            self.step()
        return self._encircled(), self.steps


# --- The faction patrol -----------------------------------------------------
# The verified Taï loop (Lemoine et al. 2023, CC-BY 4.0): travel toward the
# border -> stop on high ground near the perimeter -> rest and listen
# (assessment is mainly acoustic) -> advance or retreat by the assessed
# imbalance of power and the rivals' distance.

# Probability of stopping on a peripheral hill, by travel direction —
# Lemoine et al. 2023, confirmed verbatim in the archive (section P1).
P_STOP_TOWARD_BORDER = 0.5773   # Lemoine et al. 2023, PLoS Biol 21(11): e3002350
P_STOP_TOWARD_CENTER = 0.2509   # Lemoine et al. 2023, PLoS Biol 21(11): e3002350

# Probability of advancing after assessment, by rival distance — the
# paper's decision model as reported by Reuters (2023-11-02) and filed in
# the archive (section P1): ~40% at ~500 m, ~50% at ~1 km, ~60% at ~3 km.
ADVANCE_BY_DISTANCE_M = {500: 0.40, 1000: 0.50, 3000: 0.60}  # Lemoine et al. 2023 via Reuters


def _advance_base(distance_m):
    pts = sorted(ADVANCE_BY_DISTANCE_M.items())
    if distance_m <= pts[0][0]:
        return pts[0][1]
    if distance_m >= pts[-1][0]:
        return pts[-1][1]
    for (d0, p0), (d1, p1) in zip(pts, pts[1:]):
        if d0 <= distance_m <= d1:
            # Linear interpolation between the paper's points —
            # DESIGN CHOICE (the paper reports the points, not a curve).
            return p0 + (p1 - p0) * (distance_m - d0) / (d1 - d0)


class FactionPatrol:
    def __init__(self, party_size, seed=0):
        self.party_size = party_size
        self.rng = random.Random(seed)

    def patrol(self, rival_size, rival_distance_m, toward_border=True):
        """One patrol: returns what the party did and decided."""
        p_stop = P_STOP_TOWARD_BORDER if toward_border else P_STOP_TOWARD_CENTER
        if self.rng.random() >= p_stop:
            # No high-ground stop, no assessment — the party simply comes
            # home uninformed. DESIGN CHOICE consequence (the paper models
            # decisions after hilltop stops; unmodeled case kept simple).
            return {"stopped": False, "decision": "no_recon"}
        # Hilltop: resting and listening. Assessment weighs the imbalance
        # of power (own vs rival party size) against distance — Lemoine
        # et al. 2023. The exact combination below is a DESIGN CHOICE:
        # factor is 1.0 at equal strength, <1 outnumbered, >1 outnumbering.
        base = _advance_base(rival_distance_m)
        factor = 2.0 * self.party_size / (self.party_size + rival_size)  # DESIGN CHOICE formula
        p_advance = min(0.95, base * factor)  # DESIGN CHOICE cap
        decision = "advance" if self.rng.random() < p_advance else "retreat"
        return {"stopped": True, "decision": decision, "p_advance": round(p_advance, 3)}


def fission_check(member_count, bridge_losses):
    """Qualitative fission-risk hook from the Ngogo split — a RULE OF THUMB
    from a documented outcome (Sandel et al.), NOT a fitted model.
    Ngogo's unusually large community (~200 members at peak) began
    fissioning in 2015; researchers suspect strained social ties — group
    size, competition, alpha turnover, and disease killing adults who were
    key bridges between clusters — as contributors. Bridge loss is one
    suspected factor among several, and this hook treats it that way."""
    LARGE_COMMUNITY = 200  # Ngogo's approximate peak membership (archive section P3)
    if member_count >= LARGE_COMMUNITY and bridge_losses > 0:
        return "elevated"   # Ngogo's documented configuration when fission began
    if member_count >= LARGE_COMMUNITY or bridge_losses >= 3:  # DESIGN CHOICE threshold
        return "watch"
    return "low"


# --- Demo -------------------------------------------------------------------
if __name__ == "__main__":
    # The pack hunt: two rules, no orders given. Watch the ring close.
    hunt = WolfPackHunt(n_wolves=6, seed=7)
    caught, steps = hunt.run()
    print(f"WolfPackHunt: encirclement {'ACHIEVED' if caught else 'not achieved'} "
          f"after {steps} steps (6 wolves, Muro et al. 2011 two-rule model)")

    # The patrol: same party, three distances, three different fates.
    patrol = FactionPatrol(party_size=12, seed=3)
    for dist in (500, 1000, 3000):
        print(f"FactionPatrol: 12 vs 10 rivals at {dist} m -> {patrol.patrol(10, dist)}")

    # The slow fracture: size alone strains ties; size + lost bridges broke Ngogo.
    print("fission_check(120 members, 0 bridge losses):", fission_check(120, 0))
    print("fission_check(205 members, 0 bridge losses):", fission_check(205, 0))
    print("fission_check(205 members, 2 bridge losses):", fission_check(205, 2))
