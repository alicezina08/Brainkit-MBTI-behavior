// BrainProfile.h — portable (no engine deps). Trait vector + allometric sizing.
// Jerison's equation: E = 0.12 * P^0.67, with P in GRAMS. (A pasted snippet
// once passed kilograms — the ~100x error is guarded by the grams assert.)
#pragma once
#include <string>
#include <cmath>
#include <cassert>

namespace brainkit {

enum class TaxonAnchor { Mammal, Reptile, Bird, Insect, Dragon, Undead, Other };

// Typical encephalization quotients by taxon (baseline = 1.0 mammal average).
// Fan-tunable; these are starting points, not measurements.
inline double taxonEQ(TaxonAnchor t) {
    switch (t) {
        case TaxonAnchor::Mammal:  return 1.0;
        case TaxonAnchor::Bird:    return 0.9;   // corvids/parrots higher; tunable
        case TaxonAnchor::Reptile: return 0.25;
        case TaxonAnchor::Insect:  return 0.05;  // ganglia, not a brain — see note
        case TaxonAnchor::Dragon:  return 1.2;   // fan baseline: smart reptile
        case TaxonAnchor::Undead:  return 0.15;  // cortex gone; reflex + residue
        default:                   return 1.0;
    }
}

struct FanMultipliers {
    double sapience = 1.0;  // labeled fan parameter
    double magic    = 1.0;  // labeled fan parameter
    double undeath  = 0.0;  // 0..1, labeled fan parameter
};

struct BrainProfile {
    std::string name;
    TaxonAnchor taxon = TaxonAnchor::Mammal;
    double bodyMassKg = 0.0;      // fan estimate unless provenance says sourced
    bool   massIsFanEstimate = true;
    int    heads = 1;             // >1: central brain + per-head cervical ganglia
    FanMultipliers fan;

    // Personality/behavior parameters, 0..1 (fan interpretation of verified behavior).
    double aggression = 0.5, sociability = 0.5, curiosity = 0.5;
    double fearfulness = 0.5, territoriality = 0.5;

    // Expected brain mass (g) from real allometry. P MUST be grams.
    double jerisonExpectedGrams() const {
        assert(bodyMassKg > 0 && "body mass required");
        const double p_grams = bodyMassKg * 1000.0;
        return 0.12 * std::pow(p_grams, 0.67);
    }
    // Modeled brain mass after taxon EQ + fan multipliers.
    double modeledBrainGrams() const {
        double e = jerisonExpectedGrams() * taxonEQ(taxon)
                 * fan.sapience * fan.magic;
        e *= (1.0 - 0.8 * fan.undeath);  // undeath erodes higher function
        return e;
    }
    // Cognitive budget derived from modeled mass (for the modder to scale
    // memory length, perception radius, planning depth — their call).
    double cognitiveBudget() const {
        // Normalized so a 1kg mammal ~= 1.0. Relative comparisons are the point.
        return modeledBrainGrams() / 12.0;
    }
};

} // namespace brainkit
