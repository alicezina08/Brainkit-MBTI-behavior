# Copyright Audit Checklist — reusable method

**Standing rule (Alice, 2026-11-08):** every coding project must be 100% free of
copied copyrighted material — original expression, licensed, or public-domain only;
no verbatim game text / art / music / code anywhere; game-derived content is
summary / facts / names only, never verbatim. The RuneScape storybook is a fan
derivative retelling under Jagex's Fan Content Policy (licensed fan work) — the rule
means no copied material *inside* it, not that it stops being a RuneScape retelling.

This file is the method from the first audit (BrainKit Atlas, 2026-11-08). Follow it
in order. The audit is **read-only**: never modify the audited files — report only.

## 0. Scope first

- Name the corpus precisely (directory, file count, record count). Count **instances**
  and **distinct entities** separately — batch files + compiled files can store the
  same record twice, which inflates the count.
- Name the rule being audited against (above) and the schema doc, if any
  (Atlas: `Docs/COMMON_ENTITY_RECORD.md`).

## 1. Programmatic sweep (scan everything, sample nothing)

Write a script (Python + `json`/`glob`/`re`) that walks every file and checks:

1. **Record census** — files parsed / unparsed; total record instances; distinct
   IDs; records per sub-directory. A record = a dict carrying the schema's identity
   keys (e.g. `entity_id` + `evidence_grade` + `personality`).
2. **Provenance coverage** — for every record: `source_and_license` present and
   non-empty? `evidence_grade` present? `evidence_class` present? MBTI /
   personality label present and containing an interpretation marker
   (`interpret…` / `fan interpretation`)? Report counts, not just a pass/fail.
3. **Copy signals in every free-text field** (skills, attributes, behavior,
   notes, relationships, memory, cognition, game implementation, origin):
   - URLs (`http`, wiki/fandom domains) — note whether they sit in a *source
     list* (pointer, clean) or in *prose* (suspicious).
   - Wiki template markup: `{{`, `}}`, `[[`, `]]`, `Category:`, `File:`.
     Beware the false positive: case-insensitive `file:` also matches
     `profile:` — check context before flagging.
   - Attribution phrasing: `according to the wiki`, `the wiki states`,
     `citation needed`, `retrieved from`, `oldid`, `infobox` (check context:
     "per the official wiki infobox" is a provenance note, not copied text).
   - Long quoted passages: text inside `"` / `"` `"` of ≥40 characters.
   - Length outliers: every free-text string ≥80 words, listed longest-first.
   - Duplicated long strings: normalized strings ≥60 chars appearing in 2+
     records. Expect boilerplate (standard labels, template sentences) — the
     hunt is for *substantive* duplicated prose, not labels.
4. **Field-shape checks** — e.g. `origin` / `attributes` length distribution per
   sub-directory; a sub-directory whose text fields run systematically longer
   than the rest deserves a targeted read.

## 2. Targeted reads (read flagged passages in full context)

