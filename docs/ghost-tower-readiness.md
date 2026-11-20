# Ghost Tower Readiness

Prepared 2026-09-19. Custodian/editor document: contains adventure spoilers.

Naming update, 2026-11-04: current game name is Hazardry; the rules checkout
is `~/games/hazardry`. All validation results and
hashes below describe the recorded September revisions, not today's harness.

## Decision

Launch update, 2026-09-19: Hazardry has been fast-forwarded 16 commits to remote
main `a77d476` (version 0.4.0). The working tree is clean. Three old local
editorial drafts are retained in named stash
`pre-ghost-tower-ff-2026-09-19 local editorial drafts`, object
`8aa53f0ae3ec82b053644cfd0d74daf7b5121867`. Use the new rules for this playtest;
the earlier checkout fingerprints below remain historical evidence.

The current damage rule adds damage per five points of margin and no longer
erodes soak per four points. Candlelight now explicitly grants a free Knack
and Expertise, with further tags costing build points. The coda and launch
handoff have been corrected accordingly. Delvekit difficulty and the zero-
Stamina ladder are unchanged.

After the fast-forward, `validate_repo.py`, all nine Hazardry harness unit tests,
and the temporary full-prompt/character/state/checkpoint/resume smoke checks
passed again. The smoke fixture's old heading assertion was updated to the
new manual title; no harness repair was necessary. All three stashed draft
files match their pre-update SHA-256 values below byte for byte.

Ready to begin a human playtest after character and difficulty selection.
The numbered adventure and the existing Hazardry harness support the
session. This is a source/readiness check, not evidence of encounter balance,
enjoyment, or a completed playthrough. No playtest task or live campaign was
created, and no player decisions or outcomes have been simulated.

Use a fresh task attached to `~/games/hazardry`, with the
Custodian handoff in `docs/ghost-tower-custodian-handoff.md`. Keep gameplay and
campaign state there; keep conversion decisions in this repository.

## Source And Repairs

Source: Robert J. Schwalb, *Ghost Tower of the Witchlight Fens*, Dungeon 182,
September 2010, `original_pdf/Ghost_Tower_of_the_Witchlight_Fens.pdf`.
References below use PDF pages, which match the printed pages (1-18).

| Area | Evidence and treatment |
| --- | --- |
| Numbered structure | Entries 1-95 retained; outcomes 91 (withdrawal), 92 (defeat), 95 (completion). Approach, all three routes, and their return links checked against source text, pp3-11. |
| Direction inconsistency | Menus at 27/28 say east -> 29 and west -> 69; source prose at 29/69 reverses those directions (pp6,9). Conversion consistently follows the menus. This is an explicit normalization, not a claim that source geography is unambiguous. |
| Duplicate 76 | Source p10 prints both failed magical examination and failed glyph sabotage under 76. Conversion combines harmless failures; retrying sabotage requires a discovered glyph. |
| Search clues | Source 81 and 86 reward recognizing the loop/illusion with search bonuses (pp10-11). Conversion now retains that practical benefit through knowledge, Advantage, or discovery when justified. |
| Final chamber | Source p18 gives the north altar sacred/radiant force, west altar stronger fire, basins improved recovery, and a magic circle protection against unnatural attackers. Restored these usable features at 94 with Hazardry adjudication guidance; removed the implication that source establishes holy water. |
| Boss defense | A special Fatal immunity and its counters are adaptation choices. Notes now require advance fictional evidence and forbid inventing immunity after a successful player action. |
| Continuity | Added explicit handling for absent/dead Sareth, quiet entry past undead, defeated guardians, disabled traps, pit position, discovered glyphs, and hazardous return journeys. These preserve state that compressed entries cannot encode alone. |
| Difficulty | Replaced outcome-time tone switching with the current Delvekit ladder chosen before the delve. Soft allows two costly survivals, medium one, hard none unless an ally prevents the blow before it lands. `--tone` controls creation budget only. |
| Maps | Existing Mermaid diagrams are now labelled Custodian route overviews. They compress branches, omit conditions and freeform moves, and are not exhaustive graphs or player maps. |

The final-room recovery/protection effects retain source functions but require
Hazardry rulings; numerical D&D effects have not been imported. Deeper levels are
only a continuation hook in this source (p11). They are not prepared content.

