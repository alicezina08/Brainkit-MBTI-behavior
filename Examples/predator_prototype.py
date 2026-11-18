# predator_prototype.py — one predator, two architectures, one honest test.
#
# THE QUESTION (Alice's design, 2026-10-20): does connecting BrainKit's
# memory + drives + verified pack rules actually beat the way game
# predators are usually coded — not in a demo cherry-picked to flatter it,
# but head-to-head, same world, same seeds, with the world CHANGED
# mid-run to see who adapts?
#
#   A) ScriptedPredator — the conventional baseline: fixed waypoints,
#      chase the nearest visible prey at a fixed speed, fixed give-up
#      distance, no memory, no drives. This is how shipped game
#      predators are typically written.
#   B) BrainKitWolf — the same body in the same world, but its choices
#      come from BrainKit parts: drives (hunger / fear / fatigue),
#      category perception (prey / packmate / hazard / den are different
#      kinds of thing, not blobs), a MemoryLedger-style place+outcome
#      memory (BrainKit/Core/MemoryLedger, adapted from people to
#      places and tactics), and the verified Muro et al. pack rules.
#
# WHAT THIS IS:     a behavioral model built from published rules +
#                   BrainKit components, run in a toy 2D world.
# WHAT THIS IS NOT: neural data, a measurement of real wolves, or
#                   evidence about production games. Every number the
#                   literature did not give us is a DESIGN CHOICE and is
#                   labeled as one, inline, where it lives.
#
# SOURCES:
#   * Muro C, Escobedo R, Spector L, Coppinger RP, "Wolf-pack (Canis
#     lupus) hunting strategies emerge from simple rules in computational
#     simulations", Behavioural Processes 88(3):192-197, 2011.
#     PMID 21963347, DOI 10.1016/j.beproc.2011.09.006. Copyrighted
#     article; the two-rule model is implemented here in original code
#     from the published abstract, as in group_tactics.py.
#   * MemoryLedger design: BrainKit/Core/MemoryLedger.h — threat/
#     kindness per individual, half-life decay, generalization. Here the
#     "individuals" are PLACES (kill spots attract, injury spots repel)
#     and TACTICS (each keeps its own recent success record). The
#     mechanism — associative memory with forgetting — is the archive's;
#     the adaptation is a DESIGN CHOICE.
#   * This code is Alice's, MIT-shareable per her ethic: everything free.

import math
import random
import time


def _unit(dx, dy):
    d = math.hypot(dx, dy)
    if d == 0.0:
        return (0.0, 0.0)
    return (dx / d, dy / d)


def _dist(ax, ay, bx, by):
    return math.hypot(ax - bx, ay - by)


# --- The world ---------------------------------------------------------------
# One environment class, instantiated twice per seed with identical
# initial conditions — the two predators never share a world, so neither
# can contaminate the other's test.

WORLD_SIZE = 200.0          # DESIGN CHOICE — plane is 200x200 units
DEN = (20.0, 180.0)         # DESIGN CHOICE — den location
HAZARD = (150.0, 60.0, 26.0)  # DESIGN CHOICE — ravine: (x, y, radius)
GRAZE_PRE = (60.0, 60.0)    # DESIGN CHOICE — herd grazing centre, phase 1
GRAZE_POST = (126.0, 66.0)  # DESIGN CHOICE — phase 2: herd grazes at the
                            # ravine's fringe (centre ~24 from hazard centre,
                            # inside its 26 radius) — the world gets crueller
N_PREY = 12                 # DESIGN CHOICE — herd size
PREY_WANDER_R = 18.0        # DESIGN CHOICE — grazing spread around centre
PREY_GRAZE_SPEED = 0.30     # DESIGN CHOICE
PREY_FLEE_PRE = 0.72        # DESIGN CHOICE — prey flee speed, phase 1
PREY_FLEE_POST = 0.97       # DESIGN CHOICE — phase 2: prey are ~35% faster
RESPAWN_DELAY = 150         # DESIGN CHOICE — killed prey is replaced at the
                            # grazing centre after this many ticks, so the
                            # herd (and the test) does not deplete
INJURY_P_PER_TICK = 0.015   # DESIGN CHOICE — chance per tick that a predator
                            # inside the ravine is injured (slips/falls)
INJURY_SLOW_TICKS = 90      # DESIGN CHOICE — injury speed penalty duration
INJURY_SLOW_FACTOR = 0.6    # DESIGN CHOICE — injured speed multiplier
CATCH_RADIUS = 1.6          # DESIGN CHOICE


