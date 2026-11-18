# BrainKit Universal Atlas

The Atlas is BrainKit's universe: a side database of creatures on four shelves —
**REAL · MYTHIC · SPIRITUAL · ALIEN/FICTION** — where every creature carries the
same Common Entity Record, receives a **brain, a personality, and skills** from
the profile factory, and takes an **address on the Universal Map**, in whichever
universe it lives. Design: `../Docs/UNIVERSAL_ATLAS_DESIGN.md`. Alice's schema:
`../Docs/COMMON_ENTITY_RECORD.md`. Run rules: `FACTORY_SPEC.md`. Provenance for
every run: `HARVEST_LEDGER.md`.

**Current state (2026-10-23): 909 records · 907 distinct entities · 17 universe
layers · grades: 29 MEASURED · 92 INFERRED · 788 GENERATED.**

## How to read a record

Every record is one JSON object with Alice's 14 fields, plus factory fields:

- `evidence_grade` — **MEASURED**: real data behind the brain facts ·
  **INFERRED**: from kin + documented behaviour, basis stated · **GENERATED**:
  built from lore by region-analogy (the design decisions are recorded in the
  record). The grade describes the profile, never the creature's worth.
- `personality.mbti` — **a lore-based interpretive read (fan interpretation)**:
  a behaviour-design lens, always labelled, always with a one-line justification
  from the creature's own lore/behaviour and usually a runner-up. It is never a
  measurement. Where a creature has no mind to type (a statue, an ooze, a
  process), the field says "n/a" and explains why — that honesty is part of
  the design.
- `cognition_model.brain_profile` — architecture, region/drive sketch in
  BrainKit's style (drives 0..1, matching `creature_profile.schema.json` traits),
  so a record can be exported into a runnable BrainKit profile.
- `confidence_and_conflicts` — the record's conscience: thin sources,
  disagreements between sources, withheld figures, disputed claims. Read it
  before citing anything.
- `map_placement` — `{universe, domain, address, bridges}`: where the entity
  lives on the Universal Map and its bridge edges. `core_entity_id` links a
  variant to its core (null on cores).

## The pilot (Phase 1)

`pilot/atlas_pilot.json` — 13 hand-built records that set the quality bar and
demonstrate the multiverse model. Roster:

| Entity | Shelf / Grade | MBTI | Note |
|---|---|---|---|
| Common octopus | REAL · MEASURED | INTP | ~500M neurons, two-thirds in the arms |
| Western honeybee | REAL · MEASURED | ESFJ | The worker read; the colony is the true entity (flagged) |
| Red fox | REAL · INFERRED | INTP | CORE of the kitsune |
| Common raven | REAL · INFERRED | ENTP | CORE of Huginn & Muninn |
| Western dragon | MYTHIC · GENERATED | INTJ | CORE of dragons in three other universes |
| Kitsune | MYTHIC · GENERATED | ENTP | Variant of the fox core |
| Fenrir | MYTHIC · GENERATED | ISTP | Variant of the wolf core — the pack, removed |
| Paimon | SPIRITUAL · GENERATED | ENFJ | The Goetia's teacher-king; West/northwest variance flagged |
| Gabriel | SPIRITUAL · GENERATED | INFJ | Messenger; canon fixed to the 1913 Catholic Encyclopedia |
| The Grey | FICTION-UFO · GENERATED | INTP | Hypothesis tier at maximum strictness — a *reported* entity |
| Xenomorph XX121 | FICTION · GENERATED | ISTP | Fan-data tier; canon conflicts preserved |
| Gray wolf | REAL · MEASURED | ENTJ | THE CORE of the first multiverse family |
| Wolf (Dragonwilds) | GAME · GENERATED | ENTJ (inherited) | Stub by design — superseded by the full record in the Dragonwilds corpus |

`pilot/multiverse_map.json` is the pilot as a graph; `pilot/multiverse_map.html`
is a single-file viewer of it (open it in any browser — layers as bands, gold
bridges core↔variant, click a creature for grade + MBTI + lore note).

