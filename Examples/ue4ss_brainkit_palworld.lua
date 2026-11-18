-- ue4ss_brainkit_palworld.lua -- BrainKit for Palworld (UE4SS Lua sample)
-- PALWORLD-SPECIFIC SAMPLE. Reference scaffold, NOT tested in a live game.
-- Palworld 1.0 (Steam) + UE4SS Palworld fork (Okaetsu build) + PalSchema.
--
-- Why Palworld first: it already has a live UE4SS mod scene on Nexus Mods,
-- and RuneScape: Dragonwilds official mod support is still on Jagex's 2027
-- roadmap, so Alice is waiting on that one. Palworld is the place to try
-- BrainKit in a real Unreal game today.
--
-- What this does (same BrainKit idea as the generic sample, Palworld-shaped):
--   * MemoryLedger in Lua: threat AND kindness per individual, decay
--     (24h half-life), generalization to categories (e.g. "red_armor")
--   * attitude -> mode Calm / Wary / Alarmed, with a focus target
--   * Palworld init pattern used by working Palworld mods: hook
--     ServerAcknowledgePossession / ClientRestart, then NotifyOnNewObject
--     for pals, with RETRY -- Blueprint pal classes only exist once a
--     player has spawned, so a boot-time hook can fail and must be retried.
--   * Chat commands: type in Palworld chat to feed the ledger by hand
--     (!brainkit feed, !brainkit hurt, !brainkit status) -- a safe,
--     testable way to see the brain react without relying on damage hooks.
--   * Damage hook ATTEMPTED with candidates + pcall + logging, never a
--     hard crash if the function is not found.
--
-- HONEST LIMITS (read before using -- these come from real Palworld mods):
--   1. Pal damage routing differs by mode. One Nexus damage mod reports
--      player-owned Pal damage is hookable on a DEDICATED SERVER only;
--      in single-player / player-hosted co-op the game applies Pal damage
--      natively in C++, which UE4SS Lua hooks cannot intercept. Player
--      damage hooks DO work in single-player in other mods. So: do not
--      assume a damage hook fires for every Pal in every mode. This
--      sample logs when a hook fails, and the chat commands always work
--      as a fallback so you can still see the ledger react.
--   2. Game updates break hooks. If Palworld updates and a function path
--      changes, this script logs "hook not available" and keeps running;
--      it never crashes the game on a missing hook.
--   3. Hook paths below that are marked VERIFIED are paths seen in
--      working Palworld mods / tutorials (see header notes). Paths marked
--      CANDIDATE are best-effort guesses to try in order -- they may not
--      exist in 1.0. Never present a candidate as verified.
--   4. Not consciousness, not a neural network, not telemetry. No network,
--      no save edits, nothing written to your world settings.
--
-- Install (Palworld 1.0, Windows, Steam):
--   1. Install the UE4SS Palworld fork (Okaetsu build) into Palworld/
--      (PalSchema optional, recommended by most Palworld Lua mods).
--   2. Put this file at:
--      Palworld/Pal/Binaries/Win64/ue4ss/Mods/BrainKitPal/Scripts/main.lua
--      and enable it in ue4ss Mods (enabled.txt / mods.txt, per your
--      UE4SS version).
--   3. Launch Palworld, load a world, watch the UE4SS console log.
--
-- Standalone test: run this file in plain Lua/LuaJIT (no UE4SS). The demo
-- at the bottom runs automatically and prints attitudes, so you can check
-- the ledger math without launching Palworld.

local BrainKitPal = {}

local function log(msg)
    if Mod and Mod.Log then Mod:Log("[BrainKitPal] " .. msg)
    else print("[BrainKitPal] " .. msg) end
end

-- ---------------------------------------------------------------------------
-- Profile: Anubis, from Alice's Palworld Team Builder dex.
-- Traits are the lore-based MBTI heuristic (fan interpretation, as always).
-- Body mass is a FAN ESTIMATE unless provenance says sourced -- do not
-- present it as measured. Jerison math is real; the input is approximate.
-- ---------------------------------------------------------------------------
local PROFILE = {
    name = "Anubis",
    kind = "creature",
    taxon_anchor = "mammal",
    body_mass_kg = 85.0, -- fan estimate
    traits = {
        aggression = 0.6, sociability = 0.5, curiosity = 0.5,
        fearfulness = 0.4, territoriality = 0.7,
    },
    fan_multipliers = { sapience = 1.0, magic = 0.0, undeath = 0.0 },
    memory_config = {
        memory_half_life_hours = 24.0,
        generalization_rate = 0.3,
        max_individuals = 64,
    },
    data_provenance = {
        confidence = "fan_estimate",
        sources = { "Palworld Team Builder dex -- Anubis entry, lore-based" },
    },
}

local function jerison_expected_grams(body_mass_kg)
    local p_grams = body_mass_kg * 1000.0
    assert(p_grams > 0, "body mass must be > 0 (grams assert)")
    return 0.12 * (p_grams ^ 0.67)
