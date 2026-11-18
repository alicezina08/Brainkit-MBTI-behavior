# living_npc_minimal.py — the design-around in miniature.
# No hierarchies, no ranks, no vendetta flags: just associative memory.
# This is the same architecture as BrainKit/Core/MemoryLedger (C++17),
# distilled to its readable essence so any studio can see the idea at a glance.

class MemoryLedger:
    def __init__(self, half_life_hours=24):
        self.people = {}      # individual_id -> {"threat", "kindness", "seen"}
        self.categories = {}  # e.g. "red_armor" -> {"threat", "kindness"}
        self.half_life = half_life_hours * 3600

    def interact(self, who, threat=0.0, kindness=0.0, tags=(), now=0.0):
        m = self.people.setdefault(who, {"threat": 0.0, "kindness": 0.0, "seen": now})
        self._decay(m, now)
        m["threat"] += threat
        m["kindness"] += kindness
        m["seen"] = now
        for tag in tags:  # a slice of every lesson generalizes: individuals -> categories
            c = self.categories.setdefault(tag, {"threat": 0.0, "kindness": 0.0})
            c["threat"] += threat * 0.3
            c["kindness"] += kindness * 0.3

    def attitude(self, who, now):
        """Net attitude: >0 warm, <0 hostile, ~0 neutral. Decayed to now."""
        m = self.people.get(who)
        if not m:
            return 0.0
        self._decay(m, now)
        return m["kindness"] - m["threat"]

    def _decay(self, m, now):
        dt = now - m["seen"]
        factor = 0.5 ** (dt / self.half_life)  # forgetting curve, like real memory
        m["threat"] *= factor
        m["kindness"] *= factor


# --- The goblin sentry, thinking -------------------------------------------
ledger = MemoryLedger(half_life_hours=12)

t0 = 0.0
ledger.interact("player:Alice", threat=1.0,
                tags=["kind:player", "armor:red"], now=t0)   # she raided the camp

t1, t2 = 86400.0, 172800.0                                    # a day, two days later
ledger.interact("player:Alice", kindness=0.6, now=t1)          # she left food
ledger.interact("player:Alice", kindness=0.6, now=t2)          # ...and again

a = ledger.attitude("player:Alice", now=200000.0)
if a > 0.5:
    approach("player:Alice")   # befriended — Nemesis has no code path for this
elif a < -0.5:
    raise_alarm()              # threatened
else:
    watch_cautiously()         # neutral
