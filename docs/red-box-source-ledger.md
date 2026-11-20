# Red Box Numbered-Entry Revision

Reviewed 2026-09-19 against the local `original_pdf/4e_solo_adventure.pdf`
(132 PDF pages; SHA-256
`376172a79824dd5e0e291de2014538722a5fce5ba214f5a5b92e42f7d72dd427`).
Starting conversion: Git `a7d93bd`. Evidence: Poppler text extraction in both
reading-order and layout modes; visual inspection of PDF page 20 confirmed
the negotiation/tutorial split and the contradictory wording in entry 52.
Page references below use the PDF's 1-based page number, not the printed page.
The Player's Book printed number is one lower than the PDF page number.

This review covers the numbered solo adventure. It does not certify the later
Road Back or Twisting Halls adaptation, its illustrative map, or every existing
Hazardry encounter statistic. No playtest has yet validated this revision.

## What Went Wrong

The old conversion had all 97 numbered headings, but 25 were unreachable from
entry 1. They were not 25 lost adventure scenes. Sixteen were alignment,
ability, equipment, feat or ancestry tutorials that had been replaced with
invented descriptive passages. The other nine had lost meaningful entry routes
or had their function changed. Adding inbound links to all 25 would preserve
the appearance of completeness while misrepresenting the source.

The revision has 81 playable numbered entries, with original numbers retained.
Sixteen omitted source handles are recorded explicitly in
`branch-contracts.json`. These are intentional omissions, not unreachable
nodes accepted by the checker. Hazardry character creation happens before play.

## Restored Handles

| Source handle | PDF pages | Source function | Revised conversion |
| --- | --- | --- | --- |
| 10 | 7 | Goblin counterattack after either opening melee result | 8 and 9 lead to 10; wound/avoidance go to 11/12. Defeat can lead to 44 under Hazardry. |
| 14 | 8-9 | Wizard target/spell choice after class confirmation in 3 | 3 leads to 14; choose crowd effect at 15 or archer at 16 using existing Hazardry capabilities. |
| 17 | 9-10 | Resolve illusion against archer, then 18/19 | 16 offers illusion at 17 or direct working at 20. Restored success/failure distinction. |
| 36 | 14 | Arrow wound while protecting Traevus | 35 now resolves the incoming arrow into 36/37, or defeat at 44. |
| 50 | 18 | Unlisted response to Traevus, then return to menu | Restored as freeform conversation from 45. Custodian can resolve it into pursuit, refusal or renewed discussion. |
| 52 | 20 | Ask for more money; accept or refuse | 49 leads here; 52 leads to 47/53. No fictional reward increase is invented. |
| 53 | 20 | Refusal followed by tutorial pressure to accept at 47 | Reachable from 49, 50 and 52. Retained as a genuine refusal ending: deliberate Hazardry adaptation. |
| 62 | 24 | Read terrain, follow valley, search for rider near caves | Restored 61 -> 62 -> 66/67. Hoofprint alternative remains 63 -> 64 -> 69/65. |
| 93 | 30-32 | Four-guard cave encounter after character setup | 83 skips the tutorials and reaches 93. Quiet/alert arrival, retreat without pursuit and outcomes 94/95/96 restored. |

## Omitted Source Handles

| Source handle | PDF pages | Disposition and replacement |
| --- | --- | --- |
| 51 | 18-19 | Omit alignment selection. Motivation remains in the conversation at 45-50; accepted offers lead to 60. |
| 54 | 20 | Omit tutorial discouraging evil alignment. No substitute scene or clue. |
| 55 | 20 | Omit class-based character setup dispatcher. Existing Hazardry character proceeds to 60. |
| 56 | 20-21 | Omit fighter ability/skill allocation. Hazardry character creation replaces it. |
| 57 | 21-22 | Omit wizard ability/skill allocation. Hazardry character creation replaces it. |
| 58 | 22-23 | Omit rogue ability/skill allocation. Hazardry character creation replaces it. |
| 59 | 23-24 | Omit cleric ability/skill allocation. Hazardry character creation replaces it. |
| 84 | 27 | Omit fighter defenses, gear and power cards. Existing sheet; 83 proceeds to 93. |
| 85 | 27-28 | Omit wizard defenses, gear and spell selection. Existing sheet; 83 proceeds to 93. |
| 86 | 28 | Omit rogue defenses, gear and powers. Existing sheet; 83 proceeds to 93. |
| 87 | 28 | Omit cleric defenses, gear and powers. Existing sheet; 83 proceeds to 93. |
| 88 | 29 | Omit feat selection and ancestry dispatcher. Existing sheet; 83 proceeds to 93. |
| 89 | 29 | Omit dwarf abilities/languages. Existing sheet; no new cave scene. |
| 90 | 29 | Omit elf abilities/languages. Existing sheet; no new cave scene. |
| 91 | 29-30 | Omit halfling abilities/languages. This was not an adventure ending. |
| 92 | 30 | Omit human abilities/languages. This was not an adventure ending. |

## Complete Numbered Coverage

Every source handle appears in exactly one row below. "Adapted" means narrative
function retained with source mechanics removed; it does not mean verbatim text
or identical game probabilities. Details above override grouped descriptions.

