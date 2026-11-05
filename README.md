# BrainKit — a universal creature-brain plugin scaffold

Gives game creatures and NPCs a real cognitive architecture instead of a
single behavior script: a sized brain, differentiated perception, individual
memory (threats *and* kindness), relationships, and faction dynamics.

## What "universal" means here (honest version)

- **Portable core** (`Core/`): pure C++17, zero engine dependencies. Trait
  vectors, allometric brain sizing, the memory ledger, and the faction
  simulator compile anywhere — Unreal, Unity (via a C++ plugin), or a custom
  engine.
- **One data contract** (`Schema/creature_profile.schema.json`): the same JSON
  the Dragonwilds Creature Brain Database app exports. Author brains in the
  app, load them at runtime. Any game, same format.
- **Thin adapters** (`Unreal/`): the *only* game-specific part. Implement two
  small interfaces (world-state feed, actuation) for your game and the core
  runs unmodified. A worked example is in `Docs/INTEGRATION.md`.

It is not magic plug-and-play: every game feeds perception and executes
actions differently, so the adapter is real work — but it is *bounded* work,
and everything above it is reusable.

## Honesty box (read before using)

1. This is a **reference scaffold**, reviewed by reading, not by compiling.
   There is no Unreal toolchain in this environment, so treat it as a
   carefully designed starting point your modder compiles and tests.
2. It provides **behavior as if alive** — memory, learning, relationships,
   factions. It does not produce consciousness, and nothing here claims to.
3. Body masses in the source data are **fan estimates**; the allometry math
   (Jerison, grams — see `BrainProfile`) is real, the inputs are approximate.
   "Sapience / magic / undeath" multipliers are labeled fan parameters.
4. The **dialogue/LLM layer is separate** (see the app's modder bridge). This
   plugin is the mind; the voice is another module that reads the same memory.
5. You need **mod hooks** to inject this into a shipped game: UE4SS Lua on PC
   today; official Dragonwilds mod support (CurseForge) is on Jagex's 2027
   roadmap. Respect the game's modding guidelines.

## Layout

```
BrainKit/
  Core/        portable brain: profiles, allometry, memory ledger, factions
  Unreal/      thin UE glue: component + adapter interfaces (game-specific)
  Schema/      JSON data contract for creature profiles
  Docs/        integration guide with a worked goblin-sentry example
```

## The stack (each layer emerges from the one below)

brain/allometry (capacity) → differentiated perception (world model) →
individual memory + relationships → life sim (daily living) →
faction simulation (collective dynamics)

## The plug-in standard (Alice, 2026-10-20)

How BrainKit enters any new game world — the same every time:

1. **Core stays, lore swaps.** The cognitive architecture (drives, perception,
   memory ledger, decisions, factions) is game-agnostic. Only the lore layer —
   species data, provenance cards, the world adapter — changes per game.
2. **Verified data only.** Grounding material must be public domain, CC0, or
   CC-BY, confirmed on the source's own page. Everything else is cite-only or
   reference-only. No license is ever taken on faith.
3. **Prototype before plug-in.** Each new world gets a head-to-head test: a
   BrainKit creature against a conventional scripted baseline, same
   environment, same seeds, with a scoreboard. Adaptation after a mid-run
   world change is the headline metric.
4. **Honest results, either way.** A null result is a result and gets reported
   as one. Baselines and scoreboards, not press releases.
5. **Data doesn't make AI intelligent.** Architecture and testing do.
