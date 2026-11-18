# Elysian Adaptive AI ↔ BrainKit — Architecture Mapping

*Companion to PROJECT ELYSIAN DOWNWARD §2 (Adaptive Learning AI), compiled 17 Oct 2026.
How the locked design maps onto the BrainKit reference implementation.*

## The one-sentence version

BrainKit's MemoryLedger is the per-creature memory substrate Elysian's adaptive
AI needs. Elysian's design adds a **director layer above it** (attention budget,
temperature, vendetta) and a **diegetic readout layer below it** (tells, trade
refusal, fog). Nothing in §2 requires inventing a new memory system.

## The three layers

```
┌─────────────────────────────────────────────────────────┐
│ DIRECTOR (proposed — does not exist in BrainKit yet)     │
│ AttentionBudget: fixed pool of focus; creatures/regions  │
│ bid with target temperature. Only winners learn.         │
│ Temperature: per-player/clan score from aggregate threat │
│ + visibility (success, loudness, group size).            │
└──────────────────────┬──────────────────────────────────┘
                       │ threat/kindness deltas
┌──────────────────────▼──────────────────────────────────┐
│ LEDGER (exists — BrainKit Core/MemoryLedger)             │
│ Per-creature associative memory: threat + kindness per  │
│ individual, 24h-half-life decay, individuals→categories  │
│ generalization (0.3), 64-individual cap.                │
└──────────────────────┬──────────────────────────────────┘
                       │ attitude() scores
┌──────────────────────▼──────────────────────────────────┐
│ READOUT (adapter work — the IWorldAdapter pattern)      │
│ Ledger scores drive world systems: refused trade, fog    │
│ symbols, radio static with old names, prioritized packs,│
│ weighted parameter rolls for world events.              │
└─────────────────────────────────────────────────────────┘
```

## Concept-by-concept mapping

| Elysian §2 concept | BrainKit mechanism | Mapping notes |
|---|---|---|
| Attention budget (finite focus; can't torment whole server) | **Proposed director-layer allocator** | Doesn't exist in BrainKit — ledgers are per-creature. The budget is a server-level pool: creatures bid attention with target temperature. This is the second bloat control (see below). |
| "Success and loudness raise temperature" | **Proposed `Temperature` score** | Per-player/clan: aggregate ledger threat across creatures + visibility metrics. Feeds the attention bidding. |
| Generational vendetta (clan heat across decades) | `CategoryLesson` with long half-life | The ledger already generalizes individuals→categories. A vendetta is a category entry keyed on bloodline/clan ID with half-life in *years* instead of hours. "Durable but not eternal" = very slow decay, not zero decay. |
| Atonement paths (rebuilding, protecting rivals…) | Kindness accumulation | The ledger already records kindness per individual *and* per category. Atonement is kindness events applied to the bloodline category, reducing net heat. No new machinery. |
| "What it studies" (playstyle, team comp, economy, voice, social graph, bloodline) | Delta-computation layer above `interact()` | These signals convert into `threatDelta`/`kindnessDelta` passed to `MemoryLedger::interact()`. Voice/prosody (opt-in) is one input among several — matches "voice is one signal among several." |
| Diegetic tells (refused trade, fog symbols, static, prioritized packs) | `attitude()` → world systems | Readouts of ledger state, not ledger mechanics. `attitude(id, now)` below threshold → traders refuse; heat feeds the fog system. Adapter-layer work. |
| Parameter roll (weighted, not RNG) | `FactionSim` seeded contests, weighted | The faction sim already runs seeded territory contests. Elysian's roll weights them by aggregate heat + server state instead of pure RNG. |
| "Patient predator, not a random grief engine" | Attention budget + temperature gating | Emerges from the design: pressure concentrates on high-temperature targets by rule, never uniform. |

## The bloat answer, stated once

Bloat is circumvented at **two levels**:

1. **Ledger level (per creature):** forget (24h half-life) → generalize
   (individuals collapse into categories) → cap (64 individuals, LRU eviction).
   A creature's memory physically cannot grow past this.
2. **Director level (per server):** the attention budget means only a subset of
   creatures are *learning* at any moment. A creature nobody looks at costs
   almost nothing — no ledger updates, no bidding. Server-wide memory stays
   bounded even with generational vendettas, because vendettas live as a
   handful of long-half-life *category* entries, not per-individual records.

## Tuning surface (Elysian-flavored knobs)

The fine-tuning interface a modder actually touches, in the design's language:

| Knob | BrainKit parameter | Elysian meaning |
|---|---|---|
| Attention pool size | *(director, proposed)* | How many creatures may actively learn at once |
| Temperature sensitivity | *(director, proposed)* | How fast success/loudness draws focus |
| Grudge half-life | `halfLifeHours` (per category) | Hours for individuals; decades for vendetta categories |
| Stereotyping speed | `generalizationRate` (0.3) | How fast individuals collapse into "goblins are hostile" |
| Social circle size | `maxIndividuals` (64) | How many individuals one creature can hold at once |
| Atonement weight | kindness delta scale | How much rebuilding offsets inherited heat |

## What's new code vs what exists

- **Exists:** the entire ledger (decay, generalization, cap, kindness/threat,
  category lessons), the faction sim, the JSON data contract, the UE adapter
  pattern.
- **Proposed:** the director layer (attention pool, temperature scoring,
  bidding), the delta-computation layer (study signals → deltas), the diegetic
  readout bindings. All three are bounded, well-specified work — none of them
  is a research problem.

## Boundary respected

This mapping is a creative/world-building module, consistent with the compiled
doc's boundary note: it stays out of the Universe Matrix empirical registry.
No real-world claims are made about any of these mechanisms.
