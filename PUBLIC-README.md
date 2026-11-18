# BrainKit — Public-Safe Version

This is the public-safe version of BrainKit, Alice's universal
creature-brain system. It shares the engine, the method, and the
public-domain data. The full Atlas — with complete brain profiles for
copyrighted characters — is Alice's private research and is **not**
included here.

## What is BrainKit?

BrainKit gives game creatures and NPCs a real cognitive architecture
instead of a single behavior script: a sized brain, differentiated
perception, individual memory (threats *and* kindness), relationships,
and faction dynamics. It is the training scaffolding for alive AI —
game creatures that react as if truly alive — built on real brain
data used generatively, never coercively.

## What is in this version

- **Core/** — the portable C++17 core (BrainProfile, MemoryLedger,
  FactionSim). MIT-licensed, as published on GitHub.
- **Docs/** — the method: the Common Entity Record (Alice's 14-field
  schema), the Universal Atlas design, the sources inventory, the
  integration guide, and the copyright-audit checklist.
- **Schema/** — the creature profile JSON schema: one data contract
  for every game.
- **Examples/** — UE4SS Lua samples, a Skyrim Papyrus sample, Python
  prototypes, and reports.
- **Unreal/** — the thin Unreal adapter (BrainComponent).
- **Atlas/ (full data)** — the public-domain and openly-licensed
  shelves, with complete records:
  - Real — real species (CC0 / public literature)
  - Mythic — mythology (public domain)
  - Spiritual — spiritual beings (public domain)
  - Bestiary — the Aberdeen Bestiary (CC BY 4.0)
  - Goetia — the Ars Goetia (public domain, 1904 Mathers translation)
  - SRD — D&D SRD 5.1 monsters (CC BY 4.0, Wizards of the Coast)
  - Pilot — the 13 hand-built founding records (the Dragonwilds Wolf
    and the Alien Xenomorph are reference-only stubs; see below)
  - Ancient Knowledge — links only (the research notes themselves stay
    in Alice's private archive)
  - multiverse_map.json — the Universal Map graph. Nodes for the
    Dragonwilds game layer and the Alien Xenomorph are reference-only
    (name and address on the map, no profile); everything else is
    full data.
- **Atlas/reference/ (reference only)** — copyrighted characters,
  listed by name only:
  - anime-reference-index.md — anime characters
  - western-reference-index.md — western animation characters
  - dragonwilds-reference-index.md — RuneScape: Dragonwilds creatures,
    bosses and NPCs
  - These contain **no brain profiles, no MBTI, no skills or movesets,
    and no lore summaries**. The full profiles for these characters
    live in Alice's private Atlas.

## The split (why two versions)

The full Atlas is Alice's private research database. It holds complete
profiles for characters from copyrighted shows and games. She keeps
that version private so the work is not gutted, and shares this public
version instead. This public version shares the engine, the method, and
every record that is public-domain or openly licensed — and lists
copyrighted characters by name only, as a reference.

## Rules this version follows (Alice's five BrainKit principles)

1. Original analysis belongs to BrainKit.
2. Third-party factual references retain attribution where appropriate.
3. Licensed material retains its license information.
4. Copied expressive content requires permission or another valid legal
   basis.
5. Generated and inferred information is labelled accurately.

MBTI in this version is a lore-based interpretive read (fan
interpretation), never a measurement. Evidence grades are labelled on
every record: MEASURED / INFERRED / GENERATED.

## Licences in this package

- BrainKit Core and Alice's original writing: MIT License © 2026
  alicezina08 (see README.md).
- D&D SRD 5.1 content: CC BY 4.0 (Wizards of the Coast) — attribution
  kept in each record.
- Aberdeen Bestiary material: CC BY 4.0 (University of Aberdeen
  digitisation).
- Everything else in the Atlas: public domain or CC0, as stated in each
  record's source_and_license.