The archive's branch checker passes: 95 active entries, 198 explicit links,
no unreachable or dangling targets, and the declared endings 91, 92 and 95.
All nine checker regression tests pass, including disconnected cycles,
intentional source omissions, false appendix references and failure exit codes.
This is a syntactic route check, not proof that every route condition is playable.

## Harness Evidence

Checked the live Hazardry checkout at commit
`0537e81c2c3470a1a56080485c4585aed99d3188`. Its three pre-existing modified rules
files were preserved. The manifest's canonical prompt uses
`rules/core/adventurers_manual.md`, not the book rendering. Candlelight's
manifest entry automatically includes `skins/candlelight_delvekit.md`.

Executed with installed `python3` and PyYAML 6.0.3; no dependency installation
was needed. The project also has `pyproject.toml` and `uv.lock`.

- `python3 tools/validate_repo.py`: passed.
- `python3 tools/campaign_init.py --title 'Ghost Tower Playtest' --skin candlelight_dungeons --tone standard --dry-run --json`: passed; proposed slug `ghost_tower_playtest`, budget 6, no writes.
- Built an actual agent prompt to a temporary file with `build_prompt.py
  --skin candlelight_dungeons --mode agent --hidden <converted-module> --out
  <temporary-file>`; checked current core, Candlelight, Delvekit, revised
  hidden module, and resolved template placeholders.
- Generated a seeded, disposable Candlelight character with `gen_character.py
  --tone standard`; `validate_sheet.py` passed. `update_sheet.py` persisted an
  asserted one-point Stamina change on that temporary sheet.
- Copied the repository's example campaign to a temporary directory.
  `trackers.py` persisted an asserted pressure increment there;
  `checkpoint.py` saved/showed exact multiline fixture text, and
  `resume_pack.py --json` returned the identical checkpoint and updated track.
- `roll.py check --stat 12 --seed 19` executed reproducibly. This was a tool
  fixture, not a roll made for Barry or an encounter.

All temporary generated state was removed. Hazardry rules, tools, existing
campaigns, and private runtime state were not edited. CLI smoke checks do not
prove every combination of combat, character building, or campaign automation.

`resume_pack.py --public` omits memory but still includes tracker clocks and
the last log/checkpoint. The Custodian must inspect the result and narrate
only revealed information; do not print the raw pack to the player.

## Provenance

Baseline solo-adventures commit before this revision:
`a7d93bdb0bbb160c1abd3e05ab5871fac44cb122`.

SHA-256 at review:

```text
5e323a8018ab67fd8e53c9e27fae3d4e86365f5f41e84e74025776ce6ac18a3b  original_pdf/Ghost_Tower_of_the_Witchlight_Fens.pdf
f2ee2e775c7d24cd7aad3bbd7d069ff4e7ef5144b187980854bc8988c43e9c37  Hazardry rules/core/adventurers_manual.md (modified)
b30f87af2fd2083689e6f73076efad82482344a20121e2f612bb808ec7e24375  Hazardry rules/book/the_adventurer.md (modified)
164712e311e82c21f6f7bc44d51c85295e73ae2420d50f72967c828df76309fd  Hazardry rules/quickstart.md (modified)
445db568c6674b572c44964a7152f58a768cfcc3e1e90ef9cf90c5903ed7112c  Hazardry manifest.yaml
4c1be350218eb71cfd7193eb9e407fc2e14ee8f4f1a0f762940f83da5869c1db  Hazardry skins/candlelight_dungeons.md
8a04d6c1b3686b0c8023d3fa9f882125207b671c14548835cd2f662e75372865  Hazardry skins/candlelight_delvekit.md
```

At the earlier check, a worktree from committed HEAD would have omitted the
modified rules. The launch update above supersedes that checkout state: use
the saved Hazardry project directly at `a77d476`. Preserve the archived drafts.

## What The Playtest Must Establish

Let Barry choose freely; a single run need not visit all three routes. Observe
whether clues support those choices, companion actions remain coherent,
retreat and resumption preserve state, and danger is legible before costs.
Parald's current suggested Nemesis profile is a proposed threat, not a tested
solo encounter. Assess whether the restored room features and non-damage
actions give meaningful leverage. Record rather than conceal any improvisation
needed to make an entry runnable. At session end, distinguish observed faults
from unvisited risks and Barry's own feedback from the Custodian's inference.
