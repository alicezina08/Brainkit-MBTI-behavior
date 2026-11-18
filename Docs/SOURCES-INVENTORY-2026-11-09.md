# SOURCES INVENTORY — Alice's Projects (consolidated)

**Compiled:** 2026-11-09 · **Compiler:** C (subagent) · **Status:** inventory only — no project data file was edited, nothing published or uploaded.

**Why this file exists:** Alice directed (2026-11-09) that every link data was collected from be listed, if not already listed. Her standing rule: licensed material must retain its license information; third-party factual references must retain attribution.

**How to read it**

- **Collected from** = data was actually taken from this source into a project file. **Surveyed / candidate** = the source was checked and filed as a possible source but nothing was (yet) collected from it — those entries are pointers, not collection claims, and are marked as such.
- **License** is given as verified on the source's own page where the inventory says "verified on source page"; where it says **UNVERIFIED** the licence could not be confirmed in this pass and the item is listed in §12.
- **Reference-only** = usable as a finding aid / citation only under Alice's bar (public domain / CC0 / CC-BY verified on the source page itself, else reference-only). Facts may be restated in original words; no text, image, or code is copied from a reference-only source.
- Where an existing attribution file already lists a source fully, this inventory **points at it** (file path + what it covers) instead of duplicating it, and only adds the links that were missing there.
- **Canonical links added in this pass** are marked **[link added 2026-11-09]**. Links that could not be found are listed as explicit **GAP**s in §12, not silently omitted.

**Existing attribution files this inventory consolidates (read these for full detail):**

| File | Covers |
|---|---|
| `Atlas/HARVEST_LEDGER.md` | Atlas harvest corpora: source, licence, record counts, deferrals |
| `Atlas/README.md` | Atlas structure, corpus table, anime/western/ancient-knowledge subcategories |
| `Docs/COMMON_ENTITY_RECORD.md` | The 14-field schema; `source_and_license` field; Alice's fan-data ruling |
| `Docs/copyright-audit-checklist.md` | Audit method (not a source list) |
| `~/workspace/your_files/research-links-vault.md` | Research Links Vault — all sections incl. the Atlas source registry and the 2026-10-23 verified-free-sources hunt |
| `~/workspace/research_notes/free-data-sources-directory.md` | 55-source verified-licensing survey, 2026-10-20 (survey only — see §10) |
| `~/workspace/aniimo-build/catalog_SOURCES.md` | Aniimo catalog sources (99 creatures) |
| `~/workspace/aniimo-build/world_SOURCES.md` | Aniimo Idyll world/lore sources |
| `~/workspace/aniimo-build/flywire_SOURCES.md` | FlyWire brain-region computation sources |
| `~/workspace/dragonwilds-build/catalog_SOURCES.md` (= `~/workspace/research_notes/dragonwilds-brain/catalog_SOURCES.md`, identical) | Dragonwilds catalog: 137 entries, 58 distinct URLs |
| `~/workspace/goals/runescape-storybook/files/era-3-*-sources.md` + era trackers | Storybook Era 3 source hunts; Era 1/2 trackers |
| `~/workspace/goals/runescape-storybook/files/jagex-fan-project-disclosure-2026-11-08.md` | Jagex disclosure (policy mapping, §8 credit) |

---

## 0. Counts reconciliation (Atlas audit cross-check)

| Corpus | Records | Distinct entities |
|---|---|---|
| Atlas harvest (ledger: pilot 13, Goetia 72, Aberdeen 127, SRD 334, Mythic 84, Spiritual 26, Real 116, Dragonwilds 137) | **909** | **907** (Paimon exists as pilot + Goetia record; Wolf as pilot stub + full Dragonwilds record — two entities at two depths by design) |
| Atlas animation — anime lists | 1,724 entries | 1,724 |
| Atlas animation — western lists | 1,942 entries (+ 9 link-backs) | 1,942 |
| **Total** | **4,575 records** | **4,573 distinct entities** |

Reconciles exactly with the 2026-11-08 audit figure of **4,573 distinct entities (3,666 animation + 907 harvest)**. Grades across the harvest: 29 MEASURED · 92 INFERRED · 788 GENERATED.

Per-record provenance check (this pass): across the 8 harvest JSON files, `source_and_license.sources` contains **470 distinct source strings, of which only 57 carry a URL and 413 are name-only** (book/edition/database named, no link). §1.2 supplies the canonical links for the name-only families that cover the most records; the remainder are GAPs in §12.

---

## 1. BrainKit Universal Atlas — harvest corpora (909 records)

Master file: `Atlas/HARVEST_LEDGER.md`. Every record carries all 14 Common Entity Record fields + `evidence_grade`, `personality` (MBTI as labelled fan interpretation), `skills`, `map_placement`, `core_entity_id`.

### 1.1 Corpus table (from the ledger, links added)

