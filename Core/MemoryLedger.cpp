// MemoryLedger.cpp
#include "MemoryLedger.h"
#include <algorithm>

namespace brainkit {

void MemoryLedger::interact(const std::string& id, double threatDelta,
                            double kindnessDelta, double now,
                            const std::vector<std::string>& cats) {
    MemoryRecord& r = individuals_[id];  // creates if new
    // decay existing before adding, so old + new compose correctly
    double dt = now - r.lastUpdate;
    if (dt > 0 && r.lastUpdate > 0) {
        r.threat   = decayed(r.threat, dt, halfLifeSec_);
        r.kindness = decayed(r.kindness, dt, halfLifeSec_);
    }
    r.threat   += threatDelta;
    r.kindness += kindnessDelta;
    r.lastUpdate = now;
    for (const auto& c : cats) {
        CategoryLesson& l = categories_[c];
        l.category = c;
        l.threat   += threatDelta * genRate_;    // a slice becomes category lore
        l.kindness += kindnessDelta * genRate_;
    }
    enforceCap();
}

double MemoryLedger::attitude(const std::string& id, double now) const {
    auto it = individuals_.find(id);
    if (it == individuals_.end()) return 0.0;
    const MemoryRecord& r = it->second;
    double dt = now - r.lastUpdate;
    double t = dt > 0 ? decayed(r.threat, dt, halfLifeSec_) : r.threat;
    double k = dt > 0 ? decayed(r.kindness, dt, halfLifeSec_) : r.kindness;
    return k - t;
}

double MemoryLedger::categoryAttitude(const std::vector<std::string>& cats,
                                      double now) const {
    (void)now; // categories decay on tick via decay(); kept simple here
    double sum = 0.0;
    for (const auto& c : cats) {
        auto it = categories_.find(c);
        if (it != categories_.end()) sum += it->second.kindness - it->second.threat;
    }
    return sum;
}

void MemoryLedger::decay(double now) {
    for (auto& [id, r] : individuals_) {
        double dt = now - r.lastUpdate;
        if (dt > 0) {
            r.threat   = decayed(r.threat, dt, halfLifeSec_);
            r.kindness = decayed(r.kindness, dt, halfLifeSec_);
            r.lastUpdate = now;
        }
    }
    for (auto& [c, l] : categories_) {
        l.threat   = decayed(l.threat, halfLifeSec_, halfLifeSec_); // one half-life per tick
        l.kindness = decayed(l.kindness, halfLifeSec_, halfLifeSec_);
    }
}

void MemoryLedger::enforceCap() {
    while (individuals_.size() > maxIndividuals_) {
        // evict the most-decayed (least |attitude|) entry — the forgotten
        auto victim = individuals_.begin();
        double best = 1e18;
        for (auto it = individuals_.begin(); it != individuals_.end(); ++it) {
            double mag = std::abs(it->second.threat) + std::abs(it->second.kindness);
            if (mag < best) { best = mag; victim = it; }
        }
        individuals_.erase(victim);
    }
}

} // namespace brainkit
