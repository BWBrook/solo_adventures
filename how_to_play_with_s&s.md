# How to Play These Conversions with Sinew & Steel

This coda is for an AI Custodian running the converted adventures in this
archive with Sinew & Steel, especially the Candlelight Dungeons skin. Treat the
converted Markdown files as narrative modules: they give you places, people,
choices, clues, factions, dangers, and branching structure. They do not bring
their original D&D rules with them.

The aim is not to reproduce a 4e encounter in another engine. The aim is to
use the adventure fiction as a torchlit seed for S&S play: concrete scenes,
real choices, dangerous thresholds, talkative monsters, ugly bargains, and
consequences that stay on the page.

## Load Order for an AI Custodian

When preparing a session, read or load these in order:

1. The Sinew & Steel quickstart or assembled agent prompt.
2. `skins/candlelight_dungeons.md`.
3. `skins/candlelight_delvekit.md` and the Delvekit quick reference if the
   dungeon map, route choices, keys, revisits, light, and time pressure matter.
4. One converted adventure from this archive.
5. Any campaign state, current character sheet, trackers, and prior session
   memory.

For agent-harness play from the S&S repo, Candlelight prompt builds already
pull in the Delvekit sidecar. A typical setup might use `candlelight_dungeons`
as the skin and treat the converted adventure as hidden scenario material:

```bash
python tools/campaign_init.py --title "Winterhaven" --skin candlelight_dungeons --tone standard
python tools/build_prompt.py --campaign winterhaven --mode agent \
  --hidden /Users/bwbrook/games/solo_adventures/converted/Keep_on_the_Shadowfell_H1.md
```

Use the exact generated campaign slug if it differs. Keep the adventure text
behind the screen unless the player asks for a public handout.

## The Conversion Contract

Keep these things from the converted adventure:

- Numbered choose-your-own-adventure entries and named area labels.
- The order of clues, revelations, and consequences.
- Named NPCs, places, factions, grudges, secrets, promises, and fears.
- Traps, obstacles, riddles, strange rooms, and environmental details.
- Story-significant treasure, relics, maps, letters, symbols, and rumors.
- Branching outcomes: escape, capture, alliance, retreat, discovery, failure.
- The adventure's mood and pacing.

Discard these things even if they linger in a source text:

- D&D levels, XP, encounter budgets, challenge ratings, skill DCs, powers, and
  tactical assumptions.
- Monster stat blocks, monster roles, hit points, armor class, defenses, and
  recharge mechanics.
- Grid positioning, forced movement jargon, squares, bursts, slides, pushes,
  marks, action types, and initiative procedures.
- Treasure parcels and magic item math as balance instruments.
- Any idea that combat must happen because the original module expected it.

If a branch says "if you succeed", S&S decides the success. If a room once had
a balanced encounter, Candlelight asks what the room wants, what the monsters
want, what the player can learn, and what danger is visible before it bites.

## Core S&S Discipline

Use the S&S loop every beat:

1. Frame the fiction with concrete, sensory details.
2. Ask for intent and method: "What do you do, and how?"
3. Decide whether a roll is needed.
4. If a roll is needed, state the stakes before rolling.
5. Resolve with no roll, a roll-under test, or an opposed test.
6. Apply consequences immediately to Stamina, Fortune, Fatigue, clocks, map
   state, NPC behavior, or inventory.
7. End with a hook and 2-4 options, while allowing freeform action.

Do not roll by default. Roll only when the outcome is uncertain and it matters.
If a careful approach plainly works, let it work. If failure would be boring,
use "yes, but" or "no, but" instead of inventing a check.

When a roll is needed in Candlelight Dungeons, use the skin labels:

- **STR** for force, endurance, grappling, hauling, and breaking.
- **DEX** for stealth, climbing, dodging, missile aim, locks, and traps.
- **LOR** for occult study, riddles, spellcraft, old history, and weird
  mechanisms.
- **FTH** for nerve, vows, morale, divine petition, trust, and turning undead.
- **FOR** for sheer chance and the Fortune token pool.

Fortune tokens can nudge rolls, but natural 1 and natural 20 are locked.
Fatigue is the Candlelight pressure fuse. Use it for forced marches, failed
spells, bad wounds, wrong turns, costly shortcuts, and time spent under threat.

## Preserving Numbered Branches