class Prey:
    __slots__ = ("x", "y", "respawn")

    def __init__(self, x, y):
        self.x, self.y, self.respawn = x, y, 0


class World:
    def __init__(self, seed):
        self.rng = random.Random(seed)
        self.tick = 0
        self.shifted = False
        self.graze = GRAZE_PRE
        self.prey_flee_speed = PREY_FLEE_PRE
        self.prey = []
        for _ in range(N_PREY):
            self.prey.append(Prey(
                self.graze[0] + self.rng.uniform(-PREY_WANDER_R, PREY_WANDER_R),
                self.graze[1] + self.rng.uniform(-PREY_WANDER_R, PREY_WANDER_R)))

    def apply_shift(self):
        """The mid-run change: faster prey, herd grazing at the hazard."""
        self.shifted = True
        self.graze = GRAZE_POST
        self.prey_flee_speed = PREY_FLEE_POST

    def step_prey(self, threats):
        """threats: list of (x, y, alarm_radius). A prey flees the nearest
        threat that is inside that threat's alarm radius — a slowly
        stalking predator alarms prey less than a charging one.
        DESIGN CHOICE prey rule (as in group_tactics.py, the paper's prey
        flee; the alarm-radius refinement is ours)."""
        for p in self.prey:
            if p.respawn > 0:
                p.respawn -= 1
                if p.respawn == 0:
                    p.x = self.graze[0] + self.rng.uniform(-6.0, 6.0)
                    p.y = self.graze[1] + self.rng.uniform(-6.0, 6.0)
                continue
            nearest, nd = None, None
            for (tx, ty, alarm) in threats:
                d = _dist(p.x, p.y, tx, ty)
                if d < alarm and (nd is None or d < nd):
                    nearest, nd = (tx, ty), d
            if nearest is not None:
                ux, uy = _unit(p.x - nearest[0], p.y - nearest[1])
                p.x += ux * self.prey_flee_speed
                p.y += uy * self.prey_flee_speed
            else:
                # Graze: drift toward the grazing centre + small wander.
                ux, uy = _unit(self.graze[0] - p.x, self.graze[1] - p.y)
                p.x += ux * PREY_GRAZE_SPEED * 0.4 + self.rng.uniform(-0.15, 0.15)
                p.y += uy * PREY_GRAZE_SPEED * 0.4 + self.rng.uniform(-0.15, 0.15)
            p.x = min(max(p.x, 2.0), WORLD_SIZE - 2.0)
            p.y = min(max(p.y, 2.0), WORLD_SIZE - 2.0)

    def kill_prey(self, p):
        p.respawn = RESPAWN_DELAY
        p.x, p.y = -100.0, -100.0  # off-plane while awaiting replacement

    def in_hazard(self, x, y):
        hx, hy, hr = HAZARD
        return _dist(x, y, hx, hy) < hr


# --- Predator bodies ---------------------------------------------------------
# Shared physics: position, injury slow-down, distance accounting.
# The architectures differ ONLY in how they decide. Same top speeds are
# offered to both (the scripted baseline simply never uses stalk/sprint —
# fixed-speed chasing is its defining limitation, per the task design).

class PredatorBase:
    SPEED_PATROL = 0.8    # DESIGN CHOICE
    SPEED_CHASE = 1.0     # DESIGN CHOICE — the scripted predator's only hunt speed
    SPEED_STALK = 0.55    # DESIGN CHOICE — slow approach; alarms prey at 6 not 14
    SPEED_SPRINT = 1.30   # DESIGN CHOICE — the pounce
    ALARM_MOVING = 14.0   # DESIGN CHOICE — prey flee radius vs a moving predator
    ALARM_STALK = 6.0     # DESIGN CHOICE — prey flee radius vs a stalking one

    def __init__(self, seed):
        self.rng = random.Random(seed)
        self.x, self.y = DEN
        self.injury_timer = 0
        self.phase = "pre"
        self.stats = {ph: {"attempts": 0, "kills": 0, "injuries": 0,
                           "distance": 0.0} for ph in ("pre", "post")}
        self.act_ns = 0  # wall-clock cost of this predator's own decisions

    # -- shared physics --
    def _speed(self, base):
        return base * (INJURY_SLOW_FACTOR if self.injury_timer > 0 else 1.0)

    def move_toward(self, tx, ty, base_speed):
        d = _dist(self.x, self.y, tx, ty)
        if d == 0.0:
            return 0.0
        step = min(d, self._speed(base_speed))
        ux, uy = _unit(tx - self.x, ty - self.y)
        self.x += ux * step
        self.y += uy * step
        self.stats[self.phase]["distance"] += step
        return d - step

    def injure(self):
        self.injury_timer = INJURY_SLOW_TICKS
        self.stats[self.phase]["injuries"] += 1

    def threats(self):
        """What the prey can perceive of this predator this tick."""
        return [(self.x, self.y, self.ALARM_MOVING)]

    def act(self, world):
        raise NotImplementedError


