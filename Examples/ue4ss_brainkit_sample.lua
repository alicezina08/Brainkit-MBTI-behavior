-- ue4ss_brainkit_sample.lua -- BrainKit UE4SS Lua sample
-- SAMPLE ONLY. Reference scaffold, NOT tested in a live game.
-- Mirrors the C++ BrainKit core (MemoryLedger + BrainProfile) in pure Lua,
-- so a modder can see the idea running in UE4SS without compiling C++.
--
-- What it is:
--   * a MemoryLedger in Lua: threat AND kindness per individual, with
--     forgetting (decay) and generalization (individuals -> categories)
--   * a tiny profile table (goblin sentry example) with traits + memory config
--   * attitude -> mode (Calm / Wary / Alarmed) and a focus target
--   * UE4SS hook points, clearly marked TODO(game)
--
-- What it is NOT:
--   * not a drop-in mod for any specific game. Every game names its damage /
--     interact / perception functions differently, so the hook paths below are
--     PLACEHOLDERS. Replace them with the real class/function paths for your
--     game, then test in-game.
--   * not consciousness, not a neural network, not telemetry. No network,
--     no file writes outside the mod folder, no data leaves the game.
--   * not the C++ plugin. That lives in Core/ + Unreal/. This is the same
--     idea, distilled, so the loop is legible in 30 seconds.
--
-- How to use in UE4SS (v3):
--   1. Put this file in <Game>/Mods/BrainKitSample/Scripts/main.lua
--      (UE4SS loads Scripts/main.lua for each mod folder.)
--   2. Edit PROFILE below for your creature, and the TODO(game) hook paths.
--   3. Launch the game with UE4SS enabled and watch the UE4SS console log.
--
-- Standalone test: run this file in plain Lua/LuaJIT (no UE4SS). The demo
-- at the bottom runs automatically and prints attitudes, so you can check
-- the ledger math without launching a game.

local BrainKit = {}

-- ---------------------------------------------------------------------------
-- Logging: Mod:Log in UE4SS, print anywhere else.
-- ---------------------------------------------------------------------------
local function log(msg)
    if Mod and Mod.Log then
        Mod:Log("[BrainKit] " .. msg)
    else
        print("[BrainKit] " .. msg)
    end
end

-- ---------------------------------------------------------------------------
-- Profile: the same fields as Schema/creature_profile.schema.json, in Lua.
-- Fan-built fields are flagged; nothing here pretends to be measured.
-- ---------------------------------------------------------------------------
local PROFILE = {
    name = "Goblin Sentry",
    kind = "npc",
    taxon_anchor = "other",      -- BrainKit schema value; see Core/BrainProfile.h
    body_mass_kg = 35.0,         -- fan estimate unless provenance says sourced
    traits = {
        aggression = 0.6,
        sociability = 0.4,
        curiosity = 0.5,
        fearfulness = 0.6,
        territoriality = 0.8,
    },
    -- Fan multipliers: labeled fan parameters, NOT measurements.
    fan_multipliers = { sapience = 1.0, magic = 1.0, undeath = 0.0 },
    memory_config = {
        memory_half_life_hours = 24.0,
        generalization_rate = 0.3,
        max_individuals = 64,
    },
    data_provenance = {
        confidence = "fan_estimate",
        sources = { "BrainKit sample profile -- replace with your creature's lore" },
    },
}

-- Jerison's equation, same as C++: E = 0.12 * P^0.67, P in GRAMS.
local function jerison_expected_grams(body_mass_kg)
    local p_grams = body_mass_kg * 1000.0
    assert(p_grams > 0, "body mass must be > 0 (grams assert, cf. BrainProfile.h)")
    return 0.12 * (p_grams ^ 0.67)
end

