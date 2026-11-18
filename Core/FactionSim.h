// FactionSim.h — portable. Collective dynamics on a slow tick.
// Factions recruit, lose members, and contest territory WITHOUT the player.
// Runs abstracted (tick-based), never per-frame: this is the honest perf note.
#pragma once
#include <string>
#include <unordered_map>
#include <vector>

namespace brainkit {

struct Faction {
    std::string name;
    double strength = 1.0;      // abstract power; drives contest outcomes
    double morale   = 0.5;      // 0..1; losses sap it, wins restore it
};

struct Territory {
    std::string id;             // region id, e.g. "fractured_plains"
    std::string controller;     // faction name ("" = unclaimed)
    double danger = 0.5;        // 0..1 — what the player feels walking in
};

struct FactionEvent {
    std::string description;    // human-readable log for the player to stumble on
    std::string territoryId;
};

class FactionSim {
public:
    void addFaction(const Faction& f) { factions_[f.name] = f; }
    void addTerritory(const Territory& t) { territories_[t.id] = t; }

    // One slow tick (e.g. every 5 in-game minutes). Returns events the game
    // can surface: battles, takeovers, recruitment drives.
    std::vector<FactionEvent> tick(double dtMinutes, unsigned seed);

    // An individual changes allegiance (recruitment/defection). The game
    // decides the trigger; the sim records the consequence.
    void setAllegiance(const std::string& individualId,
                       const std::string& factionName);

    std::string allegianceOf(const std::string& individualId) const;
    const Territory* territory(const std::string& id) const;

private:
    std::unordered_map<std::string, Faction> factions_;
    std::unordered_map<std::string, Territory> territories_;
    std::unordered_map<std::string, std::string> allegiance_; // individual -> faction
};

} // namespace brainkit