Never call a flag copied from the regex hit alone. Read each flagged passage whole
and adjudicate it against the line below. In the Atlas audit this cleared all 19
automated quote flags (they were quotations of the project's *own* lean entries)
and confirmed the one real finding.

- Read the **longest fields** in each sub-directory (top ~10 overall, top ~4 per
  risky sub-directory).
- Read a **random sample** (≥4) of records from each game-derived sub-directory
  in full — all text fields.
- Read every **verbatim-candidate**: any field whose wording matches a known
  source text. Confirm against the live source with a web search for a
  distinctive phrase (exact-phrase search), and cite the source found.

## 3. The line: fact / summary vs copied wording

| Side | What it looks like | Examples from the Atlas audit |
|---|---|---|
| **Fact (clean)** | Short factual phrases, numbers, names, stat lines | "40 HP in source; drops: Feathers"; "Medium humanoid, challenge rating 2"; a character's name |
| **Summary in our own words (clean)** | Same facts, different sentence structure and wording; Atlas template voice ("Triggers: … -> …", "Built by analogy…") | Dragonwilds records restating HP/drops/behaviour; SRD `behavior_model` template text; bestiary fish entry (condensed paraphrase of the Aberdeen Bestiary translation, source attributed, CC BY) |
| **Close paraphrase, licensed + attributed (clean, note it)** | Follows a source sentence-by-sentence but reworded; source is PD or CC BY and the record says so | Bestiary entries after the Aberdeen Bestiary (CC BY 4.0, attributed) |
| **Verbatim public-domain text, labeled PD (clean, note it)** | Word-for-word reproduction of a PD source, with the PD status stated in `source_and_license` | Goetia `attributes` quoting the Mathers 1904 translation (~70 of 72 records) — permitted by the rule, but the license wording should say the *attributes* quote the PD source, not only that brain/personality text is original |
| **Verbatim CC-BY text, attributed (rule violation, not infringement)** | Word-for-word reproduction of CC-BY-licensed text with attribution in the license field — legally permitted, but it breaks the no-verbatim rule and any "text is original" claim in the record | SRD `origin` fields: 16 distinct entities (acolyte, archmage, assassin, awakened-shrub, awakened-tree, axe-beak, bandit, bandit-captain, blink-dog, blood-hawk, cult-fanatic, cultist, death-dog, druid, flying-snake, frog) — verbatim SRD 5.1 flavor text, confirmed against the live SRD |
| **Verbatim copyrighted text, unattributed (clear copy — the red line)** | Word-for-word game dialogue, quest text, examine text, or wiki (CC BY-SA) prose reproduced without a licence | None found in the Atlas audit |

Short quoted fragments of *the project's own* files (e.g. confidence notes
quoting the project's lean entries, "LEAN-ENTRY FLAGS CARRIED OVER VERBATIM")
are internal carry-over, not copying — clean, but worth one line in the report
so nobody re-flags them later.

## 4. Severity tiers for the report

- **CLEAR COPY** — verbatim copyrighted (or rule-breaking verbatim) text. List
  every instance: file, entity, field, exact text, source it matches.
- **SUSPICIOUS** — reads like copied wording but not confirmed against a source.
  Read in full context and resolve to clear-copy or clean before reporting.
- **CLEAN-BUT-NOTEWORTHY** — compliant, but sits near the line or needs a wording
  fix (e.g. verbatim PD text; a license claim that overstates originality;
  close paraphrases; duplicated storage of the same record).
- **CLEAN** — facts, summaries, template voice, boilerplate labels.

## 5. Report format

1. **Verdict first** — clean as built, or what needs fixing (one paragraph).
2. **Scope** — files, instances, distinct entities, per-directory counts.
3. **Provenance stats** — missing source/license/grade/label counts (exact numbers).
4. **Findings by severity** — for each flagged record: file, entity id/name,
   field, exact flagged text (quoted), reason, and the source it matches
   (with verification method).
5. **What was checked and cleared** — the negative results matter (no game
   dialogue, no quest text, no examine text, no wiki markup, no CC BY-SA prose).
6. **Fixes recommended (not made)** — concrete, per finding (e.g. "rewrite these
   16 `origin` fields as Atlas-voice summaries, keep the factual stat line;
   correct the 'text is original' license claim on those records").
7. **Hygiene notes** — non-copyright issues found en route (e.g. batch +
   compiled duplication inflating counts).

## 6. Commands used (Atlas audit, adapt paths per project)

```bash
# census + provenance + signal sweep (script saved at /tmp/atlas_audit.py)
python3 /tmp/atlas_audit.py
# distinct entities vs instances; per-directory counts; license strings
python3 - <<'EOF'
# ... collector + collections.Counter over entity_id / source_and_license
EOF
# verify a suspected verbatim passage against the live source:
# exact-phrase web search, e.g.:
#   "It takes a strong personality, ruthless cunning, and a silver tongue"
```

## 7. Traps found on the first run (don't re-learn them)

- `file:` matches `profile:` — always read the context.
- Quote-regex flags hit internal quotations of the project's own companion files.
- Boilerplate dominates duplicate-string counts (standard MBTI label: 5,223×) —
  sort duplicates by length and read the long ones, don't count raw hits.
- "Total records" in project memory may be a subset (Atlas: 3,666 = animation
  only; full Atlas is 4,573 distinct entities). Recompute, don't quote memory.
- A record's *claim* ("text is original") is itself auditable — check the text
  against the claim, especially in licensed-source directories (SRD, Goetia).