The numbered structure matters because it gives solo play a strong procedural
shape. Keep it, but do not become trapped by it.

Use entry numbers as stable handles:

- "You are in entry 27 of Ghost Tower."
- "This freeform plan most closely points to entry 31."
- "The fiction has skipped the original success branch; continue from entry
  44 with altered consequences."

The player can always choose an action that is not listed. When that happens:

1. Resolve the action using S&S.
2. Jump to the closest matching entry if one exists.
3. If no entry fits, improvise a short bridge scene.
4. Return to the numbered structure when the next obvious branch appears.

Never force a listed option just because the conversion lists it. The entries
are a navigation aid, not a prison.

## Turning D&D Prompts into S&S Rulings

Use these translations at the table:

| Original prompt | Candlelight handling |
|---|---|
| Skill check or DC | Ask intent and method. If risk matters, choose STR, DEX, LOR, FTH, or FOR. Use Advantage for smart preparation and Disadvantage for haste, darkness, bad tools, or injury. |
| Monster encounter | Give the creature a motive, a visible sign, a likely reaction, and only enough tier/Stamina/edge/soak to resolve danger if dice become necessary. |
| Trap | Telegraph it. Let caution matter. If rushed or mishandled, cost Stamina, gear, position, time, Fatigue, separation, or in rare cases a direct drop to 0 Stamina. |
| Puzzle | Describe the mechanism plainly. Seed clues nearby. Let good reasoning work without a roll. Use one risky test at most for shortcuts. |
| Locked door or gate | If the party has the key, phrase, sigil, or leverage, open it. Roll only for risky force, rushed lockwork, or tampering under pressure. |
| Spell or ritual | Treat it as a Candlelight Cantrip, Spell, Greater Spell, or Arcanum. Apply Fortune/Fatigue costs and backlash. |
| Treasure parcel | Keep only treasure that changes choices: relics, letters, maps, favors, holy signs, leverage, strange tools, or loot that funds the next delve. |
| XP reward | Replace with milestones after 3-4 perilous beats and a narrative boon. |

For NPCs and monsters, the Custodian's Almanac gives a fast tier scale:
Peasant 8, Soldier 10, Elite 12, Monster 14, Nemesis 16. Most converted
creatures only need one tier number, a Stamina value, edge, soak, and one vivid
behavior. Many need no numbers at all until someone risks a roll against them.

## Threat Tiers for Converted Modules

Do not rebuild a D&D bestiary. Make a creature card only when a roll, fight,
chase, parley, or serious resistance is likely. Use the S&S tier method:

| Source-fiction role | S&S treatment |
|---|---|
| Frightened townsfolk, prisoners, exhausted hirelings | **Peasant 8**, Stamina 3, edge 0, soak 0. |
| Ordinary guards, goblins, kobolds, skeletons, bandits | **Soldier 10**, Stamina 4, edge 0 or +1, soak 0-1. |
| Captains, priests, dangerous scouts, named lieutenants | **Elite 12**, Stamina 5, edge +1, soak 1-2. |
| Large beasts, animated guardians, ogre corpses, young dragons | **Monster 14**, Stamina 6, usually +2 if large, edge +2, soak 1-2. |
| Adventure villains, undead blackguards, ritual masters | **Nemesis 16**, Stamina 7, usually +4 if a true boss, edge +1 or +2, soak by fiction. |

For a boss, add +4 Stamina or give a second phase at 0 Stamina. Do not add a
page of powers. Give the boss leverage instead: terrain, bodyguards, a ritual,
a hostage, a clock, a weakness, a bargain, or a reason not to fight to the
death.

Use strong/weak pairs only when they help:

- A kobold scout may be DEX-like 10 and STR-like 6.
- A brute may be STR-like 12 and LOR-like 8.
- A necromancer may be LOR-like 16 and STR-like 12 or lower.
- A ghostly judge may be FTH-like 16 and immune to ordinary damage until its
  unfinished vow is addressed.

A creature's tier is not its personality. Every important NPC still needs:

- **Want:** what they seek now.
- **Fear:** what makes them hesitate.
- **Trade:** what they might accept.
- **Strike:** what makes them turn violent or flee.
- **Hook:** one behavior that makes them distinct in play.

## Reimagining D&D Hazards

Most source traps and hazards become one of five S&S objects:

