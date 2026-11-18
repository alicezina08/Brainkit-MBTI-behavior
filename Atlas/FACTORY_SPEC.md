# Atlas Factory Spec — corpus harvest runs (2026-10-23)

Shared instructions for every harvest batch writer. The pilot
(`Atlas/pilot/atlas_pilot.json`) is the quality reference; corpus records are
the LEAN-COMPLETE version of the same shape.

## Binding rules (Alice's)

1. **Grades honest.** Every record carries `evidence_grade`: MEASURED (real
   data behind the brain facts) / INFERRED (from kin + documented behaviour,
   basis stated) / GENERATED (built from lore/canon). Never upgrade a grade to
   fill a field.
2. **MBTI is a labelled interpretive read.** `personality.mbti_label` must be:
   "Lore-based interpretive read (fan interpretation) — a behaviour-design
   lens, not a measurement." (For REAL creatures add "Basis here: documented
   behaviour.") Every MBTI gets a one-line justification from the creature's
   own lore/behaviour text, and a `runner_up` where a second type is arguable.
3. **No invented lore.** Use only the source material named in your task
   (PD text, stat block, the catalog entry's own fields, established species
   facts). Where the source is thin, write a lean record and say exactly that
   in `confidence_and_conflicts`. An honest short record beats a padded one.
4. **Brains are generated FROM ground truth**: real neuroanatomy/allometry for
   real creatures (Jerison E = 0.12·P^0.67, P in grams, where a body mass is
   known); region-analogue design from the lore's own cognitive claims for
   storied ones — each analogue named as a design decision, never as anatomy.
5. **Licences per the bar.** PD/CC0/CC-BY sources may be drawn on; fan-wiki
   text is never copied — facts in your own words, provenance in
   `source_and_license`, fan tier labelled where used.
6. **Canon outranks fan data**; conflicts go in `confidence_and_conflicts`,
   never silently resolved.

## Record shape (JSON object, exactly these top-level keys)

- `entity_id` — per your task's ID convention.
- `entity_type`
- `name_and_aliases` — {primary, scientific_name (real only), aliases[]}
- `origin` — 1–2 sentences.
- `evidence_class` — one of: Scientific observation / Historical source /
  Religious account / Fictional canon / Fictional canon (game data) /
  Hypothesis (community accounts) — with qualifiers in parentheses as needed.
- `evidence_grade`
- `source_and_license` — {sources[], license}
- `attributes` — 1–3 sentences from the source.
- `cognition_model` — {brain_profile: {grade_note, architecture (1–3
  sentences), regions: [{name, role, drive_weight}] (2–4), drives:
  {curiosity, sociability, aggression, fearfulness, territoriality} each
  0..1}, summary (1–2 sentences)}
- `personality` — {mbti, mbti_label, justification, runner_up, traits (same
  five drives)}
- `skills` — 3–6 items, each traceable to the source.
- `behavior_model` — 2–4 sentences: triggers / needs / goals / state changes.
- `relationships` — 1–3 sentences; name kin, factions, linked entities.
- `memory_model` — 1–3 sentences: what it knows/remembers/forgets/misreads.
- `confidence_and_conflicts` — honest gaps, source disagreements, thin spots.
- `game_implementation` — 1–2 sentences: how BrainKit would run it.
- `map_placement` — {universe, domain, address, bridges: [{to_entity_id,
  kind (variant_of|core_of|kinship|storied_form_of), note}]}. Bridges only
  where a link is genuinely claimed; note link confidence in the note.
- `core_entity_id` — the core record's id, or null.
- `revision_history` — [{date: "2026-10-23", change: "Corpus harvest record
  created (<corpus> run).", source: "<source named in task>"}]

## Output

Write ONE JSON array of your records to the exact output path in your task,
valid JSON (double quotes, no trailing commas, no comments). Verify with
python3 json.load before reporting. Report: count written, any records you
had to keep especially lean and why, any core links claimed.
