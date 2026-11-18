// BrainComponent.h — the thin Unreal glue. THIS is the game-specific part.
// The portable core (brainkit::) does the thinking; this component feeds it
// perception and executes its decisions via the game's own AI systems
// (Behavior Tree + Blackboard + AI Perception).
//
// NOTE: reference scaffold — compile against your engine version and test.
#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "BrainProfile.h"
#include "MemoryLedger.h"
#include "BrainComponent.generated.h"

// ---- Adapter interfaces: the ONLY code a modder writes per game ----
class IWorldAdapter {
public:
    virtual ~IWorldAdapter() = default;
    // List nearby perceivable actors with differentiated tags, e.g.
    // {"player:Alice","kind:player","armor:red","faction:none"}
    virtual TArray<FPerceivedActor> QueryPerception() = 0;
    // Execute one chosen action through the game's systems.
    virtual void ExecuteAction(const FString& ActionId,
                               const FString& TargetId) = 0;
    virtual double GameTimeSeconds() = 0;
};

struct FPerceivedActor {
    FString Id;                 // stable individual id ("player:Alice")
    TArray<FString> Tags;       // differentiated categories
    float ThreatStimulus = 0.f; // this-tick stimuli (damage, loud noise...)
    float KindStimulus = 0.f;   // ...or kindness (food offered, spared)
};

UCLASS(ClassGroup=(BrainKit), meta=(BlueprintSpawnableComponent))
class BRAINKIT_API UBrainComponent : public UActorComponent {
    GENERATED_BODY()
public:
    // Load from the app's exported JSON (see Schema/).
    UFUNCTION(BlueprintCallable, Category="BrainKit")
    void LoadProfile(const FString& JsonPath);

    // Call every tick (or on a staggered budget): perceive -> update memory ->
    // choose action -> write blackboard keys the Behavior Tree reads.
    UFUNCTION(BlueprintCallable, Category="BrainKit")
    void Think(IWorldAdapter* World);

    // Blackboard keys this component maintains for the Behavior Tree:
    //   BK_Attitude_<Id> (float), BK_FocusTarget (string),
    //   BK_Arousal (float: threat+kindness magnitude), BK_Mode (Calm/Wary/Alarmed)
    UPROPERTY(BlueprintReadOnly, Category="BrainKit")
    float Arousal = 0.f;

private:
    brainkit::BrainProfile Profile_;
    brainkit::MemoryLedger Ledger_;
    IWorldAdapter* World_ = nullptr;
};