end

-- ---------------------------------------------------------------------------
-- MemoryLedger (same shape as Core/MemoryLedger.h/.cpp, in Lua)
-- ---------------------------------------------------------------------------
local function new_ledger(cfg)
    cfg = cfg or {}
    local self = {
        half_life_sec = (cfg.memory_half_life_hours or 24.0) * 3600.0,
        gen_rate = cfg.generalization_rate or 0.3,
        max_individuals = cfg.max_individuals or 64,
        individuals = {}, categories = {}, order = {},
    }
    local function decayed(v, dt, hl)
        if dt <= 0 then return v end
        return v * (0.5 ^ (dt / hl))
    end
    function self:interact(id, threat_delta, kindness_delta, now, cats)
        local r = self.individuals[id]
        if not r then
            r = { threat = 0.0, kindness = 0.0, last_update = 0.0 }
            self.individuals[id] = r
            table.insert(self.order, id)
            while #self.order > self.max_individuals do
                self.individuals[table.remove(self.order, 1)] = nil
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
        local t, k = r.threat, r.kindness
        if dt > 0 and r.last_update > 0 then
            t = decayed(t, dt, self.half_life_sec)
            k = decayed(k, dt, self.half_life_sec)
        end
        return k - t
    end
    function self:category_attitude(category)
        local l = self.categories[category]
        if not l then return 0.0 end
        return l.kindness - l.threat
    end
    return self
end

local function think(ledger, seen, now)
    local focus, best_mag = nil, 0.0
    for _, actor in ipairs(seen or {}) do
        local att = ledger:attitude(actor.id, now)
        for _, tag in ipairs(actor.tags or {}) do
            local cat_att = ledger:category_attitude(tag)
            if math.abs(cat_att) > math.abs(att) then att = cat_att end
        end
        if math.abs(att) > best_mag then best_mag, focus = math.abs(att), actor.id end
    end
    local fear = PROFILE.traits.fearfulness or 0.5
    local brave = PROFILE.traits.aggression or 0.5
    local wary_at = 0.5 + (brave - fear) * 0.3
    local alarm_at = 1.5 + (brave - fear) * 0.5
    local mode = "Calm"
    if best_mag >= alarm_at then mode = "Alarmed"
    elseif best_mag >= wary_at then mode = "Wary" end
    return mode, focus, best_mag
end

BrainKitPal.new_ledger = new_ledger
BrainKitPal.PROFILE = PROFILE
BrainKitPal.think = think
BrainKitPal.jerison_expected_grams = jerison_expected_grams

local ledger = new_ledger(PROFILE.memory_config)
BrainKitPal.ledger = ledger

-- ---------------------------------------------------------------------------
-- Palworld chat commands -- the safe, always-works way to feed the ledger.
-- In Palworld chat type:  !brainkit feed | !brainkit hurt | !brainkit status
-- VERIFIED hook path (seen in working Palworld mods/tutorials):
--   /Script/Pal.PalGameStateInGame:BroadcastChatMessage
-- ---------------------------------------------------------------------------
local function handle_chat(message, now)
    now = now or os.time()
    if message == "!brainkit feed" then
        ledger:interact("player:you", 0.0, 1.0, now, { "player", "kind" })
        log("Chat: fed Anubis (+1 kindness from you). Attitude now "
            .. string.format("%.2f", ledger:attitude("player:you", now)))
        return true
    elseif message == "!brainkit hurt" then
        ledger:interact("player:you", 1.0, 0.0, now, { "player" })
        log("Chat: hurt Anubis (+1 threat from you). Attitude now "
            .. string.format("%.2f", ledger:attitude("player:you", now)))
        return true
    elseif message == "!brainkit status" then
        local mode, focus, arousal = think(ledger, {
            { id = "player:you", tags = { "player" } },
        }, now)
        log("Chat: Anubis mode=" .. mode .. " focus=" .. tostring(focus)
            .. " arousal=" .. string.format("%.2f", arousal)
            .. " your attitude=" .. string.format("%.2f", ledger:attitude("player:you", now)))
        return true
    end
    return false
end
BrainKitPal.handle_chat = handle_chat

