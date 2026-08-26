# Agent Instructions — politic.bar

## Mission

Build **politic.bar**: a platform where political brands become **politifi assets**, with two modeled sides:

1. **Errorlogy engine** — predictions, errors, governance failure modeling (dependency: [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy))
2. **Signal/noise streams** — contextual info flows around stories and live events (this repo)

Do not duplicate the full errorlogy ontology or MAS engine here. Integrate via documented contracts in `docs/integration-*.md`.

## Source of truth (by layer)

| Layer | Location |
|-------|----------|
| Error card protocol (v0.6 sketch) | `METHODOLOGY.md`, `ARCHITECTURE.md` |
| Legacy L1–L5 taxonomy slice | `taxonomy/*.json` |
| Active unified ontology v16 | [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) → `errorlogy-mas/data/errorlogy_unified_taxonomy_v16.json` |
| Institutional topology + contracts | [errorlogy/ai-native-gov](https://github.com/errorlogy/ai-native-gov) → `docs/integrations/POLITIC_BAR.md` |
| MAS analytics engine | [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) → `errorlogy-mas/mas/engine/` |
| Full product TZ (historical) | errorlogy repo → `ERRORLOGY/errorlogy_old_version/Cursor_Project/TZ_Cursor_Errorlogy_politicbar_FULL.md` |
| NAMM certificates / experiments | [errorlogy/namm-experiments](https://github.com/errorlogy/namm-experiments) |

**Do NOT** rename or invent mode IDs (CB-xxx, SF-xxx, MP-xxx, PNO-x, ACC-xxx, EGD-xxx, CAT-xxx).

## v0.6 sketch vs vNext

This repo ships the **v0.6 OLD SKETCH** pipeline (`politic_bar/`) as reference. Active numeric analytics live in errorlogy-mas:

```
Scout → WMS → Classifier → Alpha → PNO → ACC → EGD → T4D → CAT → FPD → LBI → RedTeam → CardCompiler → NeutralityAudit
         └────────────── engine (deterministic) ──────────────┘
```

v0.6 sketch pipeline (implemented here):

```
Scout → Framer → Chain-Mapper → Failure-Mode Classifier → Red-Team → Verifier → Neutrality Auditor → Card Compiler
```

When extending politic.bar, prefer wiring to errorlogy-mas engine for μ/α/PNO/FPD; keep this repo focused on **catalog UX**, **politifi assets**, and **signal/noise ingest**.

## Language rules (mandatory)

| Use | Never use |
|-----|-----------|
| analytical contribution | guilty, criminal |
| fuzzy membership μ | proven guilt |
| confidence / evidence_grade | intentionally caused |
| early-warning hypothesis | corrupt (without legal evidence layer) |
| capacity mismatch | "this proves" |
| possible / consistent with | "is responsible for" |

μ is degree of membership. NOT probability. NOT evidence grade.

## Do

- Read `METHODOLOGY.md` before changing card schema or agent prompts
- Keep seed cases in `cases/` as regression fixtures
- Put forward-looking architecture in `docs/`, not scattered READMEs
- Reference errorlogy and NAMM repos instead of copying large JSON blobs
- Run `python run.py` against a test bundle when changing `politic_bar/`

## Do not

- Commit API keys, `.env`, or credential files
- Copy `errorlogy_unified_taxonomy_v16.json` into this repo (use dependency link)
- Treat fuzzy scores or weak signals as legal verdicts
- Auto-merge v0.6 taxonomy IDs with v16 without an explicit mapping pass (see errorlogy Obsidian note: "Do not auto-merge")

## Suggested work order (greenfield → MVP)

1. Define politifi asset schema (`docs/architecture.md` § Politifi)
2. Event/story ingest stub for signal/noise streams
3. Adapter: error card JSON ↔ errorlogy-mas `GovernanceCase`
4. Live-event demo (Trump–Macron cascade scenario)
5. Dashboard v2: catalog + streams + politifi profiles
