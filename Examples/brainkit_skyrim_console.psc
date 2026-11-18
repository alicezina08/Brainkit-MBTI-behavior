; BrainKit_Skyrim_Console.psc -- BrainKit for Skyrim on Xbox Series X
; CONSOLE-SAFE PAPYRUS SAMPLE. Reference scaffold, NOT tested in-game.
;
; Why a different version for console:
;   Skyrim on Xbox Series X CANNOT use SKSE, F4SE, DLLs, UE4SS, Lua, or
;   any external code. Console mods run through Bethesda.net only, with
;   a 5 GB / 150-mod limit, and only vanilla Papyrus + vanilla assets.
;   So this version is PURE VANILLA PAPYRUS -- no SKSE functions, no
;   JContainers, no JsonUtil, no StorageUtil, no file reads, no network.
;   If a line in here needs SKSE, it is a bug -- tell C and it gets cut.
;
; What it does (same BrainKit idea, Papyrus-shaped):
;   * MemoryLedger in Papyrus: threat AND kindness per individual,
;     with forgetting (decay) and generalization to categories.
;     Papyrus has no dictionaries, so memory is parallel arrays:
;     KnownIDs[] / Threat[] / Kindness[] / LastSeen[].
;   * attitude -> mode Calm / Wary / Alarmed, from traits.
;   * Hooks are VANILLA ACTOR EVENTS only: OnHit, OnActivate,
;     OnCombatStateChanged. Those fire on console.
;   * No save edits beyond the NPC's own script state. No telemetry.
;
; What it is NOT:
;   * Not a full mod. It is ONE script to attach to ONE NPC in the
;     Creation Kit. A full console mod also needs: an .esp/.esl made
;     in the Creation Kit, the script compiled there, the NPC / quest
;     wired up, and an upload to Bethesda.net. I cannot do the
;     Creation Kit compile or the Bethesda.net upload from here.
;   * Not tested in-game. Papyrus syntax was checked by reading only;
;     it has NOT been compiled in the Creation Kit, and I have no Xbox
;     to test it on. A modder with the Creation Kit must compile it
;     and test it on console before publishing.
;   * Not consciousness, not a neural network. Traits + memory + rules.
;
; How to use (PC Creation Kit, for an Xbox upload):
;   1. In the Creation Kit, create this script (BK_Brain) and attach
;      it to an NPC (e.g. a test follower / guard).
;   2. Set the Trait properties in the NPC's script properties.
;   3. Compile in the Creation Kit. Fix any Papyrus errors it reports.
;   4. Save as .esp/.esl, upload to Bethesda.net, install on Series X
;      from the in-game Mods menu. Keep the whole mod well under 5 GB
;      (this script alone is a few KB).
;
; Skyrim Special / Anniversary Edition, Xbox Series X.
; Papyrus version: vanilla only. No SKSE. No DLL. No Lua.

Scriptname BK_Brain extends Actor

; --- Traits: lore-based, fan interpretation, as always. 0.0 - 1.0. ---
Float Property AggressionTrait Auto = 0.6
Float Property SociabilityTrait Auto = 0.5
Float Property CuriosityTrait Auto = 0.5
Float Property FearfulnessTrait Auto = 0.6
Float Property TerritorialityTrait Auto = 0.8

; --- Memory config: same numbers as the C++ core. ---
; Half-life in GAME DAYS (Papyrus time is in days, not seconds).
; 1.0 day = 24 hours, matching the 24h half-life in BrainKit.
Float Property MemoryHalfLifeDays Auto = 1.0
Float Property GeneralizationRate Auto = 0.3
Int Property MaxIndividuals Auto = 64

; --- Memory: parallel arrays (Papyrus has no dictionaries). ---
String[] KnownIDs
Float[] ThreatMemory
Float[] KindnessMemory
Float[] LastSeenDays
String[] KnownCategories
Float[] CategoryThreat
Float[] CategoryKindness

; --- Current state, readable by other scripts / packages. ---
String Property CurrentMode Auto Hidden
String Property FocusTarget Auto Hidden
Float Property Arousal Auto Hidden

; ---------------------------------------------------------------------------
; Helpers
; ---------------------------------------------------------------------------

Float Function DecayValue(Float afValue, Float afDaysPassed)
    If afDaysPassed <= 0.0
        Return afValue
    EndIf
    ; Half-life decay: value * 0.5 ^ (days / half-life)
    Return afValue * Math.Pow(0.5, afDaysPassed / MemoryHalfLifeDays)
EndFunction

Int Function FindIndividual(String asID)
    Return KnownIDs.Find(asID)
EndFunction

Int Function FindCategory(String asCategory)
    Return KnownCategories.Find(asCategory)
EndFunction

