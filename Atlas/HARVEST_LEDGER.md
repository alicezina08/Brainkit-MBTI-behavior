# Atlas Harvest Ledger — Corpus Runs of 2026-10-23

Every run, its source, its licence, what it produced, and what it deferred and
why. No silent truncation, no padded counts: where a run's spec overstated its
own roster, the shortfall is recorded against the spec, not the harvester.

**Grand total: 909 records = 907 distinct entities** (two entities exist at two
depths by design — see Pilot/Goetia and Pilot/Dragonwilds overlaps below).
Grades across the Atlas: **29 MEASURED · 92 INFERRED · 788 GENERATED.**
Master map graph (`Atlas/multiverse_map.json`): **17 universe layers, 907
entity nodes, 178 bridges drawn** (63 variant_of · 86 kinship · 26
storied_form_of · 3 core_of) and **67 forward links** recorded but not drawn
(they point at records not yet harvested — mostly bestiary storied-forms of
real species outside the flagship set).

| Corpus | File | Source | Licence | Records | Deferred / notes |
|---|---|---|---|---|---|
| Pilot | `pilot/atlas_pilot.json` + `pilot/multiverse_map.json` + `pilot/multiverse_map.html` | Hand-built founding set | Mixed per record (each record states its own) | 13 | The seed: 3 MEASURED, 2 INFERRED, 8 GENERATED; wolf core family (Fenrir, kitsune-via-fox, Dragonwilds wolf stub) demonstrates cores & variants |
| Goetia | `goetia/goetia.json` | Ars Goetia, Mathers translation 1904, fetched in full for verification | Public domain | **72 — COMPLETE finite set** | Nothing deferred. Paimon also exists as the richer pilot record (same entity_id, two depths by design). Edition variance (Paimon: West vs northwest) flagged in both records |
| Aberdeen Bestiary | `bestiary/bestiary.json` | Aberdeen Bestiary MS 24 via the University of Aberdeen's own Manuscript Index + translations; enumeration cross-checked against the manuscript contents | CC BY 4.0 (university digitisation policy) | **127 — COMPLETE surviving creature contents** (~123 distinct creatures; 127 records because four sub-treatments — e.g. Ram/Lamb/He-Goat — are separate manuscript entries) | **Deferred: the lost-folio creatures** — unicorn, antelope (antalops), griffin, lynx, camel, dromedary, ass, onager, manticore and others whose leaves are lost from MS 24 and are inferable only from the Ashmole sister manuscript. Not harvested; a future run may take them from that sister source with the provenance stated. Trees, Nature of Man, Stones excluded (not creatures). Asp's five named kinds and the worm body-catalogue kept inside their parent entries, as the folios present them |
| D&D SRD | `srd/srd.json` | D&D SRD 5.1 stat blocks via the dnd5eapi.co SRD index (334 monsters) | CC BY 4.0 (WotC) | **334 — the complete SRD index as served** | Product-identity creatures verified ABSENT from the entire index (searched: beholder, mind flayer, illithid, gith, displacer beast, yuan-ti, slaad — zero hits), so no exclusions were needed. Records are stat-derived lean records; 48+ INT≤2 creatures carry honest no-brain/tropism models and "MBTI not applicable" rather than invented personalities |
| Mythic Flagships | `mythic/mythic_flagships.json` | PD corpora: Bullfinch (1855), Eddas (Bellows 1923 / Brodeur 1916), Apollodorus/Hesiod/Homer in PD translation, Budge | Public domain | 84 (Greek 28 · Egyptian 13 · Norse 13 · Japanese 11 · Celtic 7 · Mesopotamian 4 · Chinese 4 · Hindu 4) | Flagship method by design (Alice's run spec): named beings, not a pretend-complete mythology. Fenrir and kitsune not duplicated (pilot records). Cultures not yet covered (Slavic, African, Oceanic, Indigenous American, Persian…) = Phase 2 breadth, not omissions in disguise |
| Spiritual Flagships | `spiritual/spiritual_flagships.json` | Catholic Encyclopedia (1913), Jewish Encyclopedia (1901–06), Britannica (1911) | Public domain | 26 | Run spec said "~38" but its own enumerated roster contained exactly 26 named beings; all 26 built, none invented to pad. Deferred: Cassiel-grade thin figures of the planetary lists (Cassiel included, kept deliberately lean); the Goetia's 72 are their own corpus, not duplicated here |
| Real Flagships | `real/real_flagships.json` | Established species literature; trait-bank posture (AnimalTraits CC0, COMBINE); Wikidata/ITIS anchors named (ID numbers given only where certain) | CC0 / public literature | 116 (Mammals 40 · Birds/Reptiles/Amphibians/Fish 36 · Invertebrates & other branches 40) — 26 MEASURED · 90 INFERRED | Run spec's "~120": batch B's enumerated roster contained 36 species, not 40 (spec's arithmetic, harvester refused to pad) — shortfall of 4 recorded against the spec; a 4-species top-up is a Phase 2 item. Brain-mass figures deliberately WITHHELD for 26+ species whose numbers circulate but weren't in the verified set. Errors caught in the run's own instructions and corrected in-record: the 2023 jellyfish-learning paper concerns *Tripedalia cystophora*, not *Chironex fleckeri* (record graded down); cleaner-wrasse mirror claim carried as DISPUTED |
| Dragonwilds | `dragonwilds/dragonwilds_atlas.json` | The project's own 137-entry catalog (`dragonwilds_catalog.json`, compiled 2026-10-16; 64 verified / 73 single_source) + its lore_role/behavior fields | Project data (fan work; game IP: Jagex) | **137 — COMPLETE** (18 bosses · 50 creatures · 69 NPCs) | 17 entries are statues/objects: function-only cognition, MBTI "n/a — object" — personhood was not fabricated for them. All body masses are fan estimates (the catalog's own flag) and every Jerison figure derived from them is labelled a fan-parameter design figure. 28 bridges / 18 core-linked records. The 'Wolf' full corpus record supersedes the pilot stub (same entity_id) |

## Method notes (all runs)

- Factory spec: `Atlas/FACTORY_SPEC.md`. Every record carries all 14 Common
  Entity Record fields + `evidence_grade`, `personality` (MBTI as a labelled
  interpretive read with one-line lore justification + runner-up), `skills`,
  `map_placement`, `core_entity_id`.
- MBTI honesty floors observed across runs: mindless creatures (SRD INT ≤ 2),
  statues/objects (Dragonwilds), and process-beings (Charybdis) received
  "not applicable" or formality-flagged reads instead of invented inner lives.
- Conflicts were preserved, never resolved silently: Berith's self-contradiction
  in the Goetia; the Plague King's HP disagreement; Aphrodite's double origin;
  Lucifer/Satan kept as separate records with the identification dispute in both.
- Batch files are preserved under each corpus's `batches/` directory; merged
  corpus files are the canonical reads.