# --- A) The conventional scripted predator -----------------------------------

class ScriptedPredator(PredatorBase):
    """Fixed waypoints, fixed chase speed, fixed give-up. No memory, no
    drives, no hazard awareness — the industry-standard game predator."""
    WAYPOINTS = [(40.0, 40.0), (160.0, 40.0), (160.0, 160.0), (40.0, 160.0)]  # DESIGN CHOICE
    SIGHT = 30.0            # DESIGN CHOICE — baseline vision radius
    GIVE_UP_TICKS = 120     # DESIGN CHOICE — fixed chase patience
    GIVE_UP_RADIUS = 70.0   # DESIGN CHOICE — fixed leash from chase start
    COOLDOWN = 20           # DESIGN CHOICE — ticks between chase episodes

    def __init__(self, seed):
        super().__init__(seed)
        self.wp = 0
        self.state = "patrol"
        self.target = None
        self.chase_ticks = 0
        self.chase_origin = None
        self.cooldown = 0

    def threats(self):
        # A charging scripted predator is always at full alarm radius;
        # while patrolling it also moves at speed — same alarm. DESIGN CHOICE.
        return [(self.x, self.y, self.ALARM_MOVING)]

    def act(self, world):
        if self.injury_timer > 0:
            self.injury_timer -= 1
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.state == "chase":
            t = self.target
            if t is None or t.respawn > 0:
                self._end_chase(world, caught=False)
            else:
                self.chase_ticks += 1
                self.move_toward(t.x, t.y, self.SPEED_CHASE)
                if _dist(self.x, self.y, t.x, t.y) < CATCH_RADIUS:
                    self._end_chase(world, caught=True)
                elif (self.chase_ticks > self.GIVE_UP_TICKS
                        or _dist(self.x, self.y, *self.chase_origin) > self.GIVE_UP_RADIUS):
                    self._end_chase(world, caught=False)
            return
        # Patrol: walk the fixed loop, watch for prey.
        wx, wy = self.WAYPOINTS[self.wp]
        if self.move_toward(wx, wy, self.SPEED_PATROL) < 1.0:
            self.wp = (self.wp + 1) % len(self.WAYPOINTS)
        if self.cooldown == 0:
            visible = [p for p in world.prey if p.respawn == 0
                       and _dist(self.x, self.y, p.x, p.y) < self.SIGHT]
            if visible:
                self.target = min(visible, key=lambda p: _dist(self.x, self.y, p.x, p.y))
                self.state = "chase"
                self.chase_ticks = 0
                self.chase_origin = (self.x, self.y)
                self.stats[self.phase]["attempts"] += 1

    def _end_chase(self, world, caught):
        if caught and self.target is not None:
            world.kill_prey(self.target)
            self.stats[self.phase]["kills"] += 1
        self.target = None
        self.state = "patrol"
        self.cooldown = self.COOLDOWN


# --- B) The BrainKit wolf -----------------------------------------------------

class PlaceMemory:
    """MemoryLedger adapted from people to places (see header). Each
    remembered spot carries a weight that decays with a half-life —
    recent lessons shout, old lessons whisper, exactly as in
    BrainKit/Core/MemoryLedger."""
    HALF_LIFE = 1500.0   # DESIGN CHOICE — ticks for a place lesson to halve
    RADIUS = 22.0        # DESIGN CHOICE — how far a spot's lesson reaches

    def __init__(self):
        self.spots = []  # (x, y, weight, kind, tick) kind: "kill" | "injury"

    def record(self, x, y, weight, kind, tick):
        self.spots.append((x, y, weight, kind, tick))

    def weight_near(self, x, y, kind, tick):
        total = 0.0
        for (sx, sy, w, k, t) in self.spots:
            if k != kind:
                continue
            d = _dist(x, y, sx, sy)
            if d < self.RADIUS:
                total += w * (0.5 ** ((tick - t) / self.HALF_LIFE)) * (1.0 - d / self.RADIUS)
        return total


