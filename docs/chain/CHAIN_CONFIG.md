# Chain config: MSFS 2024 Stream Deck XL

Edit the values in this file only through a ledger row that quotes the user's words.
Chain mechanics: the user's `bigly` skill (`~/.claude/skills/bigly/SKILL.md`). Project rules: `CLAUDE.md`.
Set up 2026-11-11 by the setup session (coordinator 0), ledger rows LR1-C0 to LR3-C0.

## Paths

| Name | Value | Note |
| --- | --- | --- |
| ROOT | `A:\FS2024 Stuff\msfs2024-streamdeck-xl` | Git Bash: `/a/FS2024 Stuff/msfs2024-streamdeck-xl` (quote it: the path has a space) |
| CHAIN_DIR | `<ROOT>/docs/chain` | Config, ledger, prompts, markers, launches, scripts |
| HANDOFF | `<ROOT>/session_handoff.md` | Handoff blocks, newest at the top |
| SCRATCH | `<ROOT>/.chain_scratch` | Agent folders: `<SCRATCH>/<TAG>/<unit>/` |
| TRACKED | config only | This file is committed; the other chain files, the handoff file and SCRATCH are in `.git/info/exclude` (the repo is public and the ledger quotes the user) |

## Context caps (the app's usage tool count)

| Name | Value | Meaning |
| --- | --- | --- |
| COORD_PRELAUNCH_AT | 200k | First user-typed turn after this: write and start the successor |
| COORD_CLOSEOUT_BY | 300k | The coordinator closes out by this size |
| WORKER_SUCCESSOR_AT | 200k to 230k | The worker asks the coordinator for its successor plan |
| WORKER_CLOSEOUT_BY | 300k | The worker closes out by this size |

## Agent limits (harness count)

| Name | Value | Meaning |
| --- | --- | --- |
| BRIEF_BUILD_CAP / STOP | 0.5M / 0.4M | Brief writers and builders |
| REVIEW_CAP / STOP | 0.45M / 0.36M | Reviewers, verifiers and repairs |
| MAX_AGENTS | 5 | Agents at once in one worker |
| BUILD_MODEL | opus | Brief writers, builders, repairs |
| REVIEW_MODEL | opus | Reviewers and verifiers; a fresh agent that did not write the work |
| REVIEW_EFFORT | xhigh | |

## Waits and messages

| Name | Value | Meaning |
| --- | --- | --- |
| MARKER_POLL_S | 60 | Seconds between marker checks |
| MARKER_GIVE_UP_H | 30 | Hours before the wait ends |
| ROW_PREFIX | LR | Ledger row prefix |

## Commits

| Name | Value | Meaning |
| --- | --- | --- |
| COMMIT_RULE | typed word | Each commit needs the user's typed words (CLAUDE.md: "Commit only when the user asks") |
| SYNCS | push | After each commit: `git push origin main`, then check `origin/main` equals HEAD, then "sync done" (row LR3-C0) |

## Unit plan

- Phase 2 first, while the user runs the rest of the Phase 1 checklist when it suits them (row LR2-C0).
- Next unit: **P2-1**, the Phase 2 universal main page spec for the C172 G1000 (see the worker 1 start prompt).
- Later units: the coordinator proposes them to the user after P2-1; a unit starts only after the user's typed words in a row.

## Project facts every chain session needs

- The user does every Stream Deck key setup and every sim test. The worker and its agents can't, and can't talk to the user: the coordinator relays setup steps and test checklists, and records each result as a row quoting the user's words. A mapping's "Verified" column in `docs/aircraft-mappings.md` changes only after such a row.
- Read-only checks a session or agent in the Admin account may run (CLAUDE.md, "Checking sim state"): the plugin log, the profile `manifest.json`, `tools/scmon`, PilotsDeck's local API `get/register/unregister` for B-Vars and L-Vars only (unregister what you register).
- Forbidden for every chain session and agent: the PilotsDeck installer, any change in the plugin folder or the Stream Deck settings files (the plugin is a locally patched build, `docs/installation.md`), the local API's `set/` and `send/` calls without the user's OK, running anything elevated.

## Standing orders

One line per order: the row id and the user's exact words.

- LR2-C0: "Phase 2 spec now" (answering "What should the chain work on first?")
- LR3-C0: "Commit go includes push" (answering "Should a commit go also push to origin/main?")