| Corpus | Records | Source (as harvested) | Link | What was collected | Licence |
|---|---|---|---|---|---|
| Pilot | 13 | Hand-built founding set (mixed per record) | — (no external link; see per-record fields) | Seed records incl. wolf core family, octopus, honeybee, raven, Paimon, Gabriel | Mixed per record |
| Goetia | 72 — complete finite set | Ars Goetia, Mathers translation 1904, fetched in full for verification | **[link added 2026-11-09]** full text via archive.org — https://archive.org/details/bookofceremonial0000crow (Mathers/Crowley 1904, *The Book of the Goetia of Solomon the King*; verify edition on the item page) and the Thelemagick Library reproduction named in-record | All 72 demons: rank, office, description, seal lore — profiles generated from the PD text | **Public domain** (1904) |
| Aberdeen Bestiary | 127 — complete surviving creature contents | Aberdeen Bestiary MS 24, via University of Aberdeen Manuscript Index + translations; enumeration cross-checked against manuscript contents | https://www.abdn.ac.uk/bestiary — **verified live 2026-11-09** (resolves to the University's bestiary site) | All surviving creature entries (incl. folio refs, e.g. f.68v–f.77r, in per-record source strings); trees / Nature of Man / Stones excluded | **CC BY 4.0** (University digitisation policy §5.2) for the digitised material; medieval text itself public domain |
| D&D SRD 5.1 | 334 — complete SRD index as served | D&D SRD 5.1 stat blocks via the dnd5eapi.co SRD index (334 monsters) | https://dnd5eapi.co/api/2014/monsters/aboleth (example record) — **verified live 2026-11-09** (returns live SRD JSON); official SRD text: https://www.dndbeyond.com/srd — **verified live 2026-11-09** (states SRD 5.1 and 5.2 under CC-BY-4.0) | Stat blocks only (no biography — records are stat-derived lean records; 48+ INT≤2 creatures carry honest no-brain/tropism models, "MBTI not applicable") | **CC BY 4.0** (Wizards of the Coast) — verified on D&D Beyond's own SRD page. **Note:** 16 SRD records reproduced SRD flavour text verbatim in `origin`; rewritten + verified 2026-11-09 per Alice's no-verbatim rule (separate fix work, not this inventory) |
| Mythic Flagships | 84 (Greek 28 · Egyptian 13 · Norse 13 · Japanese 11 · Celtic 7 · Mesopotamian 4 · Chinese 4 · Hindu 4) | PD corpora: Bullfinch (1855), Eddas (Bellows 1923 / Brodeur 1916), Apollodorus/Hesiod/Homer in PD translation, Budge | See §1.2 for per-text canonical links | Named beings only (flagship method by design); Fenrir/kitsune not duplicated (pilot records) | **Public domain** |
| Spiritual Flagships | 26 | Catholic Encyclopedia (1913), Jewish Encyclopedia (1901–06), Britannica (1911) | https://www.newadvent.org/cathen/ — **verified live 2026-11-09**; https://www.jewishencyclopedia.com — **link added 2026-11-09** (named in-record, no URL in the file; host verified as the encyclopedia's own site in the vault); Britannica 11th ed. via Wikisource / Gutenberg / archive.org (per-item — see GAP §12) | 26 named beings (run spec said "~38" but its own roster contained 26; none invented to pad) | **Public domain** (all three works pre-1923) |
| Real Flagships | 116 (Mammals 40 · Birds/Reptiles/Amphibians/Fish 36 · Invertebrates & other 40) — 26 MEASURED · 90 INFERRED | Established species literature; trait-bank posture (AnimalTraits CC0, COMBINE); Wikidata/ITIS anchors (ID numbers only where certain) | See §1.2 for per-database links | Species traits, brain-mass figures where verified (withheld for 26+ species whose numbers circulate but weren't in the verified set); 4-species top-up owed (spec arithmetic shortfall, Phase 2) | **CC0 / public literature** (per-database licences in §1.2) |
| Dragonwilds | 137 — complete (18 bosses · 50 creatures · 69 NPCs) | Project's own 137-entry catalog (`dragonwilds_catalog.json`, 2026-10-16; 64 verified / 73 single_source) + lore_role/behavior fields | `~/workspace/dragonwilds-build/catalog_SOURCES.md` — 58 distinct URLs, itemised in §6 | Full catalog carried into Atlas records; 17 statue/object entries are function-only cognition, MBTI "n/a — object"; all body masses are fan estimates, every Jerison figure labelled a fan-parameter design figure | Project fan data; game IP: Jagex. Fan database/guide listings are **reference-only** per the Atlas bar; facts paraphrased in original Atlas text, no fan text copied |

### 1.2 Canonical links for the name-only per-record source families (filled this pass)

These are the source strings that appear in `source_and_license.sources` with no URL. Links below are the canonical homes; licence as stated in the vault (verified on the source's own page in the 2026-10-23 hunt unless noted).

**Real-shelf databases**

| Source as cited in records | Canonical link | What was collected | Licence |
|---|---|---|---|
| Wikidata (CC0) — taxon identity (44 + 40 + 36 records cite it) | https://www.wikidata.org — **verified live 2026-11-09** | Taxon identity / QID anchors; also the CC0 entity layer for angels, demons, deities (spiritual shelf) | **CC0** (verified: Wikidata:Licensing) |
| ITIS — taxon identity (U.S. government, public domain) | https://www.itis.gov **[link added 2026-11-09]** | Scientific + common names, stable TSN IDs | **Public domain** (U.S. federal partnership; ITIS's own statement) |
| NCBI Taxonomy | https://www.ncbi.nlm.nih.gov/taxonomy **[link added 2026-11-09]** | Taxonomy backbone / IDs (named as anchor family in the registry) | **Public domain** (U.S. Government work, NIH/NCBI) |
| Catalogue of Life | https://www.catalogueoflife.org **[link added 2026-11-09]** | Global species checklist (named in registry; per-release licence file governs) | **CC BY 4.0** (modern COL releases; old Species 2000 terms superseded — check the licence file inside any given release) |
| Open Tree of Life | https://opentreeoflife.org **[link added 2026-11-09]** | Synthetic phylogeny / Open Tree Taxonomy — backbone for the Universal Map's real domain | **CC0 1.0** (taxonomy + synthetic tree; individual input phylogenies keep their own licences) |
| Paleobiology Database (PBDB) | https://paleobiodb.org **[link added 2026-11-09]** | Fossil taxa / occurrences — extinct-creature wing | **CC BY 4.0** |
| WoRMS | https://www.marinespecies.org **[link added 2026-11-09]** | Marine species register (Aphia IDs); text/taxonomic data only — images are CC BY-NC-SA, reference-only | **CC BY** (text); images excluded |
| AnimalTraits (brain find) | https://animaltraits.org **[link added 2026-11-09]** | Body mass, metabolic rate, brain size (>3,500 observations; brain size 1,400+ species) | **CC0 1.0** (Herries et al. 2022, *Scientific Data* 9:265; Zenodo copy also CC0) |
| COMBINE | Data via Figshare; paper: Soria et al. 2021, *Ecology* 102(6):e03344 **[link added 2026-11-09 — paper citation; no direct dataset URL in the registry — GAP, minor]** | Mammal traits (54 traits × 6,234 species, incl. brain mass) | **No restrictions stated by the authors** ("no copyright or proprietary restrictions; request citation") |
| PanTHERIA | Data via Figshare / ESA Ecological Archives E090-184; Jones et al. 2009, *Ecology* 90:2648 **[link added 2026-11-09 — paper/archive citation; no direct dataset URL — GAP, minor]** | Mammal life-history / ecology / geography (~5,400 species) | **CC0** (Figshare deposit) |
| EltonTraits 1.0 | ESA E095-178; Wilman et al. 2014, *Ecology* 95:2027 **[link added 2026-11-09 — archive citation; no direct URL — GAP, minor]** | Foraging/diet attributes, all birds and mammals | **No copyright restrictions** (per ESA data paper; worth a 2-minute confirm on the ESA page before bulk ingestion) |
| Amniote Database | ESA E096-269; Myhrvold et al. 2015, *Ecology* 96:3109 **[link added 2026-11-09 — archive citation; no direct URL — GAP, minor]** | Life-history traits, birds/mammals/reptiles | **No copyright restrictions** (same confirm-before-bulk note) |
| AnAge (HAGR) | https://genomics.senescence.info/species/ **[link added 2026-11-09]** | Ageing/longevity: 4,671 entries (Build 15), max lifespan, maturity | **CC BY 3.0** (per licence table; AnAge's own footer says "may be freely used under some conditions" — confirm on its disclaimer page before bulk ingestion) |
| NeuroNames / BrainInfo (brain find) | https://braininfo.org **[link added 2026-11-09]** | Brain-structure nomenclature (~2,500–3,000 concepts, 16,000+ synonyms) | **CC BY 3.0** (BrainInfo's own download page) |
| OpenWorm (brain find) | https://openworm.org **[link added 2026-11-09]** | *C. elegans* 302-neuron connectome, cell models, behaviour | **MIT** (permissive; flagged for Alice's explicit ruling — MIT is not literally PD/CC0/CC-BY) |
| Smithsonian Open Access | https://www.si.edu/open-access **[link added 2026-11-09]** | NMNH specimens/fossils (images, data, some 3D) | **CC0** (Open Access-designated assets only) |
| Biodiversity Heritage Library (BHL) | https://www.biodiversitylibrary.org **[link added 2026-11-09]** | Historic zoology/taxonomy literature (pre-1900 natural histories) | **Per-item** — metadata CC0; PD scans ingestible; in-copyright items CC BY-NC-SA, excluded (item's Copyright Status field governs) |
| FlyWire (see §5 for the full entry) | https://flywire.ai | Fly-brain template facts (1 record cites FlyWire-derived facts) | **CC BY-NC 4.0 — cite-only** (see §5 discrepancy note) |

**Mythic / spiritual texts (public domain)**

| Source as cited in records | Canonical link | What was collected | Licence |
|---|---|---|---|
| Bullfinch's *Mythology: The Age of Fable* (1855) | https://www.gutenberg.org/ebooks/3327 — **verified via search 2026-11-09** (eBook #3327, "Public domain in the USA") | Greek/Roman gods, heroes, creatures | **Public domain** |
| Apollodorus, *The Library*, Frazer translation (1921) | https://archive.org/stream/apollodorus00frazgoog/apollodorus00frazgoog_djvu.txt — **verified via search 2026-11-09** (1921 Loeb scan, PD). No Gutenberg edition of the Frazer translation was found. | Greek myth handbook material | **Public domain** (1921) |
| Hesiod, *Theogony*, Evelyn-White translation (1914) | https://www.gutenberg.org/ebooks/348 — **verified via search 2026-11-09** (*Hesiod, the Homeric Hymns, and Homerica*, eBook #348, incl. *Theogony* + *Works and Days*) | Greek creation / Titanomachy material | **Public domain** |
| Homer, *Iliad* and *Odyssey*, PD translations (Butler / Murray) | **GAP — exact ebook URLs not verified in this pass** (host: Project Gutenberg / archive.org; see §12) | Trojan / Odyssean material | **Public domain** (translations pre-1929) |
| Poetic Edda, Bellows translation (1923) | https://www.gutenberg.org/ebooks/73533 — **verified via search 2026-11-09** (eBook #73533) | Norse lays | **Public domain** |
| Prose Edda, Brodeur translation (1916) | https://archive.org/stream/proseedda00brodgoog/proseedda00brodgoog_djvu.txt — **verified via search 2026-11-09** (1916 scan, PD). Note: Gutenberg #17946 is the *Sephton* translation, a different translator — do not cite it for Brodeur. | Norse myth handbook (Gylfaginning, Skáldskaparmál) | **Public domain** |
| E. A. Wallis Budge, *Legends of the Gods* (1912) / *Book of the Dead* translations | **GAP — exact ebook URLs not verified in this pass** (host: Project Gutenberg / archive.org; see §12) | Egyptian gods, afterlife material | **Public domain** (pre-1929 works) |
| Herodotus, *Histories*, PD translation | **GAP — exact URL not verified** (host: Project Gutenberg; see §12) | Greek-reported Egyptian cult material | **Public domain** |
| *Enuma Elish* / Babylonian tradition, King, *The Seven Tablets of Creation* (1902) | **GAP — exact URL not verified** (host: archive.org; see §12) | Mesopotamian creation material | **Public domain** |
| Kojiki / Nihon Shoki tradition, PD translations | **GAP — exact URL not verified** (see §12) | Japanese myth material | **Public domain** (text); modern translations excluded |
| Hearn, *Legends of Japan* / *Kwaidan* tradition (PD) | **GAP — exact URL not verified** (host: Project Gutenberg; see §12) | Japanese folklore material | **Public domain** |
| Lady Gregory, *Gods and Fighting Men* (1904); Hyde / Curtin folklore collections | **GAP — exact URLs not verified** (see §12) | Celtic material | **Public domain** |
| Werner, *Myths and Legends of China* (1922); *Journey to the West* tradition | **GAP — exact URL not verified** (see §12) | Chinese myth material | **Public domain** |
| Rig Veda, Griffith translation (1889–92); PD Puranic retellings | **GAP — exact URL not verified** (host: sacred-texts.com / archive.org; see §12) | Hindu material | **Public domain** |
| Encyclopaedia Britannica, 11th ed. (1911) | Wikisource transcription / Gutenberg / archive.org scans (per-item) — **GAP: no single canonical URL verified** (see §12) | Demonology / angelology / mythology articles | **Public domain** (1911) |
| Jewish Encyclopedia (1901–06) | https://www.jewishencyclopedia.com **[link added 2026-11-09]** | Entries 'Angelology', 'Metatron', 'Lilith', 'Azazel', 'Samael' and related | **Public domain** (site's own homepage: "recently became part of the public domain") |
| Catholic Encyclopedia (1913) | https://www.newadvent.org/cathen/ — **verified live 2026-11-09** | Entries 'Angels', 'Devil', 'St. Michael', 'St. Raphael' and related | **Public domain** (1907–1912) |
| Aberdeen Bestiary contents enumeration via Wikipedia 'Aberdeen Bestiary' (reference only) | https://en.wikipedia.org/wiki/Aberdeen_Bestiary **[link added 2026-11-09]** (used only because the Aberdeen site returned a landing page to text fetch at harvest time; the manuscript contents themselves come from abdn.ac.uk) | Contents enumeration cross-check | **CC BY-SA** — reference-only; no text copied |

**Other name-only strings (not linkable to a single canonical page — recorded as-is, no GAP)**

- "Established species ethology / natural-history literature" / "Established ethology / cognition literature for this species (facts in own words)" — a *method* citation, not a source; facts restated in original words. No single link exists. Not a GAP in the link sense, but the underlying literature is not itemised per record — noted for the record.
- "Jerison allometric expectation computed for this record (formula in grade_note)" — a computation, not an external source.
- "Scriptural and deuterocanonical accounts as catalogued in the encyclopedias above" — covered by the encyclopedia links above.
- "Published comparative neuroanatomy compilations — brain-mass figure as stated in record" — generic; per-record figures are stated in-record with the compilation unnamed. **GAP (minor):** compilation not named per record.
- "Olkowicz et al. 2016 — avian pallial neuron counts" — paper citation, no DOI/URL in the record. **GAP (minor):** DOI not filed.

### 1.3 What was NOT collected (deferred — from the ledger, for completeness)

- Bestiary lost-folio creatures (unicorn, antelope, griffin, lynx, camel, dromedary, ass, onager, manticore…) — inferable only from the Ashmole sister manuscript; not harvested.
- Mythic cultures not yet covered (Slavic, African, Oceanic, Indigenous American, Persian…) — Phase 2 breadth.
- Real flagships: 4-species top-up owed; brain-mass figures withheld for 26+ species.
- Spiritual: Cassiel-grade thin figures kept deliberately lean; Goetia's 72 not duplicated here.

---

## 2. BrainKit Universal Atlas — animation (3,666 entries)

Files: `Atlas/anime/` (135 lists, 1,724 entries) and `Atlas/western/` (164 lists, 1,942 entries + 9 link-backs), incl. BrainKit profile records (`brainkit.json` per show, 3,666 records total per the 2026-10-30 profile phase; 96 core links).

**Source basis:** the shows themselves (canon — episodes/films as watched). Each lean list states: "Wikis and databases were used as finding aids only; nothing here is copied from a wiki, script, or subtitle" and "Name source: `../ROSTER_GOOGLE_DRAFT_2026-10-28.md` (Google AI draft — names verified against the show itself before entry; the draft is never evidence on its own)". MBTI is lore-based fan interpretation only. Headliner audit 2026-10-29: 101 entries checked, 96 passed as-is, 5 corrected (sources checked: series wikis, Wikipedia character lists, AniList, MyAnimeList character pages).

| Source / finding aid | Link | What was collected | Licence / status |
|---|---|---|---|
| The shows themselves (per-show canon) | — (no single link; per-show) | Character existence, role, skills, moveset, personality basis — all in original wording | Franchise IP belongs to its owners; non-commercial fan work, facts + pointers only |
| Google AI roster draft (2026-10-28) | `Atlas/anime/ROSTER_GOOGLE_DRAFT_2026-10-28.md` (local file; **UNVERIFIED SCAFFOLD, not records**) | Names only, verified show-by-show before entry | Third-party AI output — untrusted until verified; never evidence on its own |
| Series-specific Fandom wikis (e.g. One Piece Wiki) | Per-show; canonical host https://www.fandom.com **[link added 2026-11-09 — host only; per-show wiki URLs are NOT filed per list]** | Finding aid for the verification pass (translated databooks, timelines, power systems) | **CC BY-SA** — facts in own words + link back, never republished text |
| "Powers and abilities" wiki matrix (topstrongest.fandom.com) | https://topstrongest.fandom.com **[link added 2026-11-09 — from SOURCES_TO_CHECK.md]** | Cross-show power/skill comparisons (lead only) | **UNVERIFIED** — existence + licence unchecked; treat as a lead only |
| Anime News Network (ANN) Encyclopedia | https://www.animenewsnetwork.com/encyclopedia/ **[link added 2026-11-09 — canonical host; exact path as cited in SOURCES_TO_CHECK.md]** | Production canon / publication history, not in-universe lore | **UNVERIFIED** licence — background reading; not a citation |
| Anime Characters Database | https://animecharactersdatabase.com **[link added 2026-11-09]** | Trait/faction cross-checks | **UNVERIFIED** — coverage per show unchecked |
| MyAnimeList / AniList (character pages, forums) | https://myanimelist.net ; https://anilist.co **[links added 2026-11-09 — canonical hosts]** | Finding aids for the headliner audit; forum essays = background reading only, never a citation | **UNVERIFIED** licence/terms — no text copied |
| manami-project / anime-offline-database | https://github.com/manami-project/anime-offline-database **[link added 2026-11-09]** | Metadata scaffolding only (MAL/AniDB/AniList cross-references) | Licence on repo page — **UNVERIFIED in this pass** (check before any ingest) |
| Jikan API (MAL data) | https://jikan.moe **[link added 2026-11-09]** | Programmatic MAL metadata (characters, episodes) | Licence/terms **UNVERIFIED in this pass** |
| anime-and-manga / lists; WaifuAPI / Nekidev anime-api; Shad3Light / animescripts; Divyansh3105 / slimechronicles | GitHub repos named in `Atlas/anime/SOURCES_TO_CHECK.md` | Structural/episode mapping; format examples only (Slime/YGO not in the timelines) | **UNVERIFIED** — repo names as given by Google AI; existence not yet checked |
| HatsuSumi / anime-character-database; Munna-Scriptz / free-anime-apis; Bas1874 / Anime-Watch-Order-Api | Named in `SOURCES_TO_CHECK.md` | — (leads only) | **GAP: existence check still owed** — strike from the list if they do not resolve |

**GAP (animation):** no per-entry or per-show source URL is filed in any `list.md` or `brainkit.json` — the only per-show provenance is the roster-draft note + the "finding aids only" statement. Per-show wiki/database links were never filed. This is the largest single provenance gap in the Atlas; filling it means adding one "Sources checked" line per show list (canonical show wiki + AniList/MAL page). Not done here — that is a 299-list edit, for Alice's call.

---

## 3. BrainKit Universal Atlas — ancient-knowledge research layer (no character lists)

`Atlas/ancient-knowledge/` — a RESEARCH layer, not a story universe. Master index: `Atlas/ancient-knowledge/README.md`; corrected directory: `~/workspace/your_files/ancient-knowledge-research-directory-corrected.md` (v1.1, 2026-10-20). Full source links for this layer live in the **Research Links Vault** (§11) and the corrected directory — pointed at, not duplicated here. Notable: 15 entries in the pasted GPT directory were NOT FOUND at the claimed path and 7 owners were corrected; the corrected directory is the authoritative copy.

Also in this layer: the Voynich approach note (`Atlas/ancient-knowledge/voynich-manuscript-approach-note-2026-11-08.md`, also at `~/workspace/your_files/voynich-manuscript-approach-note-2026-11-08.md`) — anchors Llull's wheels, Hildegard's *Lingua Ignota*, Trithemius's *Steganographia*; Google-AI sample code filed as scaffold only.

---

## 4. Aniimo — Team Builder / BrainKit (99 creatures)

Master files: `~/workspace/aniimo-build/catalog_SOURCES.md`, `world_SOURCES.md`, `flywire_SOURCES.md` (all compiled 2026-10-14; copies also under `~/workspace/research_notes/aniimo-team-builder/`). Rule throughout: no game artwork, code, or verbatim descriptive text copied; flavour/skill/trait descriptions paraphrased in original wording; only factual data (names, numbers, stat values, element/role terms) recorded. Game assets © Pawprint Interactive Entertainment Pte. Ltd.

### 4.1 Catalog (per-creature data)

| Source | Link | What was collected | Licence / terms |
|---|---|---|---|
| PikaMMO Aniidex (PRIMARY) | https://pikammo.fr/Aniimo/en/aniidex — **live check not run in this pass; URL as filed 2026-10-14** | All 98 per-creature pages scraped (stats, trait, mobility, combat+innate skills, habitats, evolution chain/stage, weight, genders, flavour-text basis); post-launch official-index values (six-field stat schema). 98/99 creatures (all except Irisalis) | No explicit licence on scraped facts; descriptive prose paraphrased, not copied; no images downloaded. Licence **UNVERIFIED** |
| Official Aniimo Wiki | https://wiki.aniimo.com/en — **verified live 2026-11-09** (index now lists 130 entries incl. Hoptail, Irisalis, Dazmand — the catalog is a 2026-10-14 snapshot; roster has grown since) | Current creature list payload (`aniimo-wiki-list-en`, 86 entries, fetched 2026-10-14) to verify official numbering/roster. Detail pages returned 404 at the time, so per-creature details came from the Sept-2026 sync | Official game wiki; game IP: Pawprint. No licence statement filed — **UNVERIFIED** |
| wanghuan072/aniimo (GitHub fan site repo, aniimo.cc) | https://github.com/wanghuan072/aniimo | `src/data/game/aniimo.json` (1.9 MB, synced from official English wiki 2026-09-02, 94 entries): evolution trees, form records, habitats cross-check, pre-launch stats (conflict detection only); `roster-additions.json` (Squarrel, Squashel, Irisalis, Lunara, "Sparkelf"); `sources.json` (repo's own sourcing); `unreleased-aniimo.json` (33 unreleased entries — **not included**) | **No LICENSE file in the repo** (GitHub API confirms none) — treated as all-rights-reserved; only factual data compiled, no code/text/assets copied |
| aniimoguide.com/aniidex (verification only) | https://aniimoguide.com/aniidex | Roster-count cross-check (95 numbered + 124 forms claimed vs 92 + 6 special = 98 indexed supported); 5 combat roles; 16 habitats; stat leadership | Verification only; licence **UNVERIFIED** |
| aniidex.com (verification only) | https://aniidex.com/bosses/ ; https://aniidex.com/builds/ | Boss encounter list to verify creature names (20 bosses) | Verification only; licence **UNVERIFIED** |
| Dexerto Aniimo wiki (verification only) | https://www.dexerto.com/wikis/aniimo/best-aniimo/ | Confirmed Irisalis as a real legendary Aniimo | Verification only; press wiki, all-rights-reserved |
| aniimotools.dev/lore/ (verification only) | https://aniimotools.dev/lore/ | Game-codex lore verification (Astra/Idyll/Aeons/Veins/Prismana/Twining); no creature stats taken | Verification only; licence **UNVERIFIED** |

Known gaps carried in the catalog file: evolution unlock conditions/materials unpublished anywhere checked; skill power/cost/element unpublished in the current index; per-form stats exist only in the pre-launch schema (omitted); 24 creatures have no published habitat; 5 Squashel skills + 1 Shelly habitat label + Eko's Nova evolution name kept verbatim in Chinese, flagged; Irisalis partial record (no official stats/habitats/evolution published).

### 4.2 Idyll world data (`idyll_world.json`)

Every item carries a `source` URL + `source_kind` label (game codex / dex-published / community-reported). Sources:

| Source | Link | What was collected |
|---|---|---|
| aniimotools.dev/lore/ (game codex) | https://aniimotools.dev/lore/ | All 30 in-game World cards (paraphrased; proper names only quoted), murals, main-story chapter cards — Astra, Polaris Institute, nine Aeons, Vein network, Lumin Amber, Prismana, Twining, Ancient Idyll, Mechina, Ancient Sanctums; regions incl. Zephyr Coast, Breezy Plains, Bloomville, Russet Highlands, Sea of Flowers Mudflat |
| aniimoguide.com/aniidex (dex-published) | https://aniimoguide.com/aniidex | 16 named habitats + species counts; evolution stages Lumin→Gamma→Nova; element↔habitat tendencies; spawn conditions (habitat + weather + time) |
| PikaMMO per-creature pages (dex-published) | https://www.pikammo.fr/Aniimo/en/aniidex/wavwal ; https://www.pikammo.fr/Aniimo/en/aniidex/eko ; https://www.pikammo.fr/Aniimo/en/aniidex/eklue | Wavwal → Crescent Bay; Eko/Eklue → Forest of Falling Stars |
| aniimotools.dev/map/ (community-reported) | https://aniimotools.dev/map/ | Breezy Plains = starting region; Idyll = 15 regions + Island of Peace (region borders/levels omitted as WIP) |
| aniimotools.dev/quests/main-story/ (community-reported) | https://aniimotools.dev/quests/main-story/ | Argent Strait = prologue; Starfall Valley = Polaris Institute zone; Brightbough Plateau; first catches |
| aniimotools.dev home/news (community-reported) | https://aniimotools.dev/ | Rotating Prismana Form event spawns (Glynsera, Melloblum, Waleetle, Inferlupa); Emberpup surge; "17 regions" claim flagged as conflicting with the map page's 15+1 |
| Dexerto alpha locations (community-reported) | https://www.dexerto.com/wikis/aniimo/alpha-aniimo-locations/ | 17 Alpha boss → area mappings |
| GameRant post-game guide (community-reported) | https://gamerant.com/aniimo-post-game-guide-what-to-do-endgame-farming-activities/ | 14-region list cross-check; Everlasting Echoback Song quest; Flameruff→Inferlupa evolution (noted, not used as habitat mapping) |
| Sportskeeda event guide (community-reported) | https://www.sportskeeda.com/esports/who-s-aniimo-event-guide | Budclaw → Breezy Plains (photo-event clue) |
| Notebookcheck launch press (community-reported) | https://www.notebookcheck.net/Aniimo-sets-September-16-release-date-across-PC-and-consoles.1383909.0.html | Driftwise Meadow, Sandcastle Hill, Rosetower Wood as launch biomes; launch date 16 Sept 2026 |
| Press coverage of launch features / Egg Heist mode | (press, via the world file; no single URL filed — **GAP, minor**) | Lost Isles (Egg Heist 3-player PvEvP); Homeland (RV campsite, farming, decorating) |

Deliberately excluded (per the world file): region level bands; in-game coordinates; Whisperwake Isles / Apeiro as regions (speculative); pasted Grok/Claude lore claims (languages, species cultures, Celestuses loving music, starters from Prismana veins, fourth-wall awareness) — checked against the game codex, NOT found, listed under `unverified_claims`.

### 4.3 FlyWire brain data — see §5 (shared across Aniimo / Dragonwilds / Palworld)

---

## 5. FlyWire adult *Drosophila* connectome (shared brain template)

Used by: Aniimo brain-map build (`flywire_regions.json`), Dragonwilds brain build (same file), Palworld MBTI/BrainKit work (cited in the shareable HTML). **This is the one licence in the inventory with a live, documented discrepancy — record both sides:**

| Source | Link | What was collected | Licence |
|---|---|---|---|
| FlyWire Consortium, whole-brain connectome release v783 — connectivity data (Zenodo record) | https://doi.org/10.5281/zenodo.10676866 — **verified live 2026-11-09** (record: "FlyWire Whole-brain Connectome Connectivity Data", published 2 Jun 2024, v783.0, FlyWire Consortium, Princeton). Files used: `per_neuron_neuropil_count_post_783.feather` (233 MB), `per_neuron_neuropil_count_pre_783.feather` (17 MB), `proofread_connections_783.feather` (852 MB). Region synapse counts = column sums; region-pair flows = aggregated pairs; grand total 54,492,922 synapses (≈ published ~54.5M — consistency check passed); 78 regions, 150 flows | Per-neuron neuropil counts + proofread neuron-pair connectivity → region synapse counts and region-pair flows; 139,255 neurons / ~54.5M synapses / 78–79 neuropils | **CONFLICT — see note below** |
| FlyWire Codex (explorer) | https://codex.flywire.ai | Browsing / sanity reference; neuropil vocabulary (79 labels) | Same public-release terms as above |
| Dorkenwald et al. 2024, *Nature* 634:124–138 | https://doi.org/10.1038/s41586-024-07558-y (DOI as cited in flywire_SOURCES.md; **not re-fetched in this pass**) | Whole-brain release paper (139,255 neurons, ~54.5M synapses, 78–79 neuropils) — cross-check figures | Journal article; figures cited, not reproduced |
| Schlegel et al. 2024, *Nature* 634:139–152 | https://doi.org/10.1038/s41586-024-07686-5 (DOI as cited; **not re-fetched**) | Annotation / cell-typing release (8,400 cell types) | Journal article; cited only |
| Azevedo et al. 2024, *Nature* 631(8020):360–368 (FANC ventral nerve cord) | https://doi.org/10.1038/s41586-024-07389-x ; open full text https://pmc.ncbi.nlm.nih.gov/articles/PMC11348827/ | VNC figures only (published figures, not computed): ~45M synapses; 14,621 neuronal cell bodies; interneurons 12,468; ascending 1,668; motor 485; T1/T2/T3 + abdominal neuromeres | Journal article; figures cited |
| NIH summary | https://www.nih.gov/news-events/nih-research-matters/complete-wiring-map-adult-fruit-fly-brain | Cross-check summary | U.S. Government — public domain |
| flux-frontiers/connectome_kg (sanity reference only) | https://github.com/flux-frontiers/connectome_kg | Sanity reference only (79 neuropils, 5,786 directed pairs) — NOT a data source | Their docs credit underlying data as CC BY-NC-SA 4.0 for their renders |
| omkar-dhakane/flywire-gnn (sanity reference only) | https://github.com/omkar-dhakane/flywire-gnn | Sanity reference only (confirms 139,255 neurons, 2.7M thresholded pairs, 79 regions) | — |

**Licence discrepancy (important, do not "fix" by picking one side):**

- The Zenodo record's *metadata* states **CC-BY-4.0** (as quoted in `flywire_SOURCES.md` and the vault). When the Zenodo page was re-fetched 2026-11-09, **no licence field was visible in the fetched page text** — the CC-BY-4.0 claim could not be re-confirmed from the live page in this pass.
- FlyWire's **own terms page** states the opposite: https://flywire.ai/guidelines — **verified live 2026-11-09**: "FlyWire's public release data is made available under license **CC BY-NC 4.0**." (v783 = snapshot of Oct 2023.)
- **Conservative position (standing, per Alice's bar): FlyWire public-release data is CC BY-NC 4.0 — cite-only in the archive; non-commercial fan use permitted with attribution.** The flywire_SOURCES.md attribution line said "licensed CC-BY-4.0" — that wording was fixed to CC BY-NC 4.0 by the parallel legality sweep on 2026-11-09 (this inventory does not edit other files). The vault already records the BY-NC position (2026-10-22 re-check, unchanged).
- The `flywire_regions.json` computation itself (aggregation script, md5 `f48f972d262323a102aed49af1396b8a` matching the publisher's checksum) is documented in `flywire_SOURCES.md`; numbers are computed from the dataset files, not estimated.

---

## 6. Dragonwilds — Creature Brain Database (137 entries)

Master file: `~/workspace/dragonwilds-build/catalog_SOURCES.md` (identical copy at `~/workspace/research_notes/dragonwilds-brain/catalog_SOURCES.md`; companion `report.md` + `BUILD_SPEC.md`). Compiled 2026-10-16. 64 verified (2+ sources) / 73 single_source. Nothing invented: undocumented habitats/stats/drops recorded as "unknown"/null. Source priority: (1) MetaForge DB pp.1–6 (exhausted), (2) official wiki via search snippets (direct fetches 403 at the time), (3) gamemappers.com, (4) guides.

**58 distinct URLs, grouped by domain (URL mentions in brackets):**

| Domain / source | URLs (as filed) | What was collected | Licence / terms |
|---|---|---|---|
| MetaForge — RuneScape: Dragonwilds Database (PRIMARY, 133 mentions) | https://metaforge.app/runescape-dragonwilds/database/creatures-npcs/page/1 … /page/6 ; https://metaforge.app/runescape-dragonwilds/all-quests-in-runescape-dragonwilds ; https://metaforge.app/runescape-dragonwilds/icthlarins-little-helper-quest-guide — **page 1 verified live 2026-11-09** (returns live creature/NPC entries with HP, drops, locations) | Creature/NPC stats, HP, drops, regions, quest appearances — the backbone of all 137 entries; 73 entries rest on MetaForge alone | **UNVERIFIED — no licence/terms statement found in the catalog file.** Fan database; treated as reference-only (facts paraphrased, no text copied). Terms page not checked — GAP |
| Official Dragonwilds Wiki — dragonwilds.runescape.wiki (48 mentions) | https://dragonwilds.runescape.wiki/w/Dragon_Queen ; /w/Velgar ; /w/Imaru ; /w/Ashenfall ; /w/Dragonwilds ; /w/Damage_Type ; /w/Lesser_Dragon ; /w/Upcoming_updates ; /w/Update:This_Month_In_Ashenfall_-_October_2025 ; /w/Template:Infobox_NPC/doc — **wiki home verified live 2026-11-09** (community-maintained wiki; snapshot was stale ~0.9-era at audit time) | Lore, boss identities, region placements, update notes (via search snippets — direct fetches returned 403 during compilation) | Fan/community wiki (Jagex-run wiki platform, community content — typically CC BY-SA; **not verified on the page in this pass — GAP**). Facts paraphrased only |
| gamemappers.com (27 mentions) | https://gamemappers.com/all-enemy-locations-runescape-dragonwilds-guide/ | Enemy locations (all regions) | Guide site, all-rights-reserved; facts only. Licence **UNVERIFIED** |
| howtovideogame.com (11 mentions) | https://howtovideogame.com/runescape-dragonwilds-quest-list/ ; https://howtovideogame.com/runescape-dragonwilds-best-base-locations/ | Quest list / order / givers; base locations | Guide site; facts only. Licence **UNVERIFIED** |
| Steam — official Jagex news (6 mentions) | https://store.steampowered.com/news/app/1374490/view/711160422578783329 (+ other Steam news URLs in the file) | Official update/launch news (Tier B existence proof for quests/regions) | Official Jagex material; game IP: Jagex. Summarised, not copied |
| runescape-dragonwilds.wiki — fan boss guide (6 mentions) | https://runescape-dragonwilds.wiki/bosses/boss-guide/ | Boss HP / power levels / weaknesses / drops (incl. Fuzan, Imaru, Velgar) | Fan wiki; facts only. Licence **UNVERIFIED** |
| boostroom.com (6) | https://boostroom.com/blog/runescape-dragonwilds-10-scorned-wilderness-guide-progression-enemies-resources-gear-and-rewards | Scorned Wilderness progression/enemies/resources | Guide; facts only. **UNVERIFIED** |
| beebom.com (6) | https://beebom.com/runescape-dragonwilds-goblin-diplomacy-quest-guide/ | Goblin Diplomacy quest guide | Guide; facts only. **UNVERIFIED** |
| YouTube (5) | https://www.youtube.com/watch?v=5KFSO7QFOG0 ; ?v=HWgx28QcUvg ; ?v=M0YeVRN4YuY ; ?v=o_LiqH74Blo (+ 1 more in file) | Video guides (creature/boss coverage — per-video identification is in the catalog file, by creature) | Video content © its creators; facts only, no frames copied into the catalog |
| osrsmoneymaking.guide (5) | https://osrsmoneymaking.guide/news/how-to-tame-creatures-in-runescape-dragonwilds/ | Taming mechanics | Guide; facts only. **UNVERIFIED** |
| eurogamer.net (4) | https://www.eurogamer.net/all-runescape-dragonwilds-weapons | Weapons coverage | Press; facts only |
| capsulecomputers.com.au (4) | https://www.capsulecomputers.com.au/2026/04/runescape-dragonwilds-lowers-the-drawbridge-to-dowdun-reach/ | Dowdun Reach launch coverage | Press; facts only |
| bisecthosting.com (4) | https://www.bisecthosting.com/blog/runescape-dragonwilds-1-0-update-patch-notes-scorned-wilderness-kuldra-the-god-eater-combat-rework-new-items ; …/scorned-wilderness-raid-guide-kuldra-boss-fight-tips-puzzle-walkthrough ; …/umbral-sands-biome-guide-resources-mechanics-boss-fight-cave | 1.0 patch notes; Kuldra raid guide; Umbral Sands biome/boss guide | Guide/hosting blog; facts only. **UNVERIFIED** |
| fextralife.com (4) | https://fextralife.com/runescape-dragonwilds-dowdun-reach-update-adds-new-region-and-mithril-gear/ | Dowdun Reach update coverage | Fan wiki/guide; facts only. **UNVERIFIED** |
| gegebase.com (3) | https://gegebase.com/games/dragonwilds/quests | Quest index | Database; facts only. **UNVERIFIED** |
| gamever.io (3) | https://gamever.io/knowledge-base/garou-chits-the-umbral-sands-economy-what-to-actually-sell | Garou Chits / Umbral Sands economy | Guide; facts only. **UNVERIFIED** |
| gamerant.com (3) | https://gamerant.com/runescape-dragonwilds-start-enter-fellhollow-region/ ; https://gamerant.com/runescape-dragonwilds-scaling-difficulties-walkthrough/ | Fellhollow entry guide; scaling/difficulties walkthrough | Press; facts only |
| deltiasgaming.com (3) | https://deltiasgaming.com/runescape-dragonwilds-dragon-slayer-quest-walkthrough/ ; https://deltiasgaming.com/runescape-dragonwilds-goblin-diplomacy-quest-walkthrough/ | Dragon Slayer + Goblin Diplomacy walkthroughs | Guide; facts only. **UNVERIFIED** |
| christcenteredgamer.com (2) | https://www.christcenteredgamer.com/phpBB3/viewtopic.php?t=83402 | Jagex press-release reprint (blue dragonhide armour) | Press-release reprint; facts only |
| massivelyop.com (2) | https://massivelyop.com/2026/05/19/runescape-dragonwilds-revamps-runecrafting-today-teases-massive-umbral-sands-update-in-june/ ; https://massivelyop.com/2026/07/09/runescape-dragonwilds-teases-scorned-wilderness-and-its-september-15-boss-raid/ | Umbral Sands / Scorned Wilderness update coverage | Press; facts only |
| comicbook.com (1) | https://comicbook.com/gaming/news/runescape-dragonwilds-early-access-roadmap-update-expansions-1-0-release/ | Early-access roadmap coverage | Press; facts only |
| thegamer.com (1) | https://www.thegamer.com/runescape-dragonwilds-best-house-building-tips/ ; https://Www.Thegamer.com/runescape-dragonwilds-velgar-boss-battle-guide/ (sic — capitalised host as filed) | House-building tips; Velgar boss guide | Press; facts only |
| dotesports.com (1) | https://dotesports.com/general/news/runescape-dragonwilds-general-velgar-boss-fight-guide | Velgar boss guide | Press; facts only |
| gamedeveloper.com (1) | https://www.gamedeveloper.com/press-release/umbral-sands-unleashed-runescape-dragonwilds-receives-a-final-major-update-ahead-of-its-september-v1-0-launch | Jagex press release (Umbral Sands) | Official press release, reprinted; facts only |
| invisioncommunity.co.uk (1) | https://invisioncommunity.co.uk/runescape-dragonwilds-final-early-access-update-umbral-sands-goes-live/ | Same Jagex press-release reprint | As above |
| mmorpg.com (1) | https://www.mmorpg.com/news/runescape-dragonwilds-dowdun-reach-update-adds-new-region-a-foreboding-castle-mythril-weapons-and-more-2000137677 | Dowdun Reach update coverage | Press; facts only |
| pcgamer.com (1) | https://www.pcgamer.com/games/survival-crafting/runescape-dragonwilds-restless-ghosts-quest/ | Restless Ghosts quest coverage | Press; facts only |
| trueachievements.com (1) | https://www.trueachievements.com/a663662/dont-fear-the-reaper-achievement | Achievement data | Database; facts only. **UNVERIFIED** |
| noobfeed.com (1) | https://www.noobfeed.com/articles/runescape-dragonwilds-zogre-farm-shadow-sword-vestige | Zogre farm / Shadow Sword Vestige | Guide; facts only. **UNVERIFIED** |
| medium.com (1) | https://medium.com/life-is-a-game-magazine/runescape-dragonwilds-review-a-survival-crafting-rpg-that-brings-back-the-grind-2f06db84c756 | Review (context) | Blog; facts only |
| hacktheminotaur.com (1) | https://hacktheminotaur.com/runescape-dragonwilds/best-runescape-dragonwilds-melee-build/ | Melee build guide | Guide; facts only. **UNVERIFIED** |
| steamdb.info (1) | https://steamdb.info/patchnotes/21190836/ | Patch-note mirror | Data mirror; facts only |

Known gaps carried in the catalog: Black Dragon boss habitat unknown; hatchling habitats inferred from parent dragons (flagged); Kuldra's Heart identity unconfirmed; Plague King HP discrepancy (MetaForge 150 vs boss guide 300/488 at power levels 2/3); Swamp Frog has no documented HP/drops; Lesser Dragon has no MetaForge entry; several MetaForge-only NPCs/birds have no documented region; Doric/Vannaka/Zanik/Wise Old Man habitat conflicts flagged, not resolved. Excluded after verification: Kalphite Queen (OSRS/RS3 content, not Dragonwilds); "Reforged Zi" (unverifiable); SEO-spam fabrications ("Chromantic Wyrm", "Scale and Shadow" questline, OSRS prayer-switching mechanics).

**Note on the two catalog copies:** `dragonwilds-build/catalog_SOURCES.md` and `research_notes/dragonwilds-brain/catalog_SOURCES.md` contain the identical 58 distinct URLs (verified by diff this pass — no differences). One copy, two paths; the build copy is treated as canonical.

---

## 7. RuneScape Storybook saga (249 quests / 488 beats)

The saga is a **fan retelling** (original prose + narration), not a data collection: quest facts (names, givers, rewards, XP figures) were verified against the sources below and retold in saga voice. Legal basis for the retelling itself: **Jagex Fan Content Policy v1.4 (29 Sep 2026)** — https://legal.jagex.com/docs/policies/fan-content-policy.md — **verified live 2026-11-09** (linked from the Jagex Legal Portal, https://legal.jagex.com/). The policy grants fans a licence for non-commercial derivative works; the storybook is free, no ads/merch, no Jagex logo, never presented as official; exact §8 credit wording is in the app footer + About (v1.9+). Disclosure sent 2026-11-08 to IP@Jagex.com (cover letter + disclosure PDF + Wise Old Man intro video; follow-up with MP4 Parts 1–2). See `goals/runescape-storybook/files/jagex-fan-project-disclosure-2026-11-08.md`. Full policy mapping is in MEMORY.md; not duplicated here.

### 7.1 Era 1 (OSRS, 193 quests / 401 beats) + Era 2 (RS3/mainline, 18 quests / 36 beats)

Trackers: `era-1-compilation-tracker.md`, `era-2-compilation-tracker.md`. **No dedicated sources file exists for Eras 1–2** — provenance is per-beat "True bits" (traced to quest data) plus tracker notes. Sources named in the trackers:

| Source | Link | What was collected / used for | Licence |
|---|---|---|---|
| The RuneScape Wiki (RS3 wiki) | https://runescape.wiki/ — **verified live 2026-11-09** (resolves; crawl copy is old, 2024 — the live wiki is current) | Quest facts, XP/reward figures; Era 2 beats 418–437 re-verified against runescape.wiki itself 2026-10-23 (all reward figures confirmed, incl. icon-only XP skill mappings via Quests/Experience rewards tables) | Community wiki — **CC BY-SA (Jagex wiki platform default; not re-verified on the page in this pass — GAP, minor)**. Facts only, retold in saga voice; no wiki text copied (verbatim passages found in the 2026-11-08 audit were rewritten in v1.10) |
| Old School RuneScape Wiki | https://oldschool.runescape.wiki/ **[link added 2026-11-09 — canonical host; per-quest page URLs not filed in the trackers]** | Era 1 quest facts, transcripts (e.g. "official wiki transcript" cited for A Porcine of Interest) | Community wiki — **CC BY-SA (platform default; not re-verified — GAP, minor)**. Facts only |
| RuneLite Quest Helper repo | https://github.com/Zoinkwiz/quest-helper — **verified via search 2026-11-09** (Zoinkwiz/quest-helper, "Helps with Quests") | Quest step/requirement verification where no reliable OSRS web results existed (e.g. Getting Ahead, In Search of Knowledge, Crab Quest; Era-status calls via QuestHelperQuest enum absence for 185 OSRS quests) | Open-source plugin repo; licence **BSD 2-Clause, © 2020 Zoinkwiz** — verified this pass from the LICENSE file in the local clone at `~/workspace/osrs-repos/quest-helper/LICENSE` (a full local copy of the repo also sits in the workspace; it was the source consulted for quest-step verification). Used as a factual cross-check only; no code copied |
| In-game dialogue / quest transcripts (via the wikis above) | — | Dialogue facts retold in saga voice | Game IP: Jagex; covered by the Fan Content Policy basis above |

**GAP (Eras 1–2):** no per-quest source list was ever filed — the trackers record quest-by-quest *verification notes* ("verified", "corrected to verified values", "two sources conflicted") without URLs. Per-quest URLs could be reconstructed mechanically (one wiki page per quest) but were not filed; this inventory does not invent that reconstruction — it is listed as an open gap.

### 7.2 Era 3 (Dragonwilds, 38 quests / 51 beats: 443–488)

Source hunts: `era-3-dowdun-sources.md`, `era-3-fellhollow-sources.md`, `era-3-regicide-sources.md`, `era-3-umbral-sources.md`, `era-3-backfill-sources.md`; scope audit: `era-3-dragonwilds-scope-audit.md`; tracker: `era-3-compilation-tracker.md`. **These files cite sources by name, almost never by URL — the links below were filled in this pass from the canonical homes named in the files.**

Evidence tiers used throughout: A = official wiki quest page · B = official Jagex material · C = guide/list. The official Dragonwilds wiki's own quest pages for Fellhollow/Dowdun/Umbral/Regicide were **not located by search** during the hunts — Era 3 rests on Tier B + Tier C, disclosed in-beat.

| Source (as named in the hunt files) | Canonical link **[added 2026-11-09]** | What it established | Licence |
|---|---|---|---|
| Jagex press releases (Fellhollow 15 Dec 2025; Dowdun 19 Mar 2026; Umbral 23 Jun 2026; Kuldra's Saga / 1.0) via gamespress.com | https://www.gamespress.com (press-release distribution; Jagex releases filed there) — **host link; per-release URLs not filed in the hunt files — GAP, minor** | Region launches, boss/quest existence, dates (Fellhollow; Dowdun Reach 31 Mar 2026; Umbral Sands; Scorned Wilderness raid 15 Sept 2026) | Official Jagex material; summarised/quoted briefly in hunt notes (short attributed quotes — see audit note re: verbatim text; the saga beats themselves are retold) |
| Jagex 2026 roadmap (community summit, 29 Jan 2026; via gamespress + Escapist) | https://www.escapistmagazine.com (coverage) + gamespress (above) — **per-article URLs not filed — GAP, minor** | Dowdun "Madness of Zamorak" framing; region contents | Official-adjacent; summarised |
| Official update notes — "Eye on Ashenfall" (dragonwilds.runescape.com, via SteamDB mirror) | https://store.steampowered.com/news/app/1374490/ (Jagex Steam news hub for Dragonwilds) **[added 2026-11-09]**; https://steamdb.info/patchnotes/21190836/ (patch-note mirror, also in §6) | 0.11 "Enter Dowdun Reach" (four quests: Black Knight's Fortress, Wanted!, Biohazard, What's Theirs Is Mine); 0.11.1 / 0.12.1 quest-existence confirmations; 1.0 release | Official Jagex material |
| EA roadmap (devtrackers mirror of the official letter) | **GAP — devtrackers URL not filed in the hunt files and not verified in this pass** | Expansion 2 (Dowdun Reach) description | Official-adjacent; summarised |
| metaforge.app — all-quests list + walkthroughs | https://metaforge.app/runescape-dragonwilds/all-quests-in-runescape-dragonwilds (see §6 for the full MetaForge entry) | Dowdun/Fellhollow/Umbral quest rosters, givers, triggers; Black Knight's Fortress walkthrough (Soloboom, Apr 2026) | Reference-only fan DB; licence **UNVERIFIED** (see §6) |
| howtovideogame.com — quest list (updated 2026-10-23) | https://howtovideogame.com/runescape-dragonwilds-quest-list/ (see §6) | Main-story order, quest givers, region-grouped side quests | Guide; facts only. **UNVERIFIED** |
| runescape-dragonwilds.wiki — quest index + skill guide | https://runescape-dragonwilds.wiki/ (boss guide at /bosses/boss-guide/; quest index path as cited in hunt files — **exact quest-index URL not verified — GAP, minor**) | Quest-index corroboration (e.g. Growing Pains trigger; Farming arrival with 0.10) | Fan wiki; facts only. **UNVERIFIED** |
| gegebase.com — quests | https://gegebase.com/games/dragonwilds/quests (see §6) | Quest giver corroboration (e.g. Growing Pains) | Database; facts only. **UNVERIFIED** |
| ru24 fishing guide (named in backfill file, no URL) | **GAP — full source name/URL not filed in era-3-backfill-sources.md** (only "ru24" cited, for Shrimp Catcher rewards: 1 Tome of Fishing, 3 Shrimp Bait, 3 Feather Bait) | Shrimp Catcher rewards | **UNVERIFIED** |
| Official Dragonwilds wiki quest pages | https://dragonwilds.runescape.wiki/ — **verified live 2026-11-09** (home resolves) | **NOT LOCATED by search during the hunts** — recorded as a gap in the hunt files themselves, not a source used | — |

### 7.3 Storybook voice / audio (for completeness — not a data source)

Narration voice "Hospitable Lamp" (avocado_v2:qvd_04216) — voice samples are a casting choice, not collected data. No source link filed for the voice provider in the storybook files; the narration audio is generated, not collected. Not a sources gap in the data sense; noted so it isn't mistaken for one.

---

## 8. Palworld — Team Builder

**No dedicated SOURCES file exists for the Palworld builder.** The sources below were recovered this pass from links embedded in the shareable app HTML (`~/workspace/your_files/palworld-team-builder-shareable/palworld-team-builder-shareable.html`) and the egg-layer notes (`~/workspace/research_notes/palworld-egg-layer-20261013-0615/`). The builder's per-pal data provenance is therefore **partially reconstructed, not filed at build time — GAP** (see §12).

| Source | Link | What was collected / used for | Licence |
|---|---|---|---|
| PalDB (Palworld Database Wiki) | https://paldb.cc/en/Eggs — **verified live 2026-11-09** (returns live egg/location table, 754 wild eggs) | Egg data: wild-egg locations, pal↔egg mapping, weights (egg layer) | **UNVERIFIED** — no licence statement checked on the page in this pass |
| Palworld Wiki (Fandom) | https://palworld.fandom.com/wiki/Breeding ; https://palworld.fandom.com/wiki/Egg_Incubator **[links as embedded in the HTML]** | Breeding mechanics; Egg Incubator | **CC BY-SA** (Fandom platform default — not re-verified on the page in this pass) — facts only, reference-only |
| Nifrendil / pal-atlas (GitHub) | https://github.com/Nifrendil/pal-atlas | Pal data / atlas reference (as linked in the HTML) | Licence on repo page — **UNVERIFIED in this pass** |
| palcalc-tools / palworld-1.0-calculator (GitHub) | https://github.com/palcalc-tools/palworld-1.0-calculator | Breeding/calculator reference | Licence **UNVERIFIED in this pass** |
| palworldlol / palworld-coord (GitHub) | https://github.com/palworldlol/palworld-coord | Coordinate data reference | Licence **UNVERIFIED in this pass** |
| parmati94 / palworld-lens (GitHub) | https://github.com/parmati94/palworld-lens | Pal data reference | Licence **UNVERIFIED in this pass** |
| tylercamp / palcalc (GitHub) | https://github.com/tylercamp/palcalc/blob/main/PalCalc.Model/PalExtensions.cs | Breeding logic reference (PalExtensions.cs) | Licence **UNVERIFIED in this pass** |
| ianscottknight / Predicting-Myers-Briggs-Type-Indicator-with-Recurrent-Neural-Networks (GitHub) | https://github.com/ianscottknight/Predicting-Myers-Briggs-Type-Indicator-with-Recurrent-Neural-Networks | MBTI RNN model — the inspiration for lore-based MBTI on pal cards (model concept, not copied code — see note) | Licence **UNVERIFIED in this pass** |
| virtualflybrain (GitHub org) | https://github.com/virtualflybrain | Fly-brain reference (BrainKit lineage) | Licence **UNVERIFIED in this pass** |
| Dorkenwald et al. 2024, *Nature* | https://www.nature.com/articles/s41586-024-07558-y | Fly connectome paper (see §5) | Journal article; cited only |

Game IP: Palworld © Pocketpair. The builder is a free fan companion; pal data is factual game data (names, stats, breeding combos) restated in the app's own presentation.

**GAP (Palworld):** no build-time sources file; the per-pal fields in the app do not carry source URLs; the main pal-data source for the roster/stats (beyond the egg layer's PalDB) is not identified in any file — it may be the in-game Paldeck itself (primary observation) or one of the GitHub repos above, but no file says which. Needs a one-line-per-source note from whoever built the roster, or a fresh audit of the app's data against PalDB.

---

## 9. Once Human — Atlas Class Builder + Tank House Blueprint

| Source | Link | What was collected / used for | Licence |
|---|---|---|---|
| Charie Kan — "ONCE HUMAN - I Built A Tank In Winter Server! Tour & Speed Build!" (YouTube, 30 Apr 2025) | https://youtu.be/ThYVShxPbig — **as credited in `~/workspace/once-human-blueprint/blueprint-template.html`** (not re-fetched in this pass) | Tank house reconstruction: piece-by-piece blueprint from the tour + speed build; 5 video frames used as stills in the shipped blueprint (flagged in the 2026-11-08 audit as images-only issue — see note below); her house is on SEA server W_Winter-X0051; tour 0:00, speed build 2:24 | Video © Charie Kan. The blueprint is a **reconstruction with credit, not her official published blueprint**; stills are frames from her video used as visual reference with credit. **Licence/permission UNVERIFIED** — no permission on file; the audit flags the 5 frames + full video copy in the workspace as the fix item (separate work) |
| Once Human game itself (NetEase / Starry Studio) | — (game client) | Class-builder data (builds, incl. Alice's frost/cursed builds) — provenance not filed | Game IP: NetEase/Starry Studio; fan work |

**GAP (Once Human):** the Atlas Class Builder (`~/workspace/goals/once-human-atlas-class-builder/`, `~/workspace/ts-spaces/once-human-atlas-class-builder`) has **no sources file at all** — no file identifies where its class/build data came from (in-game observation? Once Human wiki? guides?). The Tank blueprint's single source (Charie Kan) is properly credited in-template; the class builder's sources are unidentified. Also note: the blueprint HTML says "Share freely — the file is self-contained and works offline", which is a distribution statement, not a licence for the embedded video frames.

---

## 10. Free-data sources directory (SURVEY — not collection)

File: `~/workspace/research_notes/free-data-sources-directory.md` — "Verified Licensing Survey", surveyed 2026-10-20. **Nothing was downloaded and no accounts were created; this is a survey, not a collection log.** It is included here because Alice's 2026-10-09 direction covers "each link data was collected from" — these 55 sources are links data was *checked against*, and the file is the place where their licences were verified. Do not cite this section as proof data came from any listed source; cite the per-project sections above for actual collection.

Verdict counts (55 sources): **INGEST-OK 10** (Smithsonian Open Access CC0 · Met Open Access CC0 · Getty Open Content + record text · USGS-authored content · Dryad CC0 · OpenNeuro · MICrONS Explorer scoped CC BY 4.0 · Pleiades CC-BY · OpenAlex CC0 · USGS Landsat) · **MIXED-FILTER 36** (Internet Archive · Project Gutenberg · BHL · HathiTrust · Library of Congress · Wikimedia Commons · DPLA · Europeana · NYPL · Rijksmuseum · Data.gov · NASA Open Data · NOAA general/Fisheries · NOAA ATN · ScienceBase · OSTI · PMC OA Subset · NCBI/NLM · BICCN/BICAN · NeMO · NARA · GBIF · iDigBio · MorphoSource · EOL · WoRMS · Xeno-canto · Zenodo · DANDI · Brain/MINDS · EBRAINS · Open Context · tDAR · Archaeology Data Service · JSTOR open portion · NOAA ocean/coastal) · **CITE-ONLY 6** (NASA Image & Video Library · Brain Image Library CC BY-SA · Animal Diversity Web · Allen Institute · FlyWire Codex CC BY-NC · Persée) · **UNVERIFIED 3** (Catalogue of Life checklist database · Theoi · Attalus) · RESTRICTED 0 standalone (restricted tiers inside NeMO, EBRAINS, MorphoSource, tDAR, BICCN human controlled data).

Headline finding (from the survey): only USGS-authored content is blanket-clean at agency level; every other portal mixes at least one non-PD tier — the filter column is where the honesty lives. Full per-source entries (URL + terms as stated + verdict) are in the file itself; this inventory does not duplicate its 55 entries.

---

## 11. Research Links Vault + Compendium / thesis material (pointers)

Master file: `~/workspace/your_files/research-links-vault.md` (created 2026-10-17; newest entries at the top of each section). The vault mixes (a) sources data was collected from, (b) sources checked and filed for later, and (c) audited reel/paste breakdowns. Only (a) belongs in a sources inventory; (b) and (c) are pointed at, not re-listed. Items already covered in §§1–10 above are not repeated here.

**Collected / used from the vault (beyond §§1–10):**

| Vault section / entry | Link | What was collected / used for | Licence |
|---|---|---|---|
| Lee & Thornton 2021 (animal cognition & urban adaptation review) | https://doi.org/10.3389/fevo.2021.633947 (DOI verified resolving to Frontiers, per vault) | Compendium claim-support lead; relevance to Compendium claims not yet mapped (GPT-provided lead) | Open access (Frontiers) — licence **UNVERIFIED in this pass** |
| WHO 2019 microplastics in drinking water | https://www.who.int/publications/i/item/9789241516198 | Compendium reference (low estimated risk on evidence at the time; does NOT establish fertility decline) | WHO publication; terms **UNVERIFIED** |
| BMJ 2024 ultra-processed foods umbrella review | https://doi.org/10.1136/bmj-2023-077310 (DOI verified resolving to BMJ, per vault) | Compendium reference (45 pooled analyses / ~9.9M participants) | Journal article; cited only |
| NOAA space weather scales | https://www.spaceweather.gov/noaa-scales-explanation-replaced-20231213 | Compendium reference (geomagnetic/solar-radiation storms & tech effects; does NOT establish human-cognition effects) | U.S. Government — public domain |
| WHO wireless radiofrequency exposure review | https://www.who.int/teams/environment-climate-change-and-health/radiation-and-health/non-ionizing/wireless | Compendium reference | WHO publication; terms **UNVERIFIED** |
| EEAS 2025 FIMI report | https://www.eeas.europa.eu/eeas/2025-report-eeas-activities-counter-foreign-information-manipulation-and-interference-fimi_en | Compendium reference (EU FIMI activities) | EU publication; terms **UNVERIFIED** |
| FlyWire (vault entry) | See §5 | Brain-data scaffolding | **CC BY-NC 4.0 — cite-only** |
| MICrONS / octopus atlas; C. elegans connectome | Named in vault, no URLs filed | Listed as CC-BY-4.0 / MIT-licensed alternatives (per Alice's licence policy: prefer over zebrafish) | **UNVERIFIED in this pass** — URLs + licence pages not filed; see §12 |
| Ancient Knowledge verified entries (2026-10-20): Eulogikon Ancient Greek Texts; First1KGreek; open-archaeo; NERD; UWHS; unesco-api; ArchaeoAstroInsight | https://github.com/eulogikon/ancient-greek-texts ; https://eulogikon.github.io/ancient-greek-texts/ ; https://github.com/OpenGreekAndLatin/First1KGreek ; https://github.com/zackbatist/open-archaeo ; https://github.com/apalmisano82/NERD ; https://github.com/rich-iannone/UWHS ; https://github.com/eprendergast/unesco-api ; https://github.com/marcfrincu/ArchaeoAstroInsight | Ancient-knowledge research directory (verified entries; full corrected directory at `~/workspace/your_files/ancient-knowledge-research-directory-corrected.md`) | Eulogikon: CC0 scaffolding, PD corpus · First1KGreek: **CC-BY-SA-4.0** (not PD) · open-archaeo: list CC0, linked projects keep own licences · NERD: **CC-BY 4.0** · UWHS: MIT, data current as of 2014 only (STALE) · unesco-api: no licence, student project, self-host only · ArchaeoAstroInsight: GPL-3.0 |
| CIA Gateway — "Analysis and Assessment of Gateway Process" (McDonnell, 9 Jun 1983) | https://www.cia.gov/readingroom/docs/cia-rdp96-00788r001700210016-5.pdf | Gateway/Hemi-Sync assessment; physics framing explicitly speculative, no experimental proof inside | U.S. Government (CIA release 2003) — public domain |
| Gateway Intermediate Workbook (Monroe Institute, 1977) | https://www.cia.gov/readingroom/docs/cia-rdp96-00788r001700210023-7.pdf | Affirmations + Resonant Breathing exercise | U.S. Government release; underlying Monroe material — **licence UNVERIFIED** |
| Sefer HaRazim — Morgan 1983 translation (via archive.org) | https://dn710109.ca.archive.org/0/items/solomonic-cycle-magic/Sepher%20ha-Razim.pdf ; summary https://en.wikipedia.org/wiki/Sefer_HaRazim | Jewish names-as-keys material (7 firmaments, angel lists, rituals) | Ancient text PD; **Morgan 1983 translation itself under copyright — cite/reference only, do not republish** |
| 100,000 Stars (Chrome Experiments) | https://stars.chromeexperiments.com/ | Reference for the Galaxy Layer map base | **UNVERIFIED** (visualisation; not ingested) |
| ESA Gaia "best Milky Way map" | https://www.esa.int/ESA_Multimedia/Images/2025/01/The_best_Milky_Way_map_by_Gaia | Galaxy reference (spiral arms, star density) | ESA multimedia terms generally CC BY 4.0 — **verify on the page itself before archive ingestion** (per Alice's bar); NASA imagery PD; ESO releases CC BY 4.0 |
| Atlas haul — GBIF API / pipelines / rgbif | https://github.com/GBIF/gbif-api ; https://github.com/GBIF/pipelines ; https://github.com/ropensci/rgbif | Real-creature backbone (candidate; GBIF data CC0/CC-BY/CC-BY-NC **per dataset** — ingest only CC0+CC-BY subsets) | Per-dataset; licence stamped per record |
| Atlas haul — Thompson Motif-Index database | https://folkloredatabase.com/db_thompson.php | Academic folklore motif index (candidate) | Copyright posture **UNVERIFIED → REFERENCE-ONLY** until checked |
| Atlas haul — Godchecker | https://www.godchecker.com/ | Mythology encyclopedia (finder only) | Site content copyrighted → **REFERENCE-ONLY** |
| Atlas haul — Theoi | https://www.theoi.com/ | Greek mythology (finder only; quoted ancient texts are PD translations, site compilation copyrighted) | **REFERENCE-ONLY** as a site |
| Atlas haul — Missouri library guide (world mythology) | https://libraryguides.missouri.edu/c.php?g=651166 | Librarian's map to further sources | Reference |
| Atlas haul — Wikipedia, List of theological demons | https://en.wikipedia.org/wiki/List_of_theological_demons | Demon list (cite/reference) | **CC BY-SA** — outside the bar for bulk ingestion; CC0 path is Wikidata |
| Atlas haul — Mythus Fandom wiki (Demons) | https://mythus.fandom.com/wiki/Category:Demons | Fan-compiled demon list (leads only) | **CC BY-SA**; claims unverified → REFERENCE-ONLY |
| Atlas haul — Alien Species Wiki (Fandom) | https://aliens.fandom.com/wiki/Alien_Species_Wiki | Fiction/ufology fan wiki (FICTION shelf, labelled) | **CC BY-SA** → REFERENCE-ONLY |
| Atlas haul — 5e Compendium Bestiary | https://github.com/5ecompendium/bestiary | D&D 5e monsters, structured (SRD-only content ingestible with attribution; repo may mix non-SRD material — verify per file) | SRD content **CC BY 4.0** (WotC); repo as a whole **UNVERIFIED** |
| Atlas haul — Kaggle, Mythological Creatures Text Corpus | https://www.kaggle.com/datasets/alishbaoff/mythological-creatures-text-corpus | Candidate corpus | Licence on Kaggle page; **UNVERIFIED → check before any use** |
| Atlas haul — Hugging Face, merve/folk-mythology-tales | https://huggingface.co/datasets/merve/folk-mythology-tales | Candidate corpus (tales themselves folk/PD in origin) | Licence on dataset card; **UNVERIFIED → check before use** |
| Atlas haul — NSA, "Communication with Extraterrestrial Intelligence" (CETI, Callimahos) | https://www.nsa.gov/portals/75/documents/news-features/declassified-documents/cryptologic-spectrum/communications_with_extraterrestrial.pdf | Declassified CETI article (alien/ufology shelf, "official records" corner) | U.S. Government — **public domain** |
| Atlas registry — Perseus / Scaife Viewer | https://scaife.perseus.org | Greek & Latin texts with PD translations (Apollodorus, Hesiod, Ovid) | **CC BY-SA** (XML collections) → REFERENCE-ONLY; ingest the same texts via Gutenberg instead |
| Atlas registry — Open Greek & Latin (OGL) | GitHub corpora (OpenGreekAndLatin org) | Greek/Latin TEI texts | **CC BY-SA** → REFERENCE-ONLY |
| Atlas registry — Sacred-Texts.com | https://sacred-texts.com | Finder for PD myth/religion texts (1,000+ books) | **REFERENCE-ONLY as a site** (index files/graphics/descriptive material © J.B. Hare; ingest the same texts from Gutenberg/archive.org) |
| Atlas registry — Twilit Grotto / Esoteric Archives | https://esotericarchives.com | Grimoire transcriptions (Key of Solomon, Lemegeton/Ars Goetia, Grimorium Verum, Arbatel) | **REFERENCE-ONLY as an edition** (Peterson's translations/editions are his copyrighted work); ingest PD originals via archive.org |
| Atlas registry — Grimoire scans on archive.org | https://archive.org (per-item) | Waite *Book of Black Magic* (1898), Mathers Goetia (1904), Wierus, Scot *Discoverie of Witchcraft* (1584) | **Per-item PD** — check each item's rights field |
| Atlas registry — Pathfinder 2e / Archives of Nethys | https://2e.aonprd.com | PF2 rules + bestiaries (free to read) | **ORC licence** (share-alike-style; Reserved Material excluded) → REFERENCE-ONLY under the bar |
| Atlas registry — NARA Project Blue Book records | https://www.archives.gov/research/military/air-force/ufos | USAF UFO case files 1947–1969 (12,618 reports; 94 microfilm rolls, T-1206); bulk downloads + JSON metadata ZIPs | **Public domain** (U.S. Government records) |
| Atlas registry — CIA Reading Room / CSI | https://www.cia.gov/readingroom | Declassified UFO documents incl. Blue Book Special Report No. 14, Haines's "CIA's Role in the Study of UFOs, 1947–90" | **Public domain** (U.S. Government works) |
| Atlas registry — Urbano Monte world map, 1587 (David Rumsey Map Collection, Stanford) | https://www.davidrumsey.com/blog/2017/11/26/largest-early-world-map-monte-s-10-ft-planisphere-of-1587 | Cartographic reference (60 sheets, ~10-ft planisphere; creatures placed in geographic domains) | Underlying work **public domain** (1587); scans freely viewable/downloadable at the collection |
| Atlas registry — GBIF / others in §1.2 | See §1.2 | — | — |

**Vault sections with no links filed (not sources, just empty shelves):** Toxicity Index, Elysian, RuneScape Storybook / Brain Archive, Wandering Chef's Fantasy Codex — nothing filed yet; nothing to inventory.

**Vault audit-breakdown entries (reels/pastes — NOT collection sources):** the vault's 2026-10-23–27 entries (framing effect, Lindy/Spinoza, Hygrofuel/8YSZ, Degaussing/Philadelphia Experiment, CIA ivermectin document, David Wilcock dossier, controlled-false-realities reels, Carr/Searl, pharma companion, Old Rooter) are **audited claims with sources named inside each entry** (papers, CIA document IDs, patents, court findings). They are research notes, not data collected into a project corpus, and are not re-listed here — the vault entries themselves carry their citations. One standing correction from the vault: the Lindy "time filters but never verifies" line is demoted to a filing note (derived from pasted third-party material, not Alice's own words).

---

## 12. Gaps register — filled vs open

### 12.1 Gaps FILLED in this pass (link added where a source was cited by name only)

1. **Atlas per-record name-only families** — canonical links added for: Wikidata, ITIS, NCBI Taxonomy, Catalogue of Life, Open Tree of Life, PBDB, WoRMS, AnimalTraits, AnAge, NeuroNames/BrainInfo, OpenWorm, Smithsonian Open Access, BHL, Jewish Encyclopedia, Catholic Encyclopedia (link confirmed), Bullfinch (Gutenberg #3327), Hesiod/Evelyn-White (Gutenberg #348), Poetic Edda/Bellows (Gutenberg #73533), Prose Edda/Brodeur (archive.org scan), Apollodorus/Frazer (archive.org scan), Aberdeen Bestiary contents enumeration (Wikipedia article, reference-only), Fandom/ANN/ACDB/MAL/AniList/Jikan/manami-project hosts (anime finding aids), QuestHelper repo, PalDB/Fandom/GitHub links for Palworld (recovered from the app HTML).
2. **Storybook Era 3** — canonical links added for the Tier B/C sources named without URLs: Jagex Steam news hub, SteamDB patch-note mirror, MetaForge quest list, howtovideogame quest list, gegebase quests, runescape-dragonwilds.wiki home, gamespress host.
3. **Once Human Tank blueprint** — source already credited in-template (Charie Kan YouTube link); recorded here with the audit flag attached.
4. **Dragonwilds catalog** — confirmed the two copies are identical (58 distinct URLs) and grouped them by domain with roles; verified the two most-load-bearing domains live (MetaForge page 1, Dragonwilds wiki home).

### 12.2 Gaps REMAINING OPEN (with reasons)

| # | Gap | Why it remains open | What would close it |
|---|---|---|---|
| G1 | Atlas animation (299 lists): no per-show/per-entry source URL anywhere | Never filed at build time; the lists carry only the roster-draft note + "finding aids only" statement | Add one "Sources checked" line per show list (canonical show wiki + AniList/MAL page). 299-list edit — needs Alice's call, not a silent bulk edit |
| G2 | Atlas mythic texts: Homer (Butler/Murray), Budge (*Legends of the Gods* / *Book of the Dead*), Herodotus, King *Seven Tablets of Creation*, Kojiki/Nihon Shoki PD translations, Hearn, Lady Gregory/Hyde/Curtin, Werner, Griffith Rig Veda, Britannica 11th ed. — exact ebook/scan URLs not verified | Search time in this pass covered Bullfinch, Bellows, Brodeur, Apollodorus, Hesiod only; the rest were not individually verified and URLs must not be guessed | One search round per text against Gutenberg/archive.org; file the exact ebook/item URLs |
| G3 | COMBINE / PanTHERIA / EltonTraits / Amniote — no direct dataset URL filed (paper/archive citations only) | Registry cites papers + ESA archive numbers, not download URLs | File the Figshare/ESA dataset URLs from the papers' data-availability statements |
| G4 | "Published comparative neuroanatomy compilations" (Real records) — compilation unnamed per record | Generic citation in the records themselves | Name the compilation(s) per record (or per batch) from the harvest working notes, if they survive |
| G5 | Olkowicz et al. 2016 — no DOI/URL in the record | Paper cited by author/year only | File the DOI |
| G6 | Storybook Eras 1–2: no per-quest source list; per-quest wiki URLs never filed | Trackers record verification notes without URLs | Reconstruct mechanically (one wiki page per quest on oldschool.runescape.wiki / runescape.wiki) and file as an era sources appendix — needs a verification pass, not just URL generation |
| G7 | Storybook Era 3: gamespress per-release URLs; Escapist roadmap article URL; devtrackers mirror URL; runescape-dragonwilds.wiki quest-index exact URL; "ru24" fishing guide (full name/URL unknown) | Hunt files cite these by name only; not verified in this pass | Re-locate each item by search and file the exact URLs; identify "ru24" |
| G8 | Dragonwilds catalog: MetaForge licence/terms; Dragonwilds wiki licence (CC BY-SA assumed, not verified); all guide/press sites' licences | No terms statement was ever recorded for these fan/press sources | Check MetaForge terms + wiki footer licence; record "all-rights-reserved, facts only" explicitly for the guide sites |
| G9 | Aniimo: PikaMMO, aniimoguide, aniidex.com, aniimotools.dev licences; wanghuan072 repo already known (no LICENSE file) | No licence statement on file for the fan databases | Check each site's footer/terms; record the result (expect: no licence → all-rights-reserved, facts-only posture stands) |
| G10 | Palworld builder: no sources file; main roster/stats source unidentified; per-pal source URLs absent | Never filed at build time; sources recovered only from HTML links (egg layer) | Fresh audit of the app's data against PalDB + a build-time sources note; file `palworld_SOURCES.md` |
| G11 | Once Human Atlas Class Builder: no sources file; data origin entirely unidentified | Never filed | Identify the data origin (in-game observation? wiki? guides?) and file `once-human_SOURCES.md` |
| G12 | Anime SOURCES_TO_CHECK leads: HatsuSumi / anime-character-database, Munna-Scriptz / free-anime-apis, Bas1874 / Anime-Watch-Order-Api — existence unchecked; manami-project / Jikan / WaifuAPI / ACDB licences unchecked | Google-AI leads, never existence-checked | Existence + licence check per repo; strike non-resolving entries |
| G13 | Vault: MICrONS / octopus atlas + C. elegans connectome — named, no URLs filed | Vault entry gives licence claims (CC-BY-4.0 / MIT) without links | File the dataset URLs + licence pages |
| G14 | Vault: Kaggle myth corpus, HF folk-mythology-tales, Thompson Motif-Index, Theoi, Godchecker — licences unverified (reference-only already) | Hunt flagged them UNVERIFIED / reference-only in 2026-10-23 | Check the Kaggle/HF dataset cards + Motif-Index terms before any use (they are candidates, not yet used) |
| G15 | Free-data directory: Catalogue of Life (checklist DB), Theoi, Attalus — UNVERIFIED in the 2026-10-20 survey | Survey could not verify terms on the source itself | Re-check their terms pages |
| G16 | FlyWire: Zenodo metadata CC-BY-4.0 vs steward terms CC BY-NC 4.0 (see §5); `flywire_SOURCES.md` attribution line said CC-BY-4.0 (fixed 2026-11-09) | Live pages disagree; the file wording was stale, now fixed 2026-11-09 | Fixed 2026-11-09 by the parallel legality sweep (attribution line now CC BY-NC 4.0) |
| G17 | SRD 5.1: 16 records' verbatim flavour text (rewritten 2026-11-09) — the *inventory* is unaffected (source + licence unchanged), but the Atlas records' `origin` fields were edited by the parallel sweep | Fix work in progress elsewhere | Confirm with the sweep owner that all 16 are rewritten + verified (reported done 2026-11-09) |
| G18 | Fandom wikis' CC BY-SA (platform default, not re-verified on-page); Old School / RuneScape wiki CC BY-SA (platform default, not re-verified on-page) | Not checked on the source pages in this pass | One check per site footer/terms; record the exact licence text. (QuestHelper's licence is now VERIFIED — BSD 2-Clause, © 2026-11-09 check of the local clone's LICENSE file — and has been moved out of this gap.) |

### 12.3 Licences that could NOT be verified in this pass

- **MetaForge** (Dragonwilds DB) — no terms/licence statement found; assumed all-rights-reserved fan DB, facts-only use.
- **PikaMMO Aniidex, aniimoguide.com, aniidex.com, aniimotools.dev** (Aniimo) — no licence statements on file.
- **PalDB (paldb.cc)** — no licence statement checked.
- **All Dragonwilds guide/press sites** (§6, except official Jagex material) — treated as all-rights-reserved, facts-only; not individually verified.
- **Palworld GitHub repos, anime metadata repos/APIs (Jikan, manami-project, WaifuAPI), ACDB, ANN, MAL/AniList terms** — not checked on their pages. (QuestHelper's licence is verified: BSD 2-Clause, © 2020 Zoinkwiz, from the local clone's LICENSE file — see §7.1.)
- **FlyWire Zenodo metadata licence** — not visible on the live Zenodo page as fetched 2026-11-09 (steward terms CC BY-NC 4.0 verified instead; see §5).
- **COMBINE / PanTHERIA / EltonTraits / Amniote / AnAge** — licence claims rest on secondary licence tables / paper text, not on a fresh check of each dataset page (EltonTraits/Amniote/AnAge flagged "confirm before bulk ingestion" in the registry itself).
- **PHYLACINE, WormAtlas** — UNVERIFIED in the 2026-10-23 hunt (PHYLACINE's Dryad home "normally means CC0" — check the dataset page before use).
- **Kaggle myth corpus, HF folk-mythology-tales, Thompson Motif-Index** — UNVERIFIED (candidates only, nothing collected).
- **Gateway Intermediate Workbook underlying Monroe material; WHO/EEAS publications** — terms not checked.
- **Charie Kan video** — no permission on file for the 5 frames / video copy (audit flag, separate fix work).

**Licences verified correct in this pass (spot-checks, 2026-11-09):** SRD 5.1/5.2 **CC BY 4.0** (D&D Beyond's own SRD page, fetched live); FlyWire public release **CC BY-NC 4.0** (flywire.ai/guidelines, fetched live — supersedes the Zenodo metadata claim); Wikidata **CC0** (live homepage + Licensing statement as cited in the vault); Aberdeen Bestiary site resolves (abdn.ac.uk/bestiary); Jagex Fan Content Policy v1.4 live at legal.jagex.com; Bullfinch Gutenberg #3327 PD; Hesiod/Evelyn-White Gutenberg #348; Poetic Edda/Bellows Gutenberg #73533; dnd5eapi.co live SRD JSON; MetaForge page 1 live; Dragonwilds wiki home live; official Aniimo wiki live (roster has grown past the 2026-10-14 snapshot); PalDB eggs page live; runescape.wiki home live; New Advent Catholic Encyclopedia live.

---

## Appendix A — Verification log (this pass, 2026-11-09)

Spot-check method: for each distinct domain listed, the homepage/API root (or the exact canonical URL where one exists) was fetched and confirmed to resolve to the named source. Full per-URL checking was not done for the Dragonwilds catalog's 58 URLs (domain-level check + the two most-load-bearing pages fetched live); the Aniimo source URLs are as filed 2026-10-14 except where noted live above.

| Check | Result |
|---|---|
| wikidata.org | ✓ resolves (live homepage) |
| dnd5eapi.co/api/2014/monsters/aboleth | ✓ live SRD JSON returned |
| flywire.ai/guidelines | ✓ "public release data … CC BY-NC 4.0" (live) |
| doi.org/10.5281/zenodo.10676866 | ✓ Zenodo record v783 resolves; no licence field visible in fetched text |
| abdn.ac.uk/bestiary | ✓ resolves (University bestiary site) |
| legal.jagex.com (+ /docs/policies/fan-content-policy.md) | ✓ Legal Portal live; Fan Content Policy linked |
| runescape.wiki | ✓ resolves (crawl copy old, 2024; live wiki current) |
| dragonwilds.runescape.wiki | ✓ resolves (community wiki home) |
| wiki.aniimo.com/en | ✓ live index (130 entries — roster grown since the 2026-10-14 snapshot) |
| metaforge.app/…/creatures-npcs/page/1 | ✓ live entries returned |
| paldb.cc/en/Eggs | ✓ live egg table returned |
| newadvent.org/cathen | ✓ live (Catholic Encyclopedia home) |
| dndbeyond.com/srd | ✓ live; "Both SRD 5.1 and 5.2 are available under CC-BY-4.0" |
| gutenberg.org/ebooks/3327 (Bullfinch) | ✓ via search (PD, USA) |
| gutenberg.org/ebooks/348 (Hesiod/Evelyn-White) | ✓ via search (eBook #348) |
| gutenberg.org/ebooks/73533 (Poetic Edda/Bellows) | ✓ via search (eBook #73533) |
| archive.org Prose Edda/Brodeur scan | ✓ via search (1916 scan, PD) |
| archive.org Apollodorus/Frazer scan | ✓ via search (1921 Loeb scan, PD) |
| github.com/Zoinkwiz/quest-helper | ✓ via search (repo exists); licence **BSD 2-Clause © 2020 Zoinkwiz** verified from the local clone's LICENSE file (`~/workspace/osrs-repos/quest-helper/LICENSE`) |
| Dragonwilds catalog two-copy diff | ✓ identical 58 distinct URLs |
| Atlas per-record source audit | 470 distinct source strings; 57 with URLs, 413 name-only (counts from the JSON files) |
| Atlas counts reconciliation | ✓ 909 records / 907 distinct + 3,666 animation = 4,573 distinct (matches audit) |

**Domains listed in this inventory but NOT live-checked in this pass** (relied on the filed attribution + the 2026-10-23 hunt's own checks): itis.gov, ncbi.nlm.nih.gov, catalogueoflife.org, opentreeoflife.org, paleobiodb.org, marinespecies.org, animaltraits.org, braininfo.org, openworm.org, si.edu, biodiversitylibrary.org, jewishencyclopedia.com, sacred-texts.com, scaife.perseus.org, esotericarchives.com, 2e.aonprd.com, archives.gov, cia.gov/readingroom, nsa.gov CETI PDF, eulogikon/First1KGreek/open-archaeo/NERD/UWHS/unesco-api/ArchaeoAstroInsight GitHub repos, GBIF/folkloredatabase/godchecker/theoi/kaggle/huggingface links, all Dragonwilds guide/press domains beyond MetaForge + the Dragonwilds wiki, all Aniimo fan-database domains beyond the official wiki, palworld GitHub repos, youtu.be/ThYVShxPbig, oldschool.runescape.wiki, gamespress.com, steam store news hub. These are recorded as filed (with their filed licence status); a live re-check round for them is a follow-up, not a blocker — none of them is the sole source for a corpus.

---

*End of inventory. Maintenance note: when a GAP in §12.2 is closed, edit that row in place (move it to §12.1 with the date) rather than appending a new section, so this file stays the single consolidated list. When a new project/corpus starts collecting data, add its section here first — before the data lands in the project.*