class TacticMemory:
    """Each hunting tactic keeps its own recent record — the wolf learns
    from its OWN actions' outcomes (Alice's core engine principle).
    Smoothed success rates over a sliding window; DESIGN CHOICE window
    and smoothing."""
    WINDOW = 12        # DESIGN CHOICE — outcomes remembered per tactic
    PRIOR = (1, 1)     # DESIGN CHOICE — Laplace smoothing (1 fake win, 1 fake loss)

    def __init__(self):
        self.outcomes = {"solo": [], "pack": []}

    def record(self, tactic, success):
        o = self.outcomes[tactic]
        o.append(1 if success else 0)
        del o[:-self.WINDOW]

    def rate(self, tactic):
        o = self.outcomes[tactic]
        return (sum(o) + self.PRIOR[0]) / (len(o) + self.PRIOR[0] + self.PRIOR[1])

    def attempts(self, tactic):
        return len(self.outcomes[tactic])


class BrainKitWolf(PredatorBase):
    # Drive dynamics — ALL DESIGN CHOICEs (no literature gives a wolf a
    # hunger constant; these are the model's dials, labeled as such).
    HUNGER_RISE = 0.0011      # per tick
    HUNGER_PER_KILL = 0.65    # hunger removed by a kill
    HUNT_THRESHOLD = 0.35     # hunger above which hunting is considered
    DESPERATE = 0.80          # hunger above which hazard risk is accepted
    FATIGUE_RISE = 0.0011     # per active tick
    FATIGUE_SPRINT = 0.0020   # extra per sprinting tick
    REST_RECOVER = 0.02       # per resting tick at the den
    REST_START = 0.85         # fatigue that forces a rest trip
    REST_END = 0.15           # fatigue that ends a rest
    FEAR_PER_INJURY = 0.5     # fear spike per injury
    FEAR_DECAY = 0.002        # per tick
    # Solo stalk — DESIGN CHOICEs.
    POUNCE_RANGE = 9.0
    STALK_TIMEOUT = 220
    POUNCE_TIMEOUT = 70
    # Pack hunt (Muro et al. 2011 rules; constants DESIGN CHOICE as in
    # group_tactics.py).
    PACK_SIZE = 3             # packmates joining the focal wolf
    PACK_SAFE_DISTANCE = 6.0
    PACK_TIMEOUT = 350
    HUNT_COOLDOWN = 30        # DESIGN CHOICE ticks between hunt episodes

    def __init__(self, seed, ablate=None):
        # ablate: None | "tactics" | "places" | "drives" — which BrainKit
        # component is switched off for an ablation run. Every "off"
        # state is a DESIGN CHOICE documented below; the off variant is
        # compared against the full wolf on identical seeds.
        super().__init__(seed)
        self.ablate = ablate
        if ablate == "drives":
            # No drives: hunger/fear/fatigue pinned to fixed mid values —
            # always hungry enough to hunt (0.6 > 0.35 threshold), never
            # desperate (< 0.80), never afraid, never tired. The wolf hunts
            # on sight + cooldown, like the scripted baseline, but keeps
            # its memory machinery. DESIGN CHOICE off-state.
            self.hunger = 0.6
            self.fear = 0.0
            self.fatigue = 0.0
        else:
            self.hunger = 0.3     # DESIGN CHOICE starting drives
            self.fear = 0.0
            self.fatigue = 0.2
        self.places = PlaceMemory()
        self.tactics = TacticMemory()
        self.state = "decide"  # decide | rest | stalk | pounce | pack | avoid
        # Diagnostics only (never read by any decision): per-phase tactic use.
        self.tactic_use = {ph: {"solo": [0, 0], "pack": [0, 0]}
                           for ph in ("pre", "post")}  # [attempts, kills]
        self.target = None
        self.state_ticks = 0
        self.cooldown = 0
        self.packmates = []    # [x, y, injury_timer] while a pack hunt runs
        self.wander = None

    # -- perception: categories, not blobs (Alice's engine principle) --
    def perceive(self, world):
        seen = {"prey": [], "hazard": HAZARD, "den": DEN,
                "packmates": self.packmates}
        for p in world.prey:
            if p.respawn == 0:
                seen["prey"].append(p)
        return seen

    def threats(self):
        alarm = self.ALARM_STALK if self.state == "stalk" else self.ALARM_MOVING
        out = [(self.x, self.y, alarm)]
        for (mx, my, _t) in self.packmates:
            out.append((mx, my, self.ALARM_MOVING))
        return out

    def extra_agents(self):
        return self.packmates

    def injure(self):
        super().injure()
        if self.ablate == "places":
            pass  # ablation: no injury-spot recording (place memory off)
        else:
            self.places.record(self.x, self.y, 1.0, "injury", self._tick)
        if self.ablate == "drives":
            pass  # ablation: no fear response (drives off)
        else:
            self.fear = min(1.0, self.fear + self.FEAR_PER_INJURY)

    # -- the decision layer: drives + memory choose, no fixed script --
    def act(self, world):
        self._tick = world.tick
        if self.injury_timer > 0:
            self.injury_timer -= 1
        if self.ablate != "drives":
            self.fear = max(0.0, self.fear - self.FEAR_DECAY)  # a drive: pinned when ablated
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.state in ("stalk", "pounce"):
            self._solo(world)
        elif self.state == "chase":
            # Ablation "stalk" only: straight scripted-style chase replaces
            # the stalk-and-pounce machinery for the solo tactic.
            self._chase(world)
        elif self.state == "pack":
            self._pack(world)
        elif self.state == "rest":
            self._rest(world)
        else:
            self._decide(world)
        # Drives move last: activity tires, time hungers (DESIGN CHOICE rates).
        # Ablated "drives" variant pins all three drives — nothing moves.
        if self.ablate != "drives":
            self.hunger = min(1.0, self.hunger + self.HUNGER_RISE)
            if self.state != "rest":
                self.fatigue = min(1.0, self.fatigue + self.FATIGUE_RISE)

    def _decide(self, world):
        seen = self.perceive(world)
        # Exhaustion outranks everything: a wrecked wolf goes home.
        if self.fatigue > self.REST_START:
            self.state = "rest"
            self._rest(world)
            return
        # Caution: inside the ravine and not hunting — get out (the
        # "avoid area" action). A desperate wolf overrides its own fear;
        # that trade is the drives working as designed, and it is labeled
        # a DESIGN CHOICE, not a wolf fact.
        if world.in_hazard(self.x, self.y) and self.hunger < self.DESPERATE:
            hx, hy, _r = HAZARD
            ux, uy = _unit(self.x - hx, self.y - hy)
            self.move_toward(self.x + ux * 10.0, self.y + uy * 10.0,
                             self.SPEED_PATROL)
            return
        if self.hunger > self.HUNT_THRESHOLD and self.cooldown == 0 and seen["prey"]:
            self._start_hunt(world, seen)
            return
        # Otherwise patrol — toward the best remembered hunting ground if
        # memory offers one, else a fresh wander point (DESIGN CHOICE).
        # Ablated "places" variant never uses kill-spot memory: always wanders.
        dest = None
        if self.ablate != "places":
            best = 0.05  # DESIGN CHOICE — minimum remembered value worth walking to
            for (sx, sy, _w, k, _t) in self.places.spots:
                if k == "kill":
                    v = self.places.weight_near(sx, sy, "kill", world.tick)
                    if v > best:
                        best, dest = v, (sx, sy)
        if dest is None:
            if self.wander is None or _dist(self.x, self.y, *self.wander) < 2.0:
                self.wander = (self.rng.uniform(20.0, 180.0),
                               self.rng.uniform(20.0, 180.0))
            dest = self.wander
        self.move_toward(dest[0], dest[1], self.SPEED_PATROL)

    def _start_hunt(self, world, seen):
        # Tactic choice from its OWN record: prefer the better recent
        # rate; a tactic with almost no attempts gets explored
        # (DESIGN CHOICE exploration rule and margins).
        # Ablated "tactics" variant: coin flip instead of the record —
        # the principled no-learning control (both tactics stay available).
        if self.ablate == "tactics":
            tactic = "pack" if self.rng.random() < 0.5 else "solo"
        else:
            solo_r, pack_r = self.tactics.rate("solo"), self.tactics.rate("pack")
            if self.tactics.attempts("pack") < 3:
                tactic = "pack"
            elif self.tactics.attempts("solo") < 3:
                tactic = "solo"
            else:
                tactic = "pack" if pack_r > solo_r else "solo"
        # Target choice: nearest prey, discounted by remembered injury
        # spots and by live hazard proximity — caution scales DOWN as
        # hunger rises: a starving wolf accepts the ravine's fringe.
        # Ablated "places" variant skips the injury-spot discount.
        caution = (1.0 - 0.7 * self.hunger) * (0.5 + self.fear)
        best_prey, best_score = None, None
        for p in seen["prey"]:
            score = -_dist(self.x, self.y, p.x, p.y)
            if self.ablate != "places":
                score -= 25.0 * caution * self.places.weight_near(
                    p.x, p.y, "injury", world.tick)
            if world.in_hazard(p.x, p.y):
                score -= 30.0 * caution
            if best_score is None or score > best_score:
                best_prey, best_score = p, score
        # If the only prey are in the ravine and the wolf is neither
        # desperate nor calm about it, it waits rather than charges in.
        if (best_prey is not None and world.in_hazard(best_prey.x, best_prey.y)
                and self.hunger < self.DESPERATE and caution > 0.45):  # DESIGN CHOICE gate
            return
        self.target = best_prey
        self.stats[self.phase]["attempts"] += 1
        self.tactic_use[self.phase][tactic][0] += 1
        self.state_ticks = 0
        if tactic == "pack":
            self.state = "pack"
            self.packmates = [[self.x + self.rng.uniform(-3.0, 3.0),
                               self.y + self.rng.uniform(-3.0, 3.0), 0]
                              for _ in range(self.PACK_SIZE)]
        elif self.ablate == "stalk":
            # Ablation "stalk": the solo tactic becomes a straight
            # scripted-style chase (fixed speed, fixed give-up) — same
            # constants as ScriptedPredator for comparability. The wolf
            # keeps its drives, memories, and tactic routing.
            self.state = "chase"
            self.chase_ticks = 0
            self.chase_origin = (self.x, self.y)
        else:
            self.state = "stalk"

    def _end_hunt(self, world, tactic, caught):
        if caught and self.target is not None:
            world.kill_prey(self.target)
            self.stats[self.phase]["kills"] += 1
            self.tactic_use[self.phase][tactic][1] += 1
            if self.ablate != "drives":  # ablation: hunger pinned, kills don't feed
                self.hunger = max(0.0, self.hunger - self.HUNGER_PER_KILL)
            if self.ablate != "places":  # ablation: no kill-spot recording
                self.places.record(self.target.x, self.target.y, 1.0, "kill",
                                   world.tick)
        self.tactics.record(tactic, caught)
        self.target = None
        self.packmates = []
        self.state = "decide"
        self.cooldown = self.HUNT_COOLDOWN

    def _solo(self, world):
        t = self.target
        if t is None or t.respawn > 0:
            self._end_hunt(world, "solo", caught=False)
            return
        self.state_ticks += 1
        d = _dist(self.x, self.y, t.x, t.y)
        if self.state == "stalk":
            self.move_toward(t.x, t.y, self.SPEED_STALK)
            if d < self.POUNCE_RANGE:
                self.state = "pounce"
                self.state_ticks = 0
            elif self.state_ticks > self.STALK_TIMEOUT:
                self._end_hunt(world, "solo", caught=False)
        else:  # pounce — sprint, with hunger buying persistence
            if self.ablate != "drives":  # ablation: fatigue pinned, sprinting doesn't tire
                self.fatigue = min(1.0, self.fatigue + self.FATIGUE_SPRINT)
            self.move_toward(t.x, t.y, self.SPEED_SPRINT)
            # Persistence scales with hunger (DESIGN CHOICE formula):
            # a fed wolf quits a losing chase; a hungry one stays in it.
            patience = 45.0 + 60.0 * self.hunger
            if _dist(self.x, self.y, t.x, t.y) < CATCH_RADIUS:
                self._end_hunt(world, "solo", caught=True)
            elif self.state_ticks > patience or self.state_ticks > self.POUNCE_TIMEOUT + 60:
                self._end_hunt(world, "solo", caught=False)

    def _chase(self, world):
        """Ablation-only: straight scripted-style chase, the solo tactic
        with the stalk-and-pounce machinery removed. Same give-up
        constants as ScriptedPredator (120 ticks / 70 units)."""
        t = self.target
        if t is None or t.respawn > 0:
            self._end_hunt(world, "solo", caught=False)
            return
        self.chase_ticks += 1
        self.move_toward(t.x, t.y, self.SPEED_CHASE)
        if _dist(self.x, self.y, t.x, t.y) < CATCH_RADIUS:
            self._end_hunt(world, "solo", caught=True)
        elif (self.chase_ticks > 120
                or _dist(self.x, self.y, *self.chase_origin) > 70.0):
            self._end_hunt(world, "solo", caught=False)

    def _pack(self, world):
        """Muro et al. (2011), the two rules, exactly as in
        group_tactics.py: (1) move toward the prey until the safe
        distance; (2) at the safe distance, move away from the other
        wolves near it. Encirclement is emergent; nobody commands."""
        t = self.target
        if t is None or t.respawn > 0:
            self._end_hunt(world, "pack", caught=False)
            return
        self.state_ticks += 1
        wolves = [[self.x, self.y]] + [[m[0], m[1]] for m in self.packmates]
        if self._encircled(wolves, t):
            self._end_hunt(world, "pack", caught=True)
            return
        if self.state_ticks > self.PACK_TIMEOUT:
            self._end_hunt(world, "pack", caught=False)
            return
        moves = []
        for i, (wx, wy) in enumerate(wolves):
            slow = INJURY_SLOW_FACTOR if (i > 0 and self.packmates[i - 1][2] > 0) else 1.0
            if i == 0 and self.injury_timer > 0:
                slow = INJURY_SLOW_FACTOR
            d = _dist(wx, wy, t.x, t.y)
            if d > self.PACK_SAFE_DISTANCE:
                ux, uy = _unit(t.x - wx, t.y - wy)          # rule 1
                moves.append((ux * 1.0 * slow, uy * 1.0 * slow))
            else:
                rx = ry = 0.0
                for j, (ox, oy) in enumerate(wolves):      # rule 2
                    if i != j and _dist(ox, oy, t.x, t.y) <= self.PACK_SAFE_DISTANCE * 1.5:
                        ux, uy = _unit(wx - ox, wy - oy)
                        rx += ux
                        ry += uy
                if d < self.PACK_SAFE_DISTANCE:
                    ux, uy = _unit(wx - t.x, wy - t.y)
                    rx += ux
                    ry += uy
                ux, uy = _unit(rx, ry)
                moves.append((ux * 1.0 * slow, uy * 1.0 * slow))
        # Apply together; account the focal wolf's travel honestly.
        self.stats[self.phase]["distance"] += math.hypot(*moves[0])
        self.x += moves[0][0]
        self.y += moves[0][1]
        for m, mv in zip(self.packmates, moves[1:]):
            m[0] += mv[0]
            m[1] += mv[1]
            if m[2] > 0:
                m[2] -= 1

    def _encircled(self, wolves, prey):
        # Same metric as group_tactics.py (DESIGN CHOICE thresholds,
        # there and here): all wolves near the ring, no gap >= 150 deg.
        bearings = []
        for (wx, wy) in wolves:
            if _dist(wx, wy, prey.x, prey.y) > self.PACK_SAFE_DISTANCE * 1.75:
                return False
            bearings.append(math.atan2(wy - prey.y, wx - prey.x))
        bearings.sort()
        gaps = [bearings[i + 1] - bearings[i] for i in range(len(bearings) - 1)]
        gaps.append(bearings[0] + 2.0 * math.pi - bearings[-1])
        return max(gaps) < math.radians(150.0)

    def _rest(self, world):
        if _dist(self.x, self.y, *DEN) > 3.0:
            self.move_toward(DEN[0], DEN[1], self.SPEED_PATROL)
        else:
            self.fatigue = max(0.0, self.fatigue - self.REST_RECOVER)
            if self.fatigue <= self.REST_END:
                self.state = "decide"