-- ---------------------------------------------------------------------------
-- MemoryLedger: who did what to me, and what I learned from it.
-- Mirrors Core/MemoryLedger.h/.cpp exactly in shape:
--   interact(id, threat, kindness, now, categories)
--   attitude(id, now) -> threat - kindness, decayed
-- ---------------------------------------------------------------------------
local function new_ledger(cfg)
    cfg = cfg or {}
    local self = {
        half_life_sec = (cfg.memory_half_life_hours or 24.0) * 3600.0,
        gen_rate = cfg.generalization_rate or 0.3,
        max_individuals = cfg.max_individuals or 64,
        individuals = {},   -- id -> { threat, kindness, last_update }
        categories = {},    -- category -> { threat, kindness }
        order = {},         -- insertion order, for cap eviction (oldest first)
    }

    local function decayed(value, dt_sec, half_life_sec)
        if dt_sec <= 0 then return value end
        return value * (0.5 ^ (dt_sec / half_life_sec))
    end

    function self:interact(id, threat_delta, kindness_delta, now, cats)
        local r = self.individuals[id]
        if not r then
            r = { threat = 0.0, kindness = 0.0, last_update = 0.0 }
            self.individuals[id] = r
            table.insert(self.order, id)
            -- Cap eviction: oldest decayed entries go first.
            while #self.order > self.max_individuals do
                local oldest = table.remove(self.order, 1)
                self.individuals[oldest] = nil
            end
        end
        local dt = now - r.last_update
        if dt > 0 and r.last_update > 0 then
            r.threat = decayed(r.threat, dt, self.half_life_sec)
            r.kindness = decayed(r.kindness, dt, self.half_life_sec)
        end
        r.threat = r.threat + (threat_delta or 0.0)
        r.kindness = r.kindness + (kindness_delta or 0.0)
        r.last_update = now
        -- A slice of every lesson generalizes to its categories.
        for _, c in ipairs(cats or {}) do
            local l = self.categories[c]
            if not l then l = { threat = 0.0, kindness = 0.0 } self.categories[c] = l end
            l.threat = l.threat + (threat_delta or 0.0) * self.gen_rate
            l.kindness = l.kindness + (kindness_delta or 0.0) * self.gen_rate
        end
    end

    function self:attitude(id, now)
        local r = self.individuals[id]
        if not r then return 0.0 end
        local dt = now - r.last_update
        local t = r.threat
        local k = r.kindness
        if dt > 0 and r.last_update > 0 then
            t = decayed(t, dt, self.half_life_sec)
            k = decayed(k, dt, self.half_life_sec)
        end
        -- Threat is negative, kindness is positive. Same sign as C++.
        return k - t
    end

    function self:category_attitude(category)
        local l = self.categories[category]
        if not l then return 0.0 end
        return l.kindness - l.threat
    end

    return self
end

BrainKit.new_ledger = new_ledger
BrainKit.PROFILE = PROFILE
BrainKit.jerison_expected_grams = jerison_expected_grams

-- ---------------------------------------------------------------------------
-- Think: attitude -> mode. Trait vector shapes the thresholds (a braver
-- creature needs more threat before Wary flips to Alarmed).
-- Returns: mode ("Calm" / "Wary" / "Alarmed"), focus_id, arousal
-- ---------------------------------------------------------------------------
local function think(ledger, seen, now)
    -- seen: array of { id = "player:Alice", tags = {"player","red_armor"} }
    local focus = nil
    local best_mag = 0.0
    for _, actor in ipairs(seen or {}) do
        local att = ledger:attitude(actor.id, now)
        -- A brand-new category lesson can also colour a stranger:
        -- e.g. red_armor was threatening before, even if THIS person is new.
        for _, tag in ipairs(actor.tags or {}) do
            local cat_att = ledger:category_attitude(tag)
            if math.abs(cat_att) > math.abs(att) then att = cat_att end
        end
        if math.abs(att) > best_mag then
            best_mag = math.abs(att)
            focus = actor.id
        end
    end
    local fear = PROFILE.traits.fearfulness or 0.5
    local brave = PROFILE.traits.aggression or 0.5
    -- Fearful creatures alarm sooner; aggressive ones tolerate more.
    local wary_at = 0.5 + (brave - fear) * 0.3
    local alarm_at = 1.5 + (brave - fear) * 0.5
    local mode = "Calm"
    if best_mag >= alarm_at then mode = "Alarmed"
    elseif best_mag >= wary_at then mode = "Wary" end
    return mode, focus, best_mag