; ---------------------------------------------------------------------------
; RecordInteraction: the heart of BrainKit. Call this from events below.
; afThreat / afKindness are amounts, not totals. Categories generalize.
; ---------------------------------------------------------------------------
Function RecordInteraction(String asID, Float afThreat, Float afKindness, String[] aCategories)
    Float fNow = Utility.GetCurrentGameTime()
    Int iIndex = FindIndividual(asID)
    If iIndex < 0
        ; New person: add them, evict the oldest if we are full.
        If KnownIDs.Length >= MaxIndividuals
            ; Oldest entry is index 0 (insertion order).
            KnownIDs = PapyrusUtil_RemoveAt(KnownIDs, 0)
            ThreatMemory = PapyrusUtil_RemoveAt_Float(ThreatMemory, 0)
            KindnessMemory = PapyrusUtil_RemoveAt_Float(KindnessMemory, 0)
            LastSeenDays = PapyrusUtil_RemoveAt_Float(LastSeenDays, 0)
        EndIf
        KnownIDs.Add(asID)
        ThreatMemory.Add(0.0)
        KindnessMemory.Add(0.0)
        LastSeenDays.Add(0.0)
        iIndex = KnownIDs.Length - 1
    EndIf

    Float fDays = fNow - LastSeenDays[iIndex]
    If fDays > 0.0 && LastSeenDays[iIndex] > 0.0
        ThreatMemory[iIndex] = DecayValue(ThreatMemory[iIndex], fDays)
        KindnessMemory[iIndex] = DecayValue(KindnessMemory[iIndex], fDays)
    EndIf
    ThreatMemory[iIndex] = ThreatMemory[iIndex] + afThreat
    KindnessMemory[iIndex] = KindnessMemory[iIndex] + afKindness
    LastSeenDays[iIndex] = fNow

    ; A slice of every lesson generalizes to its categories.
    Int i = 0
    While i < aCategories.Length
        String sCat = aCategories[i]
        Int iCat = FindCategory(sCat)
        If iCat < 0
            KnownCategories.Add(sCat)
            CategoryThreat.Add(0.0)
            CategoryKindness.Add(0.0)
            iCat = KnownCategories.Length - 1
        EndIf
        CategoryThreat[iCat] = CategoryThreat[iCat] + afThreat * GeneralizationRate
        CategoryKindness[iCat] = CategoryKindness[iCat] + afKindness * GeneralizationRate
        i += 1
    EndWhile
EndFunction

; NOTE: Papyrus has no built-in array-remove helper in vanilla script.
; The two functions below are intentionally SIMPLE and local to this
; script -- they rebuild the array without the removed index. They use
; only vanilla Papyrus (no SKSE). If the Creation Kit complains about
; them, replace them with a manual rebuild in RecordInteraction.
; (Kept as separate functions so the eviction logic stays readable.)

String[] Function PapyrusUtil_RemoveAt(String[] aArray, Int aiIndex)
    String[] sNew = new String[0]
    Int i = 0
    While i < aArray.Length
        If i != aiIndex
            sNew.Add(aArray[i])
        EndIf
        i += 1
    EndWhile
    Return sNew
EndFunction

Float[] Function PapyrusUtil_RemoveAt_Float(Float[] aArray, Int aiIndex)
    Float[] fNew = new Float[0]
    Int i = 0
    While i < aArray.Length
        If i != aiIndex
            fNew.Add(aArray[i])
        EndIf
        i += 1
    EndWhile
    Return fNew
EndFunction

; ---------------------------------------------------------------------------
; GetAttitude: kindness - threat, decayed. Positive = likes you.
; ---------------------------------------------------------------------------
Float Function GetAttitude(String asID)
    Int iIndex = FindIndividual(asID)
    If iIndex < 0
        Return 0.0
    EndIf
    Float fNow = Utility.GetCurrentGameTime()
    Float fDays = fNow - LastSeenDays[iIndex]
    Float fThreat = ThreatMemory[iIndex]
    Float fKind = KindnessMemory[iIndex]
    If fDays > 0.0 && LastSeenDays[iIndex] > 0.0
        fThreat = DecayValue(fThreat, fDays)
        fKind = DecayValue(fKind, fDays)
    EndIf
    Return fKind - fThreat
EndFunction

Float Function GetCategoryAttitude(String asCategory)
    Int iCat = FindCategory(asCategory)
    If iCat < 0
        Return 0.0
    EndIf
    Return CategoryKindness[iCat] - CategoryThreat[iCat]
EndFunction