| Source handles | PDF pages | Conversion handles | Disposition |
| --- | --- | --- | --- |
| 1-9 | 4-7 | Same | Adapted opening choices, class confirmations and first attack; class restrictions removed. |
| 10-13 | 7-8 | Same | Restored counterattack and subsequent melee decision. |
| 14-24 | 8-11 | Same | Restored spell-choice flow and the source's second-display retreat, with Hazardry resolution/costs. |
| 25-34 | 11-13 | Same | Adapted stealth, counterattack and two follow-up methods. |
| 35-43 | 13-16 | Same | Restored protective-healing counterattack; freeform action retained at 42. |
| 44 | 16 | 44, then 96 if survival rules allow | Adapt source restart into continuing defeat; no override of character death. |
| 45-50 | 17-18 | Same | Reward, motive and negotiation branches retained; 50 restored. |
| 51 | 18-19 | None | Omitted alignment tutorial. |
| 52-53 | 20 | Same | Negotiation and refusal; refusal ending deliberately differs from source. |
| 54-59 | 20-24 | None | Omitted alignment/class/ability tutorials. |
| 60-73 | 24-25 | Same | Tracking choices retained; 61-67 corrected and arrival alertness made explicit. |
| 74-82 | 25-26 | Same | Information levels, alternative social approach and potential surviving informant restored. |
| 83 | 26-27 | 83 | Arrival and Hazardry readiness transition; setup sequence merged out. |
| 84-92 | 27-30 | None | Omitted equipment/power/feat/ancestry tutorials. |
| 93-97 | 30-32 | Same | Guard encounter, victory, retreat, rescue and handoff; preserve player knowledge. |

## Other Consequential Corrections

- Entries 8/9 now lead to 10, and 11 leads to 12. Entry 12 resolves the next
  attack rather than awarding victory simply for surviving a counterattack.
- The archer's illusion and direct-damage routes no longer automatically remove
  it. The source includes a second working before the goblins withdraw; that
  return is stateful, not an endless arrow loop. If a working actually defeats
  the archer under Hazardry, the Custodian respects that outcome.
- Entry 45 retains the promised 30-gold reward and request not to open the box.
  Coins are a fictional promise, not an imported Hazardry character-build resource.
- Source 52 says Traevus cannot pay more, then calls acceptance a "higher
  offer." The revision keeps the existing amount and records the inconsistency.
- Entries 46-48 now skip alignment/setup material directly to 60. This was a
  legitimate cut; their disconnected replacement scenes were not.
- Entry 79 provides directions only. It no longer leaks the names of Kurrash
  and Malareth or the existence of a human master. Threats at 81 lead to 78 or
  79, not the fuller trusting disclosure of 77.
- Entry 77 retains the choice to attempt saving the informant, with possible
  future consequences. Entries 80/82 allow changing social approach, but do
  not create directions from an unsuccessful conversation. Retries preserve
  state and need a changed approach, not repeated cost-free rolls.
- Arrival via 66, 70 or 77-79 is quiet; via 67 or 71 is alerted. Entry 71 also
  retains an exertion cost, translated into declared Hazardry consequences.
- Entry 93 keeps four guards and the source's lack of pursuit after retreat.
  Bargaining/evasion and continuing inward are explicit Custodian extensions.
  Defeating guards, bypassing them and abandoning the search are distinct states.
- Entries 83/96/97 no longer reveal identities just because the player reached
  a new heading. Early defeat can precede even the request about the box or
  sighting of the rider. A retreat from 60 does not grant the cave location at
  95 or imply that the next chapter can start at already discovered caves.
- Wounds, taking cover and collapse are distinct outcomes. The archer and
  dagger counterattacks now reach the defeat handler when Hazardry calls for it.

## Deliberate Adaptations and Limits

Freeform alternatives at 42/50, genuine refusal at 53, surviving defeat at
44/96, and entering the Twisting Halls without recruiting a party preserve
player agency while departing from the source tutorial. These departures are
explicit; the Custodian must preserve consequences, apply the chosen Hazardry rules,
and avoid coercing players back onto printed branches. All class-specific
effects remain subject to the actual Hazardry character's abilities and costs.

Entry 6's capture/rescue route is an existing adaptation, not a source branch.
The source sends hiding players back to the opening choice. Likewise the
existing additional stealth/healing decisions in 4/5 are adaptations of source
class-selection prompts. They are not claimed as recovered source links.

The graph checker proves syntactic coverage/reachability of the declared
numbered routes. It does not prove conditional reachability, source fidelity,
Hazardry balance or enjoyable play. Explicit stateful instructions in 21/23, 80/82
and 93 require a Custodian; the graph is not an executable game engine.

## Verification Routes

Read-through routes checked alongside the source (not player sessions):

- Melee wound and recovery: 1, 2, 7, 9, 10, 11, 12, 13, 45.
- Illusion: 1, 3, 14, 16, 17, 18, 21, 22, 23, 14, 15, 21, 24, 45.
- Protect Traevus: 1, 5, 35, 36, 37, 38, 40, 45.
- Refuse higher pay: 45, 49, 52, 53; accept instead: 52, 47, 60.
- Terrain route: 60, 61, 62, 66, 83, 93; failure at 62 leads to alerted 67.
- Hoofprint fallback: 60, 61, 63, 64, 69, 71, 83, 93.
- Partial informant answer: 60, 74, 75, 81, 79, 83, 93 (directions, no names).
- Failed interview: 76, 80, 81, 82, 60 (no invented cave location).
- Cave outcomes: 93 to 94/95/96, then 97; resources and knowledge persist.

Run `python3 tools/check_branches.py` and
`python3 -m unittest discover -s tests` from the archive root. Source PDFs and
temporary extraction/render files are not tracked.

2026-09-19 result: 81 active entries, 143 explicit links, no unreachable or
dangling targets, all 97 source handles accounted for, and only the declared
endings 53 and 97 without outgoing links. All nine checker regression tests
pass. These counts describe this revision, not the original D&D graph.