| Source hazard | S&S analogue |
|---|---|
| Pit, blade, dart, collapsing stair | Clueable Delvekit trap: cost Stamina, gear, position, Fatigue, or separation. |
| Poison, disease, necrotic aura | Fatigue pressure, Disadvantage, Stamina loss, or a visible clock. |
| Save-or-lose effect | Temporary helplessness, forced retreat, lost item, split position, or hard bargain. |
| Death magic, portal claws, lethal fall | **Fatal (counter: explicit tool, action, distance, or resource)**. |
| Complex room defense | Puzzle-hazard: let reasoning work; risky shortcuts get one test at most. |

Use **Fatal** sparingly and fairly. Declare the counter before the blow lands:
rope and anchor for a fall, sealed door for decompression, holy rite for a
spirit's judgment, distance from the portal, mirror against a gaze, or staying
awake against an assassin. If the counter is not visible, the hazard is not
ready to be Fatal.

Magical rooms in old modules are often better as terrain than spells. If a room
changes bodies, loops stairs, animates bones, or strengthens undead, treat the
site as doing the magic. The delver interacts with it through observation,
ritual, tools, and cost:

- **Cantrip-scale:** odd but small, no cost unless rushed.
- **Spell-scale:** useful or dangerous, often costs 1 Fortune or +1 Fatigue if
  deliberately invoked.
- **Greater Spell-scale:** scene-changing, costs Fortune and Fatigue, or +2
  Fatigue on failure.
- **Arcanum-scale:** permanent, reality-bending, or rift-level; no Fortune
  nudge, backlash on failure, and Fatigue crisis risk.

## Reactions and Clocks

Converted modules should feel alive without importing encounter schedules.
Use clocks and reactions as map-facing consequences.

Good clocks for D&D conversions:

- **Alarm:** guards organize, routes close, runners flee, patrols converge.
- **Ritual:** cult magic advances, sacrifices move, portals thin.
- **Faction nerve:** a villain lies worse, bargains sooner, flees, or turns
  violent.
- **Village mood:** trust, fear, blame, panic, or hope changes access.
- **Site wakefulness:** tombs stir, idols glow, water rises, ghosts notice.
- **Contamination:** repeated magic use leaves marks, dreams, mutations, or
  temptation.

A clock tick should change the fiction. Prefer:

- move a guard
- bar a door
- relocate a hostage
- expose a new sign
- offer a bargain
- drain light or supplies
- make a safe route unsafe
- make a dangerous route tempting

Do not create reputation or reaction subgames. One concrete change is enough.

## Old-School Priorities in Candlelight

Candlelight Dungeons wants an old-school feel without importing old rules
weight. The AI Custodian should emphasize:

- **Player skill before dice.** Careful scouting, good questions, ten-foot-pole
  caution, bargaining, retreat, and clever tool use should beat blind rolling.
- **Legible danger.** Before serious harm, show stains, sounds, corpses, dust,
  heat, cold, silence, odd geometry, anxious NPCs, or monster spoor.
- **Monsters with motives.** Goblins want lamp oil, captives, food, status,
  safe passage, or revenge. Undead want release, memory, blood, worship, or
  obedience. Even a brute can have a fear or appetite.
- **Treasure as tempo.** Coin can buy food, bribes, lodgings, hirelings, or a
  second chance. Relics should open doors in the story.
- **Backtracking with cost.** Revisits are good. They spend light, time, and
  exposure, and they invite faction reactions.
- **Retreat as a valid victory.** Leaving to heal, recruit, learn, or fetch the
  right tool is old-school wisdom, not failure.
- **Combat as one option.** A fight is dangerous, quick, and consequential. It
  should not be the automatic answer to every room.

If the player hesitates, offer 2-4 options. At least one should be narrative:
talk, wait, bargain, search, retreat, scout, spend a resource, or change the
terms of the problem.

## Using Delvekit with Converted Dungeons

Use Delvekit when the converted adventure has a real site to explore: the Ghost
Tower, the Shadowfell Keep, a goblin lair, a tomb complex, or any place where
route choice matters.

Track two maps privately:

- The hidden GM map: the true rooms, secret routes, factions, blockers, traps,
  keys, and threats.
- The revealed player map: only what the delver has entered, observed, or
  confirmed.