# --- The test ------------------------------------------------------------------

TICKS = 6000        # DESIGN CHOICE — run length
SHIFT_TICK = 3000   # DESIGN CHOICE — the world changes halfway through
DAY = 300           # DESIGN CHOICE — ticks per in-world day (clock only)
SEEDS = (11, 23, 37, 42, 58, 71)  # DESIGN CHOICE — six seeds


def run_one(pred_cls, seed):
    """One predator, one world, the full run. Returns (predator, us/tick)."""
    world = World(seed)
    pred = pred_cls(seed * 1000 + 7)  # same construction seed for both
    for t in range(TICKS):
        world.tick = t
        if t == SHIFT_TICK:
            world.apply_shift()
        pred.phase = "pre" if t < SHIFT_TICK else "post"
        start = time.perf_counter_ns()
        pred.act(world)
        pred.act_ns += time.perf_counter_ns() - start
        world.step_prey(pred.threats())
        # Hazard physics apply to every predator body in the ravine;
        # injury COUNTS in the metrics are the focal predator's only
        # (disclosed in the report).
        if world.in_hazard(pred.x, pred.y) and world.rng.random() < INJURY_P_PER_TICK:
            pred.injure()
        for m in getattr(pred, "packmates", []):
            if world.in_hazard(m[0], m[1]) and world.rng.random() < INJURY_P_PER_TICK:
                m[2] = INJURY_SLOW_TICKS
    return pred, pred.act_ns / TICKS / 1000.0


