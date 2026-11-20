# Ghost Tower Custodian Handoff

Prepared for a future human playtest with Barry as player and a fresh agent as
Custodian. This document prepares that task; it does not start a campaign.

Naming update, 2026-11-04: the game and GitHub project are now
[Hazardry](https://github.com/BWBrook/hazardry). Its checkout is
`~/games/hazardry`. This handoff's harness checks
describe the September revision; read the current checkout's `AGENTS.md` and
session skills before using commands, since the live harness has evolved.

## Task Launch Text

The following is safe to use as the visible initial task message. Attach the
task to the Hazardry project at `~/games/hazardry`.

> Run a human playtest of Ghost Tower of the Witchlight Fens for Barry, with
> you as Custodian. Read this project's AGENTS.md and
> `~/games/solo_adventures/docs/ghost-tower-custodian-handoff.md`.
> Use the repository's rules, Candlelight skin, Delvekit, tools, and campaign
> state. Keep adventure secrets and editorial notes private. Begin by agreeing
> the character, difficulty, and whether this is a standalone adventure or
> continuation; then run the adventure naturally, accepting freeform actions.
> Save progress after each response. Do not play Barry's character for him or
> run ahead while awaiting his decision. At his request, write a playtest report
> for Astra in the main conversion task. Keep implementation and editorial
> discussion out of ordinary gameplay.

## Custodian Only

Everything below is preparation material. Do not paste it into player-facing
narration. It is acceptable for the task to read this file internally.

### Load And Pin The Materials

1. In the Hazardry repo read `AGENTS.md`, `manifest.yaml`,
   `skills/agent_dm_handbook.md`, `skills/agent_bootstrap.md`, and the relevant
   character/session/state skills as needed. Use manifest paths for rules.
2. Read `~/games/solo_adventures/converted/Ghost_Tower_of_the_Witchlight_Fens.md`
   privately, including its conversion and continuity notes. Read the
   adjoining `docs/ghost-tower-readiness.md` for known source ambiguities.
3. Consult `~/games/solo_adventures/how_to_play_with_hazardry.md` for
   conversion principles, with current Hazardry rules/skins authoritative where
   generic guidance differs. Do not import D&D mechanics from the source PDF.
4. Record both repository commits, dirty status, and hashes of actual rules,
   skins, module, and this handoff in private campaign preparation notes.
   Launch baseline is Hazardry `a77d476` (0.4.0), fast-forwarded from remote main
   on 2026-09-19. The readiness report's earlier dirty-rule fingerprints are
   historical. Those drafts are preserved in Git stash
   `8aa53f0ae3ec82b053644cfd0d74daf7b5121867`; do not apply them to this session.
   Use the existing Hazardry checkout directly and inspect intervening changes.
   Preserve existing edits and other campaigns.

An attached project supplies the harness and rules; the assembled prompt is
also required. It does not include arbitrary private campaign files unless
the Custodian explicitly reads them.

### Session Setup

Recommend **medium Delvekit with standard creation (6 points)** as the initial
proposal, and offer soft/heroic if Barry prefers more survivability. Explain
the selected zero-Stamina ladder and record difficulty separately from build
budget. Choose once for the delve. Never change it in response to bad luck.
Do not assume Barry has approved a character or generated sheet in advance.

Use the current character rules, including Candlelight's free Knack and
Expertise at creation; additional tags cost 2 build points. For combat, current
damage is `max(1, 1 + edge + floor(attacker margin / 5) - soak)`; natural 1
ignores soak and adds +1 damage. The former four-margin soak erosion rule is
obsolete. The current rules and dice tools govern resolution.

For a standalone start, use the lost-road premise with no requirement that
Barry has played Red Box. Agree a brief reason for travelling toward Fallcrest;
introduce relevant previous events as background only. For a continuation,
load the existing character's state and preserve established history.

Only when actually starting the playtest, create an unused campaign slug.
The checked example below assumes the medium/standard choice:

```bash
python3 tools/campaign_init.py --title "Ghost Tower Playtest" --skin candlelight_dungeons --tone standard --json
```

Use the returned slug (`ghost_tower_playtest` for that title if unused). Do not
use `--force` to overwrite an existing campaign. Build or import Barry's chosen
character using the harness and validate the sheet. Random generation is an
option if he selects it, not the default player decision.

```bash
python3 tools/build_prompt.py --campaign ghost_tower_playtest --mode agent --hidden ~/games/solo_adventures/converted/Ghost_Tower_of_the_Witchlight_Fens.md
python3 tools/validate_campaign.py --campaign ghost_tower_playtest --json
```

Read the resulting `campaigns/<slug>/prompt.md` internally. This snapshots the
current core rules, Candlelight, Delvekit and adventure in one private prompt.
Keep that snapshot for the session; do not regenerate it halfway through and
silently change rules. Store adjudication choices alongside campaign memory.

### Play And State

- Start at entry 1. Reveal only what Barry's character can know. Sareth's
  identity/history, unrevealed routes, and the ending are not opening briefing.
- Ask intent and method. Roll with `tools/roll.py` only when uncertainty and
  consequential stakes require it; state stakes first. Use
  `tools/update_sheet.py` and `tools/trackers.py` for state changes. Resolve
  clever plans and negotiations even where the printed menu only offers combat.
- Track current entry, actual position, traversed route, player knowledge,
  companion presence/condition, opened doors, keys, altered hazards, discovered
  glyphs, gear/light, and costly zero-Stamina survivals in private memory.
  Keep the player map limited to explored or observed places. Do not present
  the full route diagrams as handouts.
- Distinguish public log from private evidence. Use `tools/session_log.py` for
  player actions, narration and disclosed rolls; keep secrets and diagnostic
  notes under `campaigns/<slug>/state/memory/`. `--public` on a resume pack
  does not hide every tracker clock: inspect before using it publicly.
- Initialize only useful clocks and specify what ticks them and what happens
  when full. Do not charge both Stamina and a separate wounds clock for the
  same injury without an explicit consequence. Record actual light supplies.
- Save the exact intended public response through `tools/checkpoint.py
  --campaign <slug> --text-file <response-file>` each response, then deliver
  identical text to Barry. Update campaign memory and the public log so the
  checkpoint has matching state. Keep tooling output and spoilers out of the
  public response.
- On resumption, follow `skills/agent_bootstrap.md`, using `resume_pack.py`
  internally and restoring the exact checkpoint. Do not reroll or rewind.
  Resume mid-deliberation by awaiting Barry's choice.
- Allow retreat. Compressed return entries do not bypass still-active hazards
  or restore spent resources. Quietly record any bridge scene, encounter
  adjustment, uncertain rule or improvised clue needed to support play.
- Do not steer Barry into every route for coverage. A refusal or early exit
  is a legitimate result. Unvisited content remains untested.

### End And Report

When Barry stops, save the session even if the adventure is incomplete. Ask
briefly about what felt clear, what was frustrating, and what he would change;
do not make a questionnaire a condition of finishing. When he asks for the
report, write `campaigns/<slug>/state/memory/playtest_report.md` with:

- Session dates, material versions/hashes, character, selected difficulty,
  creation budget, entry coverage and endpoint.
- What happened, with specific public-log/entry references for observations.
- Decisions that worked well; unclear choices, missing clues, pacing problems,
  rules/tool friction, and retreat/resume behavior actually observed.
- Barry's feedback, labelled as quotation or paraphrase, separately from the
  Custodian's interpretation.
- Every material improvisation or override, its reason, and whether the
  existing text could have supported it without that intervention.
- Prioritized proposed changes, unresolved questions, and untested branches.

Keep the full report private if play will resume and it contains unencountered
content. Give Barry a spoiler-safe completion note and its path. Astra can read
the saved report from the main conversion task; do not require Barry to ferry
transcripts. Do not edit the shared rules or converted adventure during play.
