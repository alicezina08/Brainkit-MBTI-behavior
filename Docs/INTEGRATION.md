# Integrating BrainKit with your game

## The 3 adapter jobs (the only game-specific code)

1. **Perception feed** — implement `IWorldAdapter::QueryPerception()`.
   In UE5 this wraps `UAIPerceptionComponent`: sight/hearing/damage stimuli,
   but you must TAG them differentially (`kind:player`, `armor:red`,
   `faction:garou`, individual id `player:<name>`). The stock perception
   system gives you stimuli; the tags are what make it *differentiated*.
2. **Actuation** — implement `ExecuteAction()`: translate `Approach` /
   `Flee` / `Attack` / `OfferFood` into your animation/movement/gameplay
   calls. Keep the Behavior Tree as the executor; BrainKit only votes.
3. **Clocks & persistence** — game time in seconds; save `MemoryLedger` +
   `FactionSim` state into the save game (they're plain data).

## Worked example: goblin sentry

- Profile JSON: taxon mammal, traits aggression 0.8 / sociability 0.7 /
  territoriality 0.9, memory half-life 12h, 64 individuals.
- Player attacks the camp → `interact("player:Alice", threat=1.0, ...,
  {"kind:player","armor:red"})`. Sentry flees, then avoids Alice for days.
- Alice later drops food twice → kindness accumulates; attitude crosses
  positive → sentry approaches instead of raising alarm.
- It tells the faction sim (recruitment event) if Alice keeps helping —
  the tribe's stance shifts without a quest flag ever being set.

## Performance (the honest LOD note)

- `Think()` staggered: 1/4 of agents per tick is plenty.
- Perception radii scaled by `cognitiveBudget()` — smarter creatures literally
  notice more.
- FactionSim ticks every few in-game minutes, not per frame.
- Ledger capped (default 64 individuals); the forgotten are evicted first.

## Mod hooks, by era

- **Now (PC):** UE4SS Lua mods can host the portable core (compile Core/ to a
  DLL, call from Lua) and feed perception from the game's objects.
- **2027+:** Jagex's official CurseForge mod support for Dragonwilds. Revisit
  packaging then.
- Always comply with the game's **modding guidelines** (no cheating vectors:
  this plugin reads world state every AI already sees — it just remembers it).

## What this plugin is NOT

- Not the dialogue/LLM voice layer (separate module; reads the same ledger).
- Not consciousness. Creatures behave *as if* they remember and learn,
  via associative memory — the same mechanism as real animal conditioning.