def _sr(s):
    return (s["kills"] / s["attempts"]) if s["attempts"] else 0.0


def _dpk(s):
    return (s["distance"] / s["kills"]) if s["kills"] else float("nan")


def main():
    results = {}
    for cls, name in ((ScriptedPredator, "Scripted"), (BrainKitWolf, "BrainKit")):
        rows = []
        for seed in SEEDS:
            pred, us_per_tick = run_one(cls, seed)
            rows.append((seed, pred.stats, us_per_tick,
                         getattr(pred, "tactic_use", None)))
        results[name] = rows

    # BrainKit tactic diagnostics: which tactic carried which phase.
    tot = {ph: {"solo": [0, 0], "pack": [0, 0]} for ph in ("pre", "post")}
    for _seed, _stats, _us, tu in results["BrainKit"]:
        for ph in ("pre", "post"):
            for tac in ("solo", "pack"):
                tot[ph][tac][0] += tu[ph][tac][0]
                tot[ph][tac][1] += tu[ph][tac][1]
    n = len(SEEDS)
    print("=== BrainKit tactic use (mean per run, per phase) ===")
    for ph in ("pre", "post"):
        for tac in ("solo", "pack"):
            a, k = tot[ph][tac]
            if a:
                print(f"{ph:>4} {tac:>4}: {a / n:.1f} attempts, {k / n:.1f} kills "
                      f"(success {k / a:.2f})")
            else:
                print(f"{ph:>4} {tac:>4}: unused")

    for name, rows in results.items():
        print(f"\n=== {name} predator ===")
        print(f"{'seed':>5} {'preSR':>6} {'postSR':>7} {'delta':>7} "
              f"{'preK/A':>8} {'postK/A':>8} {'inj':>4} {'preD/K':>8} {'postD/K':>8}")
        for seed, stats, _us, _tu in rows:
            pre, post = stats["pre"], stats["post"]
            print(f"{seed:>5} {_sr(pre):>6.2f} {_sr(post):>7.2f} "
                  f"{_sr(post) - _sr(pre):>+7.2f} "
                  f"{pre['kills']:>3}/{pre['attempts']:<4} "
                  f"{post['kills']:>3}/{post['attempts']:<4} "
                  f"{pre['injuries'] + post['injuries']:>4} "
                  f"{_dpk(pre):>8.1f} {_dpk(post):>8.1f}")
        n = len(rows)
        mpre = {k: sum(r[1]["pre"][k] for r in rows) / n
                for k in ("attempts", "kills", "injuries", "distance")}
        mpost = {k: sum(r[1]["post"][k] for r in rows) / n
                 for k in ("attempts", "kills", "injuries", "distance")}
        sr_pre = mpre["kills"] / mpre["attempts"] if mpre["attempts"] else 0.0
        sr_post = mpost["kills"] / mpost["attempts"] if mpost["attempts"] else 0.0
        dpk_pre = mpre["distance"] / mpre["kills"] if mpre["kills"] else float("nan")
        dpk_post = mpost["distance"] / mpost["kills"] if mpost["kills"] else float("nan")
        print(f"MEANS  success {sr_pre:.3f} -> {sr_post:.3f} "
              f"(adaptation delta {sr_post - sr_pre:+.3f}) | "
              f"attempts {mpre['attempts']:.1f} -> {mpost['attempts']:.1f} | "
              f"kills {mpre['kills']:.1f} -> {mpost['kills']:.1f} | "
              f"injuries {mpre['injuries']:.1f} -> {mpost['injuries']:.1f} | "
              f"dist/kill {dpk_pre:.1f} -> {dpk_post:.1f} | "
              f"decision cost {sum(r[2] for r in rows) / n:.2f} us/tick")
    print(f"\n{TICKS} ticks/run ({TICKS // DAY} days), shift at tick {SHIFT_TICK}: "
          f"prey flee {PREY_FLEE_PRE} -> {PREY_FLEE_POST}, herd moves to the ravine fringe.")


if __name__ == "__main__":
    main()
