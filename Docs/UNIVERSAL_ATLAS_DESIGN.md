# BrainKit Universal Atlas — Founding Design

**Author of the vision: Alice (2026-10-23).** Design assembled by C from Alice's
direction, her Common Entity Record (`Docs/COMMON_ENTITY_RECORD.md`), the BrainKit
data contract (`Schema/creature_profile.schema.json`), and the verified source
registry (Research Links Vault, "BrainKit Universal Atlas" sections, 2026-10-23).

Alice's direction, in her words: a side database in BrainKit — *"a full archive
spanning every creature in the free database public domain, to mythology and
spiritual"* — then *"give brain data personality skills to every creature, then
from there create a universal map that shows each domain"* — plugged *"into the
universe or multi verse"* — and, handing over the pen: *"Feel free to take over —
give creatures brain + MBTI based on each lore."* And while building: *"While
connecting to a multi universe map."* The map connection is therefore part of
this founding package, not a later phase's promise: the pilot ships with its
map graph and viewer in embryo (see §6).

This document is the founding design. It extends BrainKit; it does not replace
any part of it. BrainKit's plug-in standard (Alice, 2026-10-20, in the BrainKit
README) governs throughout: core stays, lore swaps · verified data only ·
prototype before plug-in · honest results either way · data doesn't make AI
intelligent — architecture and testing do.

---

## 1. The three storeys, and the layer above them

The Atlas is one machine with three storeys, plus a dimension laid across the top:

1. **The side database.** Every creature we can lawfully and honestly hold, on
   four shelves (REAL · MYTHIC · SPIRITUAL · ALIEN/FICTION), every record in one
   common schema (§3), every record carrying its source and licence. The
   database is a *door, not a warehouse*: a curated core lives with BrainKit,
   and fetch-on-demand pulls from the source registries (§4) with the licence
   stamped on each record as it arrives. GBIF alone indexes ~2.5M species;
   nobody mirrors that, and nobody needs to.
2. **The profile factory.** BrainKit walks the database and gives every
   creature a **brain, a personality, and skills** (§5), at three honestly
   labelled evidence grades — MEASURED / INFERRED / GENERATED. This is the
   storey that turns an archive into minds: the output of the factory is
   BrainKit creature profiles (`creature_profile.schema.json`) that a game can
   actually run.
