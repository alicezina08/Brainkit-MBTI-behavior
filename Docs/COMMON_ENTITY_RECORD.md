# The Common Entity Record — BrainKit Universal Atlas

**Author: Alice (2026-10-23).** Her words: "The common record every entity should have.
This is the key to making all four shelves interoperable."

Every entity on every shelf (real · mythic · spiritual · alien/fictional) carries this same
record. One schema across all shelves is what makes the Atlas a single system rather than
four separate databases.

| Field | Purpose |
|---|---|
| Entity ID | Permanent identifier across the archive |
| Entity type | Animal, plant, mythological, spiritual, alien, fictional, etc. |
| Name and aliases | Names in different languages, cultures, or game versions |
| Origin | Species, culture, tradition, universe, or source setting |
| Evidence class | Scientific observation, historical source, religious account, fictional canon, or hypothesis |
| Source and license | Provenance, reuse rights, attribution requirements |
| Attributes | Physical traits, abilities, sensory systems, and limitations |
| Cognition model | Learning, memory, attention, decision-making, or fictional equivalents |
| Behavior model | Triggers, needs, goals, responses, and state changes |
| Relationships | Parent species, allies, enemies, factions, habitats, and linked entities |
| Memory model | What the entity knows, remembers, forgets, or misinterprets |
| Confidence and conflicts | Contradictions, uncertainty, and alternative accounts |
| Game implementation | How the information becomes usable NPC or creature behavior |
| Revision history | What changed, why it changed, and which source supports it |

## Fan data — Alice's ruling (2026-10-23)

Alice: "for certain specific creatures fan data is the best resource." True for obscure
game creatures, niche fictional species, and most alien lore, where community wikis are
often the only organized record in existence. Atlas policy:

- Fan/community data is a legitimate source tier, entered with its provenance showing:
  Source = the fan source, Evidence class = fictional canon (community compilation),
  Confidence set honestly, and contradictions preserved in Confidence and conflicts.
- Where canon exists (game data, official sources, primary texts), canon outranks fan
  data; where fan data is the only source, the record says so rather than upgrading it.
- License posture unchanged: fan wikis are usually CC BY-SA, so their text stays
  reference-only under the bar — the Atlas records the facts and the pointer, in its own
  words, and links back.

## Notes (C, for the design doc — proposals, not part of Alice's spec above)

- The Cognition / Behavior / Memory model fields are BrainKit's existing creature-profile
  core (temperament, memory ledger, state changes) generalized to every shelf — this record
  extends `Schema/creature_profile.schema.json` rather than replacing it.
- "Evidence class" + "Confidence and conflicts" together carry Alice's tier discipline at
  record level (measured / inferred / generated; contradictions kept, never silently merged).
- Two candidate additions for the multiverse layer, pending Alice's approval:
  1. **Core / variant link** — `core_entity_id`: a variant record points at its core entity,
     so incarnations across universes stay one family (the Atlas's cores-and-variants model).
  2. **Map domain** — the entity's address on the Universal Map (universe → domain → family),
     derivable from Origin + Relationships but useful as an explicit field.
