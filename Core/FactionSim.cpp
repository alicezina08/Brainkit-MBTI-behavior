// FactionSim.cpp — deterministic-ish tick (seeded) so worlds stay reproducible.
#include "FactionSim.h"
#include <random>

namespace brainkit {

std::vector<FactionEvent> FactionSim::tick(double dtMinutes, unsigned seed) {
    std::vector<FactionEvent> events;
    if (factions_.size() < 2) return events;
    std::mt19937 rng(seed);
    std::uniform_real_distribution<double> u(0.0, 1.0);

    // For each territory, neighbors contest it. Keep it legible, not "smart".
    for (auto& [tid, terr] : territories_) {
        // pick a challenger: any faction != controller, weighted by strength
        double total = 0.0;
        for (auto& [fn, f] : factions_) if (fn != terr.controller) total += f.strength;
        if (total <= 0) continue;
        double roll = u(rng) * total, acc = 0.0;
        std::string challenger;
        for (auto& [fn, f] : factions_) {
            if (fn == terr.controller) continue;
            acc += f.strength;
            if (roll <= acc) { challenger = fn; break; }
        }
        if (challenger.empty()) continue;

        double atk = factions_[challenger].strength * (0.6 + 0.8 * u(rng));
        double def = terr.controller.empty() ? 0.2
                     : factions_[terr.controller].strength * (0.6 + 0.8 * u(rng));
        // slow clock: contests are rare per tick
        if (u(rng) < 0.02 * dtMinutes && atk > def * 1.2) {
            std::string prev = terr.controller;
            terr.controller = challenger;
            terr.danger = std::min(1.0, terr.danger + 0.15);
            factions_[challenger].morale = std::min(1.0, factions_[challenger].morale + 0.1);
            if (!prev.empty()) factions_[prev].morale = std::max(0.0, factions_[prev].morale - 0.1);
            events.push_back({"[" + challenger + " seized " + tid + " from " +
                              (prev.empty() ? "no one" : prev) + "]", tid});
        } else {
            terr.danger = std::max(0.0, terr.danger - 0.005 * dtMinutes); // quiet areas calm down
        }
    }
    return events;
}

void FactionSim::setAllegiance(const std::string& id, const std::string& faction) {
    if (factions_.count(faction)) allegiance_[id] = faction;
}

std::string FactionSim::allegianceOf(const std::string& id) const {
    auto it = allegiance_.find(id);
    return it == allegiance_.end() ? "" : it->second;
}

const Territory* FactionSim::territory(const std::string& id) const {
    auto it = territories_.find(id);
    return it == territories_.end() ? nullptr : &it->second;
}

} // namespace brainkit