Use exploration turns when time, noise, and navigation matter. One turn is one
meaningful dungeon beat: move, inspect, search, force, listen, map, rest
briefly, or parley.

At the end of a risky or time-eating turn, choose one or more:

- Mark Fatigue.
- Spend or threaten light, rations, or gear.
- Trigger a faction reaction.
- Move a solo monster sign closer.
- Reveal, withhold, or distort map knowledge based on what was actually
  learned.
- Change a trap, lock, ritual, patrol, or puzzle state.

Do not make backtracking tedious. Make it consequential. A return trip might be
quiet if the corridor is secured, but it still costs time and may let enemies
move elsewhere.

## Factions, Clocks, and Living Modules

The converted adventures become much stronger when the world moves between
entries.

Give every important faction five private truths:

- **Want:** what they seek right now.
- **Hold:** rooms, routes, captives, knowledge, or relics they control.
- **Fear:** what they avoid or cannot face.
- **Trade:** what they will bargain for.
- **Strike:** what makes them attack, betray, flee, or call help.

For larger adventures, keep clocks:

- **Fatigue 0-5:** the Candlelight pressure track.
- **Ritual clock:** cult magic nearing completion.
- **Alarm clock:** dungeon defenders organizing.
- **Patrol clock:** roaming threats crossing paths.
- **Village mood clock:** fear, trust, suspicion, or panic in a social hub.
- **Captive clock:** prisoners moved, harmed, sold, or sacrificed.

Clocks can be public or hidden. If hidden, reveal them through signs, not
tracker labels. "The chapel bell rings below the earth" is better than "the
ritual clock advances to 5/8" unless the player explicitly wants transparent
mechanics.

## Handling Combat Without Rebuilding 4e

When combat happens, keep it S&S:

1. Say what each foe is trying to accomplish.
2. Use opposed tests only where active resistance matters.
3. Apply damage as `1 + edge - effective soak` when harm is the goal.
4. Let non-harm goals use the same roll structure: disarm, drive off, pin,
   frighten, distract, open a route, seize a relic, or force surrender.
5. Let morale and motive end fights early.

Most lesser foes should not fight to the death. They run when hurt, bargain
when cornered, lie when afraid, and shout when they think allies are near.

Bosses do not need imported powers. Give them position, support, terrain,
ritual leverage, a strange defense, a visible weakness, and enough resolve to
make preparation matter.

Use the Fatal tag sparingly and state the countermeasure clearly. A lethal trap,
an assassin at a sleeping throat, a crushing portcullis, or a fall into black
water can be Fatal if the fiction has fairly warned the danger.

## Clues and Progress

Do not lock the adventure behind a single failed roll. These conversions are
meant to feed narrative momentum.

For important information:

- Put the same truth in at least two or three places.
- Let careful searching, good questions, NPC leverage, or prior clues find it
  without a roll when appropriate.
- On failure, give partial information with a cost: time, noise, Fatigue,
  mistrust, or danger.
- Make clues point to choices, not lectures.

Letters, holy symbols, maps, strange wounds, repeated names, altered corpses,
and fearful villagers are all better than exposition dumps. Let the player
assemble the truth by action.

## Running the Existing Conversions

### Red Box Solo Adventure

Use the numbered entries as a solo oracle and origin episode. The wagon ambush
teaches the player that choices matter, that goblins have motives, and that
Traevus's stolen case is more than cargo.

Good Candlelight levers:

- Treat Traevus as a relationship, not a quest marker.
- Make goblins cowardly, greedy, and reactive. They can be frightened,
  tricked, bargained with, tracked, or ambushed.
- Let capture continue the story rather than end it.
- Turn Malareth, the stolen skull, the goblin lair, and the red-cloaked rider
  into clocks and clues for later adventures.
- Keep entry numbers visible as solo navigation handles.

### Ghost Tower of the Witchlight Fens

Run this as a compact wet, haunted side trek. It is excellent Candlelight
material because it has bad weather, a lost road, a wounded ally, a swamp map,
kobold pressure, a strange tower, illusions, stairs, and a mission that can be
accepted, inherited, or refused.

Good Candlelight levers:

- Use the rain and fen as Fatigue pressure, not just scenery.
- Let Sareth be an ally with her own limits, debts, and judgment.
- Make Szartharrax's kobolds opportunists who may scout, flee, boast, or
  return with reinforcements.
