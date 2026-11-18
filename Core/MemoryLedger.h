// MemoryLedger.h — portable. Who did what to me, and what I learned from it.
// Threat AND kindness per individual, with forgetting (decay) and
// generalization (individuals -> categories). This is associative memory —
// the same mechanism as real animal conditioning — not understanding.
#pragma once
#include <string>
#include <unordered_map>
#include <vector>
#include <cmath>

namespace brainkit {

struct MemoryRecord {
    double threat   = 0.0;  // accumulated threat (attacked me, threatened pack)
    double kindness = 0.0;  // accumulated kindness (fed me, spared me)
    double lastUpdate = 0.0; // seconds since epoch (game clock)
};

struct CategoryLesson {
    std::string category;   // e.g. "red_armor", "goblin", "loud_noises"
    double threat = 0.0, kindness = 0.0;
};

class MemoryLedger {
public:
    MemoryLedger(double halfLifeHours = 24.0,
                 double generalizationRate = 0.3,
                 size_t maxIndividuals = 64)
        : halfLifeSec_(halfLifeHours * 3600.0),
          genRate_(generalizationRate), maxIndividuals_(maxIndividuals) {}

    // Record an interaction with a specific individual. Positive threat for
    // harm, positive kindness for help. Category tags let it generalize.
    void interact(const std::string& individualId, double threatDelta,
                  double kindnessDelta, double nowSec,
                  const std::vector<std::string>& categories = {});

    // Net attitude toward an individual: +kind .. -threat, decayed to now.
    // >0 approach/warm, <0 avoid/hostile, ~0 neutral.
    double attitude(const std::string& individualId, double nowSec) const;

    // For brand-new individuals: what do their categories predict?
    double categoryAttitude(const std::vector<std::string>& categories,
                            double nowSec) const;

    void decay(double nowSec);   // apply forgetting curve to everything
    void clear() { individuals_.clear(); categories_.clear(); }
    size_t size() const { return individuals_.size(); }

private:
    static double decayed(double v, double dt, double halfLife) {
        return v * std::pow(0.5, dt / halfLife);
    }
    void enforceCap();

    std::unordered_map<std::string, MemoryRecord> individuals_;
    std::unordered_map<std::string, CategoryLesson> categories_;
    double halfLifeSec_, genRate_;
    size_t maxIndividuals_;
};

} // namespace brainkit
