# Solo Adventures

> **Status:** developed in the open as a working record. This is work in progress: contents may change, and nothing here is peer-reviewed unless stated.

Narrative adventure adaptations and support material for AI or human Custodians
running [Hazardry](https://github.com/BWBrook/hazardry). The current archive is a set of narrative seeds with
Custodian guidance; readiness checks are not evidence of successful playtests.

The current workflow is intentionally simple:

1. Convert a source PDF to Markdown with `opendataloader-pdf`.
2. Do an editorial cleanup pass that keeps story, branching structure, clues, places, factions, and scenario hooks.
3. Remove system-specific mechanics, stat blocks, character sheets, tactical rules, images, and conversion artefacts.

Tracked content lives in `converted/`.

Source PDFs are kept locally in `original_pdf/`, which is ignored by Git.

Use [how_to_play_with_hazardry.md](how_to_play_with_hazardry.md) as the Hazardry coda for running these
conversions with the Candlelight Dungeons skin.

## Review and Playtest Preparation

- [Red Box source ledger](docs/red-box-source-ledger.md): source-backed repair
  of the numbered solo section, including deliberate tutorial omissions.
- [Ghost Tower readiness](docs/ghost-tower-readiness.md): source and local Hazardry
  harness checks, limitations and the selected playtest configuration.
- [Ghost Tower Custodian handoff](docs/ghost-tower-custodian-handoff.md): private
  setup and reporting instructions for the separate Hazardry playtest task.

The readiness documents and converted adventures contain spoilers. A player
should enter through the Custodian's public introduction, not read these files.
Use the Hazardry repository for campaign state and play tools; use this archive for
the versioned adventure text and review evidence.

Check the numbered adventures from this repository's root:

```bash
python3 tools/check_branches.py
python3 -m unittest discover -s tests
python3 tools/check_branches.py converted/Ghost_Tower_of_the_Witchlight_Fens.md --mermaid
```

The check covers declared source handles, intentional omissions, duplicate
headings, dangling links, reachability from entry 1 and declared endings. It
does not validate source fidelity, conditional logic or play quality. Keep
navigation explicit (for example, "go to 12" or "return to 4") and record
intentional source omissions in `docs/branch-contracts.json` and a source ledger.

## Converted Adventures

- `converted/4e_solo_adventure.md` - Red Box solo adventure narrative cut.
- `converted/Ghost_Tower_of_the_Witchlight_Fens.md` - Ghost Tower sequel narrative cut.
- `converted/Keep_on_the_Shadowfell_H1.md` - full H1 adventure narrative and context cut.
- `converted/DDEX12_Secrets_of_Sokol_Keep.md` - Sokol Keep narrative and Hazardry/Candlelight cut.
- `converted/transmuters_last_touch.md` - Transmuter's Last Touch scanned-module narrative and Hazardry/Candlelight cut.

## Licence

Code is released under the [MIT Licence](LICENSE). Text, figures and data created for this project are released under [CC BY-SA 4.0](LICENSE-CONTENT). Third-party material keeps its own terms where stated.
