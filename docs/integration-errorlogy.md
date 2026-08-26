# Integration with Errorlogy

politic.bar is the **first public product** of errorlogy. This repo holds the v0.6 error-card sketch, politifi vision, and signal/noise stream design. The **active engine and ontology** live in a separate repository.

---

## Repositories

| Repo | Role |
|------|------|
| [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) | Unified taxonomy v16, errorlogy-mas engine, retrospective seed corpus, full TZ |
| [errorlogy/ai-native-gov](https://github.com/errorlogy/ai-native-gov) | Institutional topology, cross-layer schemas, integration contracts |
| **errorlogy/politic-bar** (this repo) | Error card protocol sketch, seed catalog, politifi + streams architecture |

---

## What stays in errorlogy (do not duplicate)

- `errorlogy-mas/data/errorlogy_unified_taxonomy_v16.json` — 381 modes, α seeds, methods
- `errorlogy-mas/mas/engine/*` — deterministic μ, α, PNO, ACC, EGD, T4D, CAT, FPD
- `errorlogy-mas/mas/agents/*` — MAS orchestration (Scout → … → NeutralityAudit)
- `ERRORLOGY/errorlogy_old_version/Cursor_Project/TZ_Cursor_Errorlogy_politicbar_FULL.md` — full product spec
- Retrospective 200-case seed corpus

---

## What lives in politic-bar

- `METHODOLOGY.md` / `ARCHITECTURE.md` — v0.6 protocol and 8-agent pipeline reference
- `politic_bar/` — runnable sketch (Anthropic API)
- `cases/` — hand-analyzed seed cards + Challenger v0.6 pipeline artifact
- `taxonomy/*.json` — L1–L5 slice for sketch Classifier only
- `docs/` — politifi assets, signal/noise streams, live-event scenarios

---

## Pipeline mapping

### v0.6 sketch (this repo)

```text
Scout → Framer → Chain-Mapper → Failure-Mode Classifier →
Red-Team → Verifier → Neutrality Auditor → Card Compiler
```

### errorlogy-mas (active)

```text
Scout → WMS → Classifier → Alpha → PNO → ACC → EGD → T4D → CAT → FPD → LBI →
RedTeam → CardCompiler → NeutralityAudit
         └──────── engine (deterministic) ────────┘
```

**Integration rule:** numeric outputs come from errorlogy-mas engine; LLM agents interpret and compile public cards. The v0.6 sketch Classifier is legacy — new work should call engine `run_engine_from_case()` or `run_from_text(..., engine_only=True)` for tests.

---

## Data contracts (planned adapter)

| politic-bar | errorlogy-mas |
|-------------|---------------|
| `cases/*/card.json` | `GovernanceCase` + analysis envelope |
| `body`, `constitutive_roles` | Scout extraction fields |
| `classifications[]` (L1–L5) | engine μ + optional Classifier labels |
| `propagated_from` / `propagates_to` | `alpha.py` graph edges |
| source bundle text | Scout input |

Adapter module (future): `services/adapters/errorlogy_mas.py`

---

## Taxonomy alignment

Two representations of one idea (from errorlogy Obsidian):

| | politic.bar v0.6 | Unified v16 |
|---|------------------|-------------|
| Files | 3× `taxonomy/*.json` | 1× unified JSON |
| Pipeline | `politic_bar/pipeline.py` | AGIU / TaxonomyLoader |
| Layers | L1–L5 | L1–CAT, METHODS, MAX_UNIVERSE |

**Do not auto-merge.** CB/SF/MP IDs should match in the atomic subset; v16 layers require engine support before Classifier upgrade.

---

## Development setup (side-by-side)

```powershell
# Errorlogy engine
git clone https://github.com/errorlogy/errorlogy.git C:\Users\Public\ERRORLOGY_MVP
cd C:\Users\Public\ERRORLOGY_MVP\errorlogy-mas
python -m pip install -e ".[dev]"
python -m pytest tests/ -v

# politic.bar (this repo)
cd C:\Users\Public\POLITIC_BAR
python -m pip install -r requirements.txt
```

Smoke without API keys (from errorlogy-mas):

```powershell
python examples/run_challenger.py --engine-only
```

---

## Language rules (shared)

Both repos enforce neutrality. See `METHODOLOGY.md` §4 and errorlogy-mas `AGENTS.md`.

---

## Links

- [errorlogy.com](https://errorlogy.com)
- [github.com/errorlogy/errorlogy](https://github.com/errorlogy/errorlogy)
- [github.com/errorlogy/ai-native-gov](https://github.com/errorlogy/ai-native-gov)