-- ---------------------------------------------------------------------------
-- UE4SS wiring (Palworld). Skipped in plain Lua -- demo runs instead.
-- Hook registration uses pcall + RETRY, per the Palworld-Bridge lesson:
-- Blueprint pal classes only exist once a player has spawned, so a
-- boot-time registration can fail and must be retried, never given up on
-- after one attempt, and never allowed to crash the game.
-- ---------------------------------------------------------------------------
if RegisterHook then
    log("BrainKitPal loaded for " .. PROFILE.name
        .. " | Jerison expected brain: "
        .. string.format("%.1f", jerison_expected_grams(PROFILE.body_mass_kg))
        .. " g (fan-estimate input)")

    local hooked = {}
    local function try_hook(label, path, handler)
        if hooked[label] then return true end
        local ok, err = pcall(function() RegisterHook(path, handler) end)
        if ok then
            hooked[label] = true
            log("Hook OK: " .. label .. " (" .. path .. ")")
            return true
        else
            log("Hook not available (will retry): " .. label .. " (" .. path .. ") -- " .. tostring(err))
            return false
        end
    end

    local function register_all_hooks()
        -- VERIFIED: chat hook, seen in working Palworld mods/tutorials.
        try_hook("chat", "/Script/Pal.PalGameStateInGame:BroadcastChatMessage",
            function(self, ChatMessage)
                local ok, chat = pcall(function() return ChatMessage:get() end)
                if not ok or not chat then return end
                local ok2, msg = pcall(function() return chat.Message:ToString() end)
                if ok2 and msg then handle_chat(msg, os.time()) end
            end)
        -- VERIFIED (example from a working Palworld Lua mod): level-up hook.
        -- PalMonsterCharacter:MasterWazaUpdateWhenLevelUp fires when a Pal
        -- levels up. Here it only logs -- a real mod could feed it to the
        -- ledger as a "grew stronger" event. Do not invent effects for it.
        try_hook("levelup", "/Script/Pal.PalMonsterCharacter:MasterWazaUpdateWhenLevelUp",
            function(self)
                log("Level-up seen (PalMonsterCharacter). Ledger unchanged -- hook is a placeholder for growth events.")
            end)
        -- CANDIDATE: generic Unreal damage hook. May fire for player
        -- damage in single-player; Pal damage on a dedicated server only
        -- (see header limits). If it does not exist / does not fire, the
        -- pcall logs it and the chat commands still work.
        try_hook("damage", "/Script/Engine.Actor:ReceiveAnyDamage",
            function(self, DamagedActor, Damage, DamageType, InstigatedBy, DamageCauser)
                log("Damage hook fired (candidate). TODO(game): resolve InstigatedBy to a stable id + tags, then ledger:interact(id, threat, 0, os.time(), tags).")
            end)
    end

    local function init_once()
        -- VERIFIED pattern: hook possession / restart, wait, then register.
        -- NotifyOnNewObject for pals, when the class exists.
        if NotifyOnNewObject then
            local ok, err = pcall(function()
                NotifyOnNewObject("/Script/Pal.PalMonsterCharacter", function(ctx)
                    log("PalMonsterCharacter spawned -- BrainKitPal watching.")
                end)
            end)
            if not ok then log("NotifyOnNewObject for PalMonsterCharacter not ready yet: " .. tostring(err)) end
        end
        register_all_hooks()
        -- Retry loop: every 10s for 5 minutes, until all hooks land.
        -- (Palworld-Bridge used 30 x 10s; same idea, shorter here.)
        if LoopAsync then
            local attempts = 0
            LoopAsync(10000, function()
                attempts = attempts + 1
                register_all_hooks()
                if hooked.chat and hooked.levelup then return true end -- stop loop
                if attempts >= 30 then
                    log("Hook retry gave up after 30 attempts -- chat/levelup still missing. Check UE4SS version + Palworld version.")
                    return true
                end
                return false
            end)
        end
    end

    -- VERIFIED init hooks (used by working Palworld mods):
    -- ServerAcknowledgePossession + ClientRestart, with a short delay so
    -- the world exists before we try to register anything.
    local inited = false
    local function init_guarded()
        if inited then return end
        inited = true
        if ExecuteWithDelay then
            ExecuteWithDelay(5000, function() init_once() end)
        else
            init_once()
        end
    end
    try_hook("possession", "/Script/Engine.PlayerController:ServerAcknowledgePossession", function() init_guarded() end)
    try_hook("restart", "/Script/Engine.PlayerController:ClientRestart", function() init_guarded() end)
    -- If neither init hook ever fires (e.g. already in-world on load),
    -- fall back to a delayed direct init.
    if ExecuteWithDelay then ExecuteWithDelay(8000, function() init_guarded() end) end

    log("BrainKitPal: waiting for player possession to init hooks. Chat: !brainkit feed / hurt / status")
else
    -- -----------------------------------------------------------------------
    -- Standalone demo (plain Lua, no UE4SS)
    -- -----------------------------------------------------------------------
    local now = 1000000.0
    ledger:interact("player:you", 0.0, 1.0, now, { "player", "kind" })
    handle_chat("!brainkit status", now)
    handle_chat("!brainkit hurt", now)
    handle_chat("!brainkit hurt", now)
    handle_chat("!brainkit status", now)
    log("Demo: Jerison expected brain for " .. PROFILE.body_mass_kg .. " kg = "
        .. string.format("%.1f", jerison_expected_grams(PROFILE.body_mass_kg)) .. " g")
    log("Standalone demo done. In Palworld + UE4SS, the demo is skipped and the hooks above run instead.")
end

return BrainKitPal
