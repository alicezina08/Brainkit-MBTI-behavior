// BrainComponent.cpp — Think(): the perceive-decide-act loop.
// Perception and action go through the adapter; everything between is the
// portable core. Stagger Think() across agents (don't run all every tick).
#include "BrainComponent.h"

void UBrainComponent::LoadProfile(const FString& JsonPath) {
    // TODO(game): parse Schema/creature_profile.schema.json into Profile_.
    // Fill traits, taxon, body mass (grams assert lives in BrainProfile),
    // heads, fan multipliers, and memory_config -> Ledger_ half-life/cap.
}

void UBrainComponent::Think(IWorldAdapter* World) {
    if (!World) return;
    World_ = World;
    const double now = World->GameTimeSeconds();

    // 1. PERCEIVE — differentiated, like the player sees.
    TArray<FPerceivedActor> seen = World->QueryPerception();

    // 2. REMEMBER + LEARN — feed stimuli into the ledger (own-action outcomes
    //    arrive here too: the game calls Ledger_.interact for consequences).
    FString focus;
    double bestMag = 0.0;
    for (const FPerceivedActor& a : seen) {
        if (a.ThreatStimulus > 0 || a.KindStimulus > 0) {
            TArray<FString> cats;
            for (const FString& t : a.Tags) cats.Add(t);
            std::vector<std::string> cc;
            for (const FString& t : cats) cc.push_back(TCHAR_TO_UTF8(*t));
            Ledger_.interact(TCHAR_TO_UTF8(*a.Id), a.ThreatStimulus,
                             a.KindStimulus, now, cc);
        }
        double att = Ledger_.attitude(TCHAR_TO_UTF8(*a.Id), now);
        if (FMath::Abs(att) > bestMag) { bestMag = FMath::Abs(att); focus = a.Id; }
    }
    Arousal = (float)bestMag;

    // 3. DECIDE — write blackboard keys; the Behavior Tree owns the actual
    //    animations/movement. Trait vector shapes thresholds (a braver
    //    creature needs more threat before Wary flips to Alarmed).
    // TODO(game): push BK_Attitude_<Id>, BK_FocusTarget, BK_Arousal, BK_Mode
    //    into the owner's BlackboardComponent here.

    // 4. ACT — example policy (replace with your BT):
    //    attitude very negative -> keep distance / call for help (sociability)
    //    attitude positive      -> approach / accept food
    //    neutral + curious      -> investigate stimulus
    // World->ExecuteAction(...) routes into the game's systems.
}