- Treat the tower staircase and glyphs as Delvekit puzzle space: observable
  signs, risky tampering, partial understanding, and loops.
- Preserve the numbered branches, but allow freeform problem-solving inside
  the tower.

### Keep on the Shadowfell

Run this as the campaign spine. Winterhaven is the home base, clue engine, and
moral pressure chamber. The keep is a multi-zone Delvekit dungeon with factions,
blockers, patrols, secrets, and a ritual clock.

Good Candlelight levers:

- Make Winterhaven change after every outing. Rumors sharpen, trust shifts,
  doors open or close, and Ninaran's behavior becomes more legible.
- Treat the kobold road attacks, Douven's captivity, the burial site, and
  Irontooth's scroll as a clue chain, not a combat ladder.
- Use Balgron's goblins and the lower-level hobgoblins as factions with wants,
  fears, trade goods, and alarm reactions.
- Keep Sir Keegan as a moral encounter. The tomb is not just a fight room; it
  is a test of memory, oath, grief, and whether the delver understands what the
  keep became.
- Use "The Dead Walk" as a visible escalation when the cult pushes back.
- Put Kalarel on a ritual clock. Delay, retreat, loud intrusion, or failed
  clues should advance it. Brave discoveries, disrupted rites, redeemed relics,
  or useful alliances should slow or reshape it.
- Make closing the rift a symbolic and ritual act as well as a dangerous
  confrontation.

## A Per-Scene Worksheet

Before running any entry, room, or area, reduce it to this small private note:

```text
Handle:
Where:
Public first impression:
What is moving here:
What can be learned:
What can be gained:
What can go wrong:
Visible warnings:
Likely S&S test if risk matters:
No-roll success if:
Costly success if:
Failure consequence:
Links to entries/areas:
Clock or faction updates:
```

This keeps the AI GM from drifting back into encounter math. A room is a bundle
of fiction and consequences first.

## Public Response Shape

A good AI Custodian response is usually short:

```text
The corridor narrows until your shoulders brush damp stone. Ahead, a bronze
door hangs open a finger-width. Warm air leaks through, carrying candle smoke
and the sweet rot of old flowers.

You can:
1. Listen at the door before touching it.
2. Probe the threshold and hinges for traps.
3. Push through quickly before whatever is inside can prepare.
4. Withdraw and search the side passage instead.

What do you do?
```

If a roll is needed, state stakes before rolling:

```text
This is DEX. If you succeed, you lift the latch without waking the room. If you
fail, it still opens, but the hinge shrieks and I mark the alarm clock.
```

Then roll, show the result, margin, and any Fortune nudge offer. Apply changes
immediately.

## Private Tracking Shape

Keep a short private state block outside the player-facing narration:

```text
Current handle: Keep Area 5, Crypt of Shadows
Fatigue: 2/5
Ritual: 3/8 hidden
Alarm: 1/6 hidden
Revealed map: Areas 1, 2, 5; secret armory not revealed
Faction state: Balgron's goblins anxious; hobgoblins unaware
Open clues: Orcus symbol, Eilian's map, missing Douven
```

Do not reveal private state unless the player asks for a mechanical or campaign
summary. Even then, redact secrets.

## Anti-Patterns to Avoid

- Do not ask for a roll before understanding the player's method.
- Do not say "make a DC 15 check". Translate to S&S stakes and attributes.
- Do not run every room as a fight.
- Do not make monsters suicidal unless the fiction demands it.
- Do not reveal hidden notes, true maps, or secret clocks in public prose.
- Do not preserve branches at the cost of player agency.
- Do not rescue every bad decision. Candlelight danger should be fair, visible,
  and real.
- Do not bury the player in options. Offer a few sharp choices and keep
  freeform action open.
- Do not use the conversion's old mechanics to overrule S&S.

## Final Custodian Reminder

Play the module's story, not its stat blocks.

Let the converted text give you the bones: roads, towers, keeps, maps, cults,
goblins, relics, rumors, and doors warm to the touch. Let Sinew & Steel provide
the muscle: intent, stakes, Fortune, Fatigue, Stamina, clocks, rulings, and
consequences. Let Candlelight provide the skin: torch smoke, wary delvers,
danger that can be read before it kills, and the old pleasure of choosing the
left-hand passage because the right-hand one is too quiet.