## The corpus harvest (2026-10-23)

| Corpus | Records | File |
|---|---|---|
| Ars Goetia (complete) | 72 | `goetia/goetia.json` |
| Aberdeen Bestiary (complete surviving contents) | 127 | `bestiary/bestiary.json` |
| D&D SRD 5.1 monsters (complete index) | 334 | `srd/srd.json` |
| Mythic Flagships (8 cultures) | 84 | `mythic/mythic_flagships.json` |
| Spiritual Flagships (PD encyclopedias) | 26 | `spiritual/spiritual_flagships.json` |
| Real Flagships (tree of life) | 116 | `real/real_flagships.json` |
| Dragonwilds (complete database) | 137 | `dragonwilds/dragonwilds_atlas.json` |
| Pilot | 13 | `pilot/atlas_pilot.json` |

`multiverse_map.json` (this directory) is the master graph across all corpora:
17 universe layers, 907 entity nodes, 178 bridges drawn, 67 forward links
recorded for records not yet harvested. Per-run sources, licences, counts and
deferrals: `HARVEST_LEDGER.md`.

## Subcategory: Anime (added 2026-10-28)

`anime/` — the anime timelines as an Atlas subcategory: a universe layer of
stories. Contents: `README.md` (subcategory index), `chronological.md` and
`tech-level.md` (symlinks to the master timeline files in
`~/workspace/your_files/`, so there is only ever one copy),
`SHOWS_CHECKLIST.md` (119 shows after the 2026-10-29 additions of Bleach
and Digimon Adventure 1999; 119/119 ticked — anime queue COMPLETE
2026-10-29, 1,724 entries after the version-runs batch (+231 across 16 new lists), `CHARACTERS_PLAN.md` (schema +
method; lean list format decided 2026-10-29), and one subfolder per
completed series holding that series' `list.md`.
Rules carried over: [Dated]/[Analog]/[Undated] honesty tags, the
Collapse/Hidden/Setting Reset Map, continuity bridges (Fire Force →
Soul Eater), and the Common Entity Record for characters when the phase
runs (MBTI always labelled fan interpretation).

## Subcategory: Western animation (added 2026-10-29)

`western/` — sibling of the anime track, same lean format and rules, for
western animation plus Vocaloid (virtual singers) and one game
(FusionFall). One subfolder per show (`western/<show-slug>/list.md`),
`README.md` (track index + scope notes), `SHOWS_CHECKLIST.md` (164/164
ticked — western queue COMPLETE 2026-10-29, 1,942 entries + 9 link-backs;
`HANNA-BARBERA-CATALOG.md` 141/141 LISTED). No timeline
files; character lists only.

## Subcategory: Ancient Knowledge (added 2026-10-29)

`ancient-knowledge/` — a RESEARCH layer, not a story universe: Alice's
old-world thesis, the Old Stack system, and the breakdowns of pasted
and claimed material, indexed with links to the masters (one copy, no
drift). No character lists live here. Tiering rules: documented fact /
interpretation / hypothesis / speculation-fiction kept distinct;
fiction as analogy only, never evidence.

## Next steps (per the design's phases)

- **Phase 2 — Pilot harvest growth:** convert remaining game databases as
  universe layers; top up Real flagships (+4 species owed by the run spec);
  harvest the bestiary's lost-folio creatures from the Ashmole sister
  manuscript with provenance stated; extend Mythic flagships to uncovered
  cultures (Slavic, African, Oceanic, Indigenous American, Persian).
- **Phase 3 — Factory at scale:** the generator as code over the registry
  (GBIF/Wikidata doors), with per-shelf coverage published honestly.
- **Phase 4 — The Universal Map:** grow `multiverse_map.json` + the pilot
  viewer into the layered map; the exit test is legibility — a core and all
  its variants reachable in one view.