end

BrainKit.think = think

-- ---------------------------------------------------------------------------
-- UE4SS wiring (only runs inside UE4SS; skipped in plain Lua).
-- TODO(game): replace every placeholder path below with the real
-- class/function paths for YOUR game. These are examples of the SHAPE
-- of a hook, not working paths for any shipped game.
-- ---------------------------------------------------------------------------
local ledger = new_ledger(PROFILE.memory_config)
BrainKit.ledger = ledger

if RegisterHook then
    log("BrainKit sample loaded for " .. PROFILE.name
        .. " | Jerison expected brain: "
        .. string.format("%.1f", jerison_expected_grams(PROFILE.body_mass_kg))
        .. " g (fan estimate input)")

    -- TODO(game): damage hook. Replace with your game's damage function,
    -- e.g. "/Script/Engine.Actor:ReceiveAnyDamage" is a generic example only.
    -- The hook must call ledger:interact(attacker_id, threat, 0, now, tags).
    -- RegisterHook("/Script/Engine.Actor:ReceiveAnyDamage", function(self, DamagedActor, Damage, DamageType, InstigatedBy, DamageCauser)
    --     -- TODO(game): resolve InstigatedBy to a stable individual id + tags.
    -- end)

    -- TODO(game): kindness hook. Replace with your game's give/food/spare
    -- interaction. Same ledger call, kindness side:
    -- ledger:interact(actor_id, 0, kindness, now, tags)

    -- TODO(game): per-tick think. LoopAsync runs off the game thread;
    -- keep Think() cheap, or stagger it across NPCs (don't run all every tick).
    -- if LoopAsync then
    --     LoopAsync(1000, function()
    --         -- TODO(game): build `seen` from your game's perception system,
    --         -- then: local mode, focus, arousal = think(ledger, seen, os.time())
    --         -- and write mode/focus to your Behavior Tree blackboard.
    --         return false -- return true to stop the loop; false keeps it going
    --     end)
    -- end

    log("BrainKit sample: hooks are placeholders -- edit the TODO(game) lines, then test in-game.")
else
    -- -----------------------------------------------------------------------
    -- Standalone demo (plain Lua, no UE4SS): proves the ledger math.
    -- -----------------------------------------------------------------------
    local now = 1000000.0
    ledger:interact("player:Alice", 0.0, 1.0, now, { "player", "kind" })
    ledger:interact("player:Bob", 2.0, 0.0, now, { "player", "red_armor" })
    local mode, focus, arousal = think(ledger, {
        { id = "player:Alice", tags = { "player" } },
        { id = "player:Bob", tags = { "player", "red_armor" } },
    }, now)
    log("Demo: Alice attitude = " .. string.format("%.2f", ledger:attitude("player:Alice", now))
        .. " (kind) | Bob attitude = " .. string.format("%.2f", ledger:attitude("player:Bob", now))
        .. " (threat) | red_armor category = " .. string.format("%.2f", ledger:category_attitude("red_armor")))
    log("Demo: mode=" .. mode .. " focus=" .. tostring(focus)
        .. " arousal=" .. string.format("%.2f", arousal))
    log("Demo: Jerison expected brain for "
        .. PROFILE.body_mass_kg .. " kg = "
        .. string.format("%.1f", jerison_expected_grams(PROFILE.body_mass_kg)) .. " g")
    log("Standalone demo done. In UE4SS, the demo is skipped and the hooks above run instead.")
end

return BrainKit