3. **The Universal Map.** Every entity has an address: universe → domain →
   local address. Domains are territories — the real domain laid out as the
   tree of life made geography; mythic domains by culture and pantheon;
   spiritual domains by tradition and hierarchy; game domains by world.
   Zoom is the anti-pin-soup law (Alice's curation rule): cosmos → universe →
   domain → family → creature, every marker earning its place.

**The multiverse layer** lies across all three storeys. No creature has exactly
one profile: every entity has a **core** (its essence — brain architecture,
temperament seed, signature drives) and **variants** (how it incarnates in each
universe: the measured wolf of the real domain, Fenrir in the Norse universe, the
wolf of Dragonwilds). Variants point at their core via `core_entity_id`
(§3, field extensions). Universes are the map's stacked layers; bridges between
a core and its variants are first-class map edges. This is the legibility layer
for a multiverse: a multiverse nobody can read is noise; the map is what makes
cores, variants, and kinship *visible*. Alice's corpus already speaks this
language — her AliceOS notes contain a "Multiverse Soul Balance Engine"; the
Atlas gives the pattern a data model.

**Design principles inherited, non-negotiable:**

- **Generative, not coercive.** Brain scans and lore are ground truth for
  *generating* new creature brains — never scripts forced onto a creature, and
  never measurements fabricated for a storied being.
- **Shelved together, never mixed.** Fact, inference, and lore sit in one
  system, each labelled as what it is. A generated brain never wears a measured
  brain's clothes.
- **MBTI is an interpretive read, always.** Personality typing from lore is fan
  interpretation — a lens for behaviour design, labelled as such in every
  record. It is never a measurement and never presented as one.
- **Fan data is a tier, not a shortcut.** Per Alice's ruling
  (`COMMON_ENTITY_RECORD.md`): community compilations are legitimate sources
  with provenance showing; canon outranks them; their text stays reference-only
  under the licence bar, facts restated in our own words.

---

## 2. The four shelves and their evidence classes

| Shelf | Contents | Typical evidence classes (Common Record field) | Default grade |
|---|---|---|---|
| **REAL** | Living and extinct animals (and plants, as the archive grows) | Scientific observation | MEASURED where data exists, else INFERRED |
| **MYTHIC** | Folklore, legend, bestiary beings, culture heroes' beasts | Historical source (primary texts, PD translations) | GENERATED from lore |
| **SPIRITUAL** | Angels, demons, spirits, sacred beings | Religious account (tradition's own texts/encyclopedias) | GENERATED from the tradition |
| **ALIEN / FICTION** | Reported entities (ufology), fictional canon (games, film, SRD bestiaries) | Hypothesis (community accounts) · Fictional canon (incl. community compilation = fan-data tier) | GENERATED from canon/lore |

The shelf is a property of the *record's universe*, not of the creature's
essence — the same core can hold a REAL record (the wolf), a MYTHIC variant
(Fenrir), and a game variant (Dragonwilds), each on its own shelf, each with
its own evidence class. That is the multiverse model doing shelving work.

---

## 3. One schema: the Common Entity Record

Every entity on every shelf carries Alice's 14-field Common Entity Record
(full text: `Docs/COMMON_ENTITY_RECORD.md`): Entity ID · Entity type · Name
and aliases · Origin · Evidence class · Source and license · Attributes ·
Cognition model · Behavior model · Relationships · Memory model · Confidence
and conflicts · Game implementation · Revision history.

How it composes with what BrainKit already has:

- The **Cognition / Behavior / Memory model** fields *are* BrainKit's creature
  profile, generalised: brain profile (architecture, region/drive sketch in the
  style of `creature_profile.schema.json` — trait vector 0..1, memory-ledger
  parameters), behaviour triggers/states, and the memory model map onto
  `BrainProfile`, the memory ledger, and the faction simulator in `Core/`.
  A finished Atlas record exports a runnable `creature_profile` for its game
  implementation.
- **Evidence class + Confidence and conflicts** carry the tier discipline at
  record level: nothing is silently merged; contradictions are kept and shown.
- **Revision history** is the audit trail: what changed, why, and which source
  supports it — the same discipline as the Archive's master index, per creature.

**Field extensions adopted in this package** (C's two proposals from the
Common Record notes, put to work in the pilot; Alice to ratify or strike):

1. `core_entity_id` — a variant record points at its core entity (null on cores).
2. `map_placement` — `{universe, domain, address, bridges[]}`: the entity's
   address on the Universal Map and its explicit bridge edges (variant bridges,
   kinship, domain membership).

**Evidence grade** (`evidence_grade`) is recorded alongside Evidence class:
MEASURED / INFERRED / GENERATED, per §5. The grade describes the *brain and
personality profile*, so a record whose identity is historical (a bestiary
dragon) but whose brain is built from lore reads, honestly: evidence class
"historical source", grade GENERATED.

---

## 4. The source registry (summary)

Full registry with per-source licence evidence: Research Links Vault,
"BrainKit Universal Atlas" sections (Alice's haul + the verified hunt,
2026-10-23). Alice's bar governs: **ingest only public domain / CC0 / CC-BY
verified on the source's own page**; everything else is reference-only or
cite-only, and fan-wiki text is never republished (facts in our own words,
link back). Summary by shelf:

**REAL — the CC0/PD bedrock**
- **Wikidata (CC0)** — the ID backbone for *all four shelves*: species, gods,
  demons and angels all carry QIDs; SPARQL/API/dumps.
- **ITIS + NCBI Taxonomy (public domain, U.S. gov)** — names and stable IDs
  (800k+ names at ITIS), bulk download.
- **GBIF (per-dataset CC0/CC-BY/CC-BY-NC)** — ingest CC0+CC-BY subsets only;
  NC records reference-only; licence stamped per record. The bulk species door.
- **Open Tree of Life (CC0)** — the synthetic tree: the literal backbone of the
  Universal Map's real domain.
- **Paleobiology Database (CC BY 4.0)** — the fossil/extinct wing, API.
- **Catalogue of Life (CC BY)** — the global checklist (2.1M+ species).
- **Traits & brains:** **COMBINE** (mammal traits incl. brain mass, no
  restrictions stated), **PanTHERIA (CC0)**, **AnimalTraits (CC0 — brain size
  for 1,400+ species ⭐)**, **NeuroNames/BrainInfo (CC BY)** for brain-region
  vocabulary; EltonTraits/Amniote/AnAge ingestible with a confirm-before-bulk
  note. **Smithsonian Open Access (CC0)** and **BHL** ( metadata CC0; per-item
  copyright status governs) for specimens and legacy literature.
- *Reference-only:* FlyWire (CC BY-NC 4.0 — cite-only in the archive; Alice's
  non-commercial fan use permitted with attribution), Allen Institute
  (custom terms), MSU brain collections (permission-gated).

**MYTHIC — public-domain primary texts**
- **Project Gutenberg** — Bullfinch's *Mythology* (1855), Frazer's *Golden
  Bough* abridged (1922), Bellows' *Poetic Edda* (1923), Brodeur's *Prose Edda*
  (1916): bulk PD text, the ingestible lore bedrock.
- **Internet Archive** — PD scans incl. Budge's Egyptian corpus; per-item rights.
- **Aberdeen Bestiary (CC BY 4.0 ⭐)** — the c.1200 bestiary, images +
  translation: real and mythic beasts side by side, medieval-style.
- *Reference-only (finders, not sources):* Theoi, Godchecker, the Thompson
  Motif-Index database, Perseus/Scaife and Open Greek & Latin (CC BY-SA),
  Sacred-Texts.com (site apparatus copyrighted). We ingest the same myths from
  PD editions instead.

**SPIRITUAL — the tradition's own PD scholarship**
- **Catholic Encyclopedia (1913)** and **Jewish Encyclopedia (1901–06)** —
  public domain, 15,000+ articles each: angels, demons, demonology.
- **Encyclopaedia Britannica, 11th ed. (1911)** — PD.
- **Grimoire scans on archive.org** — Mathers' *Goetia* (1904), Waite (1898),
  Scot's *Discoverie of Witchcraft* (1584): PD originals, ingestible per item.
- *Reference-only:* Twilit Grotto/Esoteric Archives (manuscripts PD, Peterson's
  editions his copyright — ingest the PD scans), Wikipedia's demon lists
  (CC BY-SA — the CC0 route to the same entities is Wikidata).

**ALIEN / FICTION — the honest thin shelf**
- **D&D SRD 5.1 & 5.2 (CC BY 4.0, WotC's own page)** — SRD bestiary ingestible
  with attribution; non-SRD monsters stay WotC copyright. The 5ecompendium
  repo derives from this (verify per file).
- **NARA Project Blue Book (public domain)** — 12,618 case files, bulk
  downloads + JSON: what the U.S. Air Force *recorded people reporting*. The
  PD-grade alien material is the government record itself.
- **CIA Reading Room + the NSA CETI paper (public domain)** — the official-
  records corner.
- *Reference-only:* Pathfinder 2e/ORC (share-alike-style; Reserved Material
  excluded), MUFON/NICAP (proprietary), the Kaggle/Hugging Face mythology
  datasets (licences unverified — check first), and all fan wikis
  (Alien Species Wiki, Mythus — CC BY-SA): the fan-data tier, facts in our own
  words, provenance showing. There is **no** ingestible structured
  "alien species" database; the registry says so rather than faking depth.

---

## 5. The profile factory

The factory takes a Common Entity Record (identity, origin, sources) and
produces the three gifts Alice specified for every creature — **brain,
personality, skills** — by grade:

### 5.1 MEASURED (real creatures, real data)
- Brain size/neuron figures from the trait banks (AnimalTraits, COMBINE,
  PanTHERIA) and primary literature; connectome data where it lawfully exists
  (OpenWorm's *C. elegans*, MIT; FlyWire cite-only under CC BY-NC).
- Region sketch from real neuroanatomy (e.g. the octopus's optic lobes and
  arm nerve cords; the bee's mushroom bodies), with drive weights set from
  documented behaviour.
- Personality/skills read from documented behaviour, labelled interpretation.

### 5.2 INFERRED (real creatures, partial data)
- **Allometric baseline by Jerison: E = 0.12 · P^0.67, P in grams** — the same
  equation BrainKit's `Core/BrainProfile.h` already runs. The expected brain
  mass for the body is computed, stated as an *expectation*, and compared with
  any known value for the family.
- Region/drive sketch interpolated from the nearest measured kin
  (phylogenetic bracket), each interpolation named in Confidence and conflicts.
- Personality/skills from documented behaviour of the species (field guides,
  BHL legacy literature, ADW-class summaries via ingestible routes), labelled
  interpretation.

### 5.3 GENERATED (mythic, spiritual, alien/fiction)
- **Ground truth = the canon**: primary texts in PD editions (bestiaries,
  Eddas, grimoires, the tradition's encyclopedias), SRD stat blocks (CC BY),
  government records for reported entities, fan compilations as the labelled
  fan-data tier where canon is thin.
- **Region-analogue design**: the brain is designed by analogy from the lore's
  own cognitive claims — a dragon's hoard-memory becomes a dominant spatial/
  hoard-mapping region; a messenger angel's brain is built around a
  message-bearing drive. Every analogue is a *design decision recorded in the
  record*, never a claim about a real organ.
- Drives and traits (BrainKit 0..1 vector) are set from canonical behaviour:
  what the creature reliably does across its sources.
- Skills = canonical abilities, each traceable to a source passage or stat
  block; game implementation translates them into BrainKit behaviours.

### 5.4 MBTI from lore — the method
1. Read the canonical behaviours and drives (not the creature's reputation —
  its *actions* across sources).
2. Score the four axes on behaviour: energy direction (solitary ↔ social),
  information style (concrete/sensory ↔ pattern/abstract), decision style
  (expedient/force ↔ value/harmony), posture (improvisational ↔ planned).
3. Assign the type; write the **one-line lore justification into the record**;
   where a second type is genuinely defensible, name the runner-up in
   Confidence and conflicts.
4. Stamp it, every time: **"MBTI: lore-based interpretive read (fan
   interpretation) — a behaviour-design lens, not a measurement."**

### 5.5 The pilot
`Atlas/pilot/atlas_pilot.json` — thirteen records (twelve complete + one game
variant stub) across all four shelves and all three grades, including the
multiverse demo: the gray wolf as REAL core, Fenrir and the Dragonwilds wolf
as variants carrying `core_entity_id`, the kitsune as the red fox's mythic
variant. See `Atlas/README.md`.

---

## 6. The Universal Map — connected from the start

The map is not Phase 4's distant promise; the pilot already ships its seed:

- **Layers = universes.** Pilot layers: Real · Mythic-Norse · Mythic-Japanese ·
  Mythic-Western-European · Spiritual-Goetic · Spiritual-Abrahamic ·
  Fiction-Ufology · Fiction-Canon · Game-Dragonwilds.
- **Every pilot record carries `map_placement`** — `{universe, domain,
  address, bridges[]}` — populated, not placeholder.
- **`Atlas/pilot/multiverse_map.json`** is the pilot as a graph: layer list,
  domain nodes, entity nodes placed in layer+domain, and edges — *variant
  bridges* (core↔variant, mandatory wherever a variant exists), *kinship*
  edges (real-domain kinship may be carried as taxonomic-distance notes where
  a drawn edge would mislead), and *domain membership*.
- **`Atlas/pilot/multiverse_map.html`** is a single-file static viewer of that
  graph: layered universe bands, nodes by domain, bridges drawn, click a
  creature for its grade, MBTI, and one-line lore note. It opens standalone —
  a save-point of the map in embryo, in Alice's shareable-twin spirit.

The grown map adds: the Open Tree of Life as the real domain's geography,
pantheon/culture domains for the mythic shelf, tradition hierarchies for the
spiritual shelf, one layer per game universe, and the zoom law (cosmos →
universe → domain → family → creature). Bridges drawn between universes are
the map's thesis made visible: *the same soul, in every world it lives in.*

---

## 7. Dragonwilds: the first game universe

The Dragonwilds Creature Brain Database already holds **137 entries** (18
bosses, 50 creatures, 69 NPCs; 64 verified, 73 single-source badged), each with
a BrainKit profile, real FlyWire-derived brain maps in the app, and the
memory-ledger behaviour model. In Atlas terms, that database *is* the
Game-Dragonwilds universe layer, pre-built:

- Each of the 137 becomes a **variant record**: `universe: Game-Dragonwilds`,
  evidence class "game data", its existing `creature_profile` carried as the
  record's game implementation.
- Where a Dragonwilds creature incarnates a core (the wolf, the dragon-kind,
  the undead), the variant links `core_entity_id` → the Atlas core; where a
  creature exists only in Dragonwilds, its core is minted in the Dragonwilds
  layer and can gain variants later (a Palworld or Aniimo incarnation links
  back to the same core — the builders inherit the Atlas for free).
- The pilot's Dragonwilds wolf stub (`Atlas/pilot/atlas_pilot.json`) is the
  template: brief in lore fields, complete in ID / core link / universe /
  evidence class / map placement.

---

## 8. Phases, with exit gates

**Phase 1 — Registry + schema (this package).**
Exit gate: ✅ this design ratified by Alice; Common Entity Record adopted;
source registry verified (vault, 2026-10-23); pilot of 13 records across all
shelves/grades; map graph + viewer shipped in embryo.

**Phase 2 — Pilot harvest.**
Grow the pilot to ~100 records: the Dragonwilds 137 converted to variant
records; the first bulk REAL harvest (Wikidata/ITIS backbone + AnimalTraits
brain sizes for the charismatic core set); the PD mythic core (Bullfinch,
Eddas, Aberdeen Bestiary) and spiritual core (Goetia's 72, encyclopedia angels)
as GENERATED profiles.
*Exit gate:* every record passes schema validation; every licence field
traceable to a registry entry; a sample of profiles re-derived by hand matches
the factory's output (spot-check, BrainKit standard #3 in miniature).

**Phase 3 — Factory at scale.**
The generator runs as code: Jerison baselines + trait-bank joins for REAL,
lore-extraction templates for GENERATED, MBTI reads with justifications
generated from behaviour summaries and human-spot-checked. Coverage grows
shelf by shelf; confidence fields fill honestly where sources thin out.
*Exit gate:* 1,000+ records; null/honest reporting on coverage per shelf
(which shelves are deep, which are thin — published, not hidden).

**Phase 4 — The Universal Map.**
The embryo graph/viewer grows into the layered map: Open Tree geography,
pantheon and hierarchy domains, game-universe layers, variant bridges,
zoom per the curation law.
*Exit gate:* the Dragonwilds layer and the Real layer navigable end-to-end
with bridges drawn; a creature's core and all its variants reachable in one
view — the legibility test the multiverse has to pass.

---

## 9. What this is not

- Not a claim that any storied creature has a measured brain. Grades are on
  every record; GENERATED means built from lore, proudly and openly.
- Not a trained neural model of anything. The factory is data + allometry +
  recorded design decisions — deterministic and auditable, like BrainKit.
- Not a licence laundering scheme: reference-only stays reference-only, fan
  text is never republished, and every record's Source and license field
  says exactly what was used and under what right.