; ---------------------------------------------------------------------------
; Think: attitude -> mode. Fearful NPCs alarm sooner; aggressive ones
; tolerate more threat before flipping from Wary to Alarmed.
; Call this after any RecordInteraction, or on a timer from a quest.
; ---------------------------------------------------------------------------
Function Think()
    Float fNow = Utility.GetCurrentGameTime()
    String sFocus = ""
    Float fBest = 0.0
    Int i = 0
    While i < KnownIDs.Length
        Float fAtt = GetAttitude(KnownIDs[i])
        If Math.Abs(fAtt) > fBest
            fBest = Math.Abs(fAtt)
            sFocus = KnownIDs[i]
        EndIf
        i += 1
    EndWhile
    FocusTarget = sFocus
    Arousal = fBest
    Float fWaryAt = 0.5 + (AggressionTrait - FearfulnessTrait) * 0.3
    Float fAlarmAt = 1.5 + (AggressionTrait - FearfulnessTrait) * 0.5
    If fBest >= fAlarmAt
        CurrentMode = "Alarmed"
    ElseIf fBest >= fWaryAt
        CurrentMode = "Wary"
    Else
        CurrentMode = "Calm"
    EndIf
EndFunction

; ---------------------------------------------------------------------------
; Vanilla events only -- these fire on Xbox Series X, no SKSE needed.
; ---------------------------------------------------------------------------

Event OnInit()
    KnownIDs = new String[0]
    ThreatMemory = new Float[0]
    KindnessMemory = new Float[0]
    LastSeenDays = new Float[0]
    KnownCategories = new String[0]
    CategoryThreat = new Float[0]
    CategoryKindness = new Float[0]
    CurrentMode = "Calm"
    FocusTarget = ""
    Arousal = 0.0
    ; Console-safe: Debug.Notification is vanilla. Remove for release
    ; if you do not want the pop-up, or keep it for testing only.
    Debug.Notification("BrainKit: " + GetDisplayName() + " is watching (Calm).")
EndEvent

Event OnHit(ObjectReference akAggressor, Form akSource, Projectile akProjectile, Bool abPowerAttack, Bool abSneakAttack, Bool abBashAttack, Bool abHitBlocked)
    If akAggressor == None
        Return
    EndIf
    String sID = akAggressor.GetDisplayName()
    If sID == ""
        sID = "unknown"
    EndIf
    String[] sCats = new String[1]
    sCats[0] = "attacker"
    ; TODO(game): add real tags here if you know them, e.g. faction or
    ; armor type, from vanilla properties only. Do not invent SKSE calls.
    RecordInteraction(sID, 1.0, 0.0, sCats)
    Think()
    Debug.Notification("BrainKit: " + GetDisplayName() + " remembers " + sID + " hurt them. Mode: " + CurrentMode)
EndEvent

Event OnActivate(ObjectReference akActionRef)
    If akActionRef == None
        Return
    EndIf
    ; A friendly activate (talk / give) counts as kindness.
    ; TODO(game): narrow this to real gift / dialogue events if you
    ; wire it to a quest -- OnActivate fires for many interactions.
    String sID = akActionRef.GetDisplayName()
    If sID == ""
        sID = "unknown"
    EndIf
    String[] sCats = new String[1]
    sCats[0] = "visitor"
    RecordInteraction(sID, 0.0, 0.5, sCats)
    Think()
EndEvent

Event OnCombatStateChanged(Actor akTarget, Int aiCombatState)
    ; aiCombatState: 0 = not in combat, 1 = in combat, 2 = searching.
    ; Kept as a log hook only -- the ledger itself is fed by OnHit.
    ; TODO(game): use this to switch the NPC's package / aggression
    ; via vanilla SetActorValue / EvaluatePackage if your mod needs it.
    If aiCombatState == 1
        Think()
    EndIf
EndEvent

; ---------------------------------------------------------------------------
; Test helpers (console-safe, vanilla only). Call these from a quest or
; from the in-game console on PC to check the ledger without combat.
; On Xbox there is no console, so wire them to a dialogue / activator
; in your mod if you want a test button in-game.
; ---------------------------------------------------------------------------

Function TestFeed(String asID)
    String[] sCats = new String[1]
    sCats[0] = "kind"
    RecordInteraction(asID, 0.0, 1.0, sCats)
    Think()
    Debug.Notification("BrainKit test: fed " + asID + ". Attitude: " + GetAttitude(asID) + " Mode: " + CurrentMode)
EndFunction

Function TestHurt(String asID)
    String[] sCats = new String[1]
    sCats[0] = "attacker"
    RecordInteraction(asID, 1.0, 0.0, sCats)
    Think()
    Debug.Notification("BrainKit test: hurt by " + asID + ". Attitude: " + GetAttitude(asID) + " Mode: " + CurrentMode)
EndFunction

Function TestStatus(String asID)
    Debug.Notification("BrainKit: " + GetDisplayName() + " mode " + CurrentMode + ", focus " + FocusTarget + ", attitude to " + asID + ": " + GetAttitude(asID))
EndFunction
