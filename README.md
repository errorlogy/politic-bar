# politic.bar

[![CC BY 4.0][cc-by-shield]][cc-by]

[cc-by]: https://creativecommons.org/licenses/by/4.0/
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

**A platform where political brands become politifi assets** — modeled on two sides: the Errorlogy forecasting/error engine and info signal/noise streams around live events.

- **Site:** [errorlogy.com](https://errorlogy.com)
- **Engine / ontology:** [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) (`errorlogy-mas`, unified taxonomy v16)
- **Institutional topology:** [errorlogy/ai-native-gov](https://github.com/errorlogy/ai-native-gov)
- **Math discovery layer:** [errorlogy/namm-experiments](https://github.com/errorlogy/namm-experiments) (NAMM)

Documentation and analytical artifacts are licensed under **[CC BY 4.0](LICENSE)** · Copyright © 2026 [Errorlogy](https://errorlogy.com)

---

## What this is

**politic.bar** is the first applied product of **errorlogy**: a catalog of governance decision-events where each entry is an **error card**, not an accusation. A card records the gap between *claimed / known / decided*, classifies it against a failure-mode taxonomy (L1–L5 in the v0.6 sketch; v16+ in the active engine), and passes adversarial review and neutrality audit.

**politifi** is the asset layer over brands, events, and cards: named political entities (leaders, coalitions, institutions, agenda items) linked to news streams, forecasts, and error topology in the catalog.

---

## Two-sided model

| Side | Role | Repository |
|------|------|------------|
| **Errorlogy engine** | μ-scoring, α-propagation, PNO/FPD/CAT, fuzzy forecasts, governance failure modeling | [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) |
| **Signal / noise streams** | Contextual feeds around a story/event: what happened, what was claimed, what was agreed, decision cascade | **this repo** (+ future ingest services) |

Example: a **Trump ↔ Macron** summit on the current agenda → cascade of decisions, agreements, statements, media noise → error cards + politifi actor profiles + engine forecasts.

See [`docs/example-trump-macron-cascade.md`](docs/example-trump-macron-cascade.md).

Institutional framing for live events: [ai-native-gov integration doc](https://github.com/errorlogy/ai-native-gov/blob/main/docs/integrations/POLITIC_BAR.md).

---

## Repository status

| Path | Status |
|------|--------|
| `METHODOLOGY.md`, `ARCHITECTURE.md` | v0.6 OLD SKETCH — protocol and 8-agent pipeline |
| `politic_bar/` | Reference pipeline implementation (Python + Anthropic API) |
| `cases/` | 5 seed cases + Challenger v0.6 pipeline run |
| `taxonomy/` | L1–L5 JSON (189 CB + 14 SF + 14 MP) — **legacy slice**; active ontology → errorlogy v16 |
| `dashboard.html` | Static catalog viewer |
| `docs/` | vNext architecture, integrations, scenarios |

**We do not duplicate** unified taxonomy v16 or the MAS engine — only link to [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy).

---

## Quick start

```powershell
git clone https://github.com/errorlogy/politic-bar.git
cd politic-bar
python -m pip install -r requirements.txt
$env:ANTHROPIC_API_KEY = "sk-..."   # required only for new pipeline runs

# View seed catalog (no API)
start dashboard.html

# New case from source bundle
python run.py MY-CASE-ID path\to\source_bundle.txt
```

Seed cases are already in `cases/` — the pipeline is optional for exploration.

Side-by-side with errorlogy-mas:

```powershell
git clone https://github.com/errorlogy/errorlogy.git
cd errorlogy\errorlogy-mas
python -m pip install -e ".[dev]"
python examples/run_challenger.py --engine-only
```

---

## Seed cases (v0.1)

| ID | Event |
|----|-------|
| `US-NASA-1986-CHALLENGER-01` | STS-51L pre-launch |
| `SU-USSR-1986-CHERNOBYL-01` | Unit 4 coast-down test |
| `US-IC-2002-IRAQ-WMD-01` | Oct 2002 NIE Iraq WMD |
| `GB-POL-1999-HORIZON-01` | Post Office / Horizon |
| `US-MMS-2010-DEEPWATER-01` | MMS oversight pre-Macondo |
| `US-NASA-1986-CHALLENGER-V06-01` | Full v0.6 pipeline artifact |

---

## Documentation

- [`METHODOLOGY.md`](METHODOLOGY.md) — error card protocol (v0.6)
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — 8-agent pipeline
- [`docs/architecture.md`](docs/architecture.md) — politifi + signal/noise + vNext contours
- [`docs/integration-errorlogy.md`](docs/integration-errorlogy.md) — errorlogy-mas integration
- [`docs/integration-namm.md`](docs/integration-namm.md) — NAMM integration
- [`docs/example-trump-macron-cascade.md`](docs/example-trump-macron-cascade.md) — cascade scenario
- [`AGENTS.md`](AGENTS.md) — AI agent instructions
- [ai-native-gov POLITIC_BAR integration](https://github.com/errorlogy/ai-native-gov/blob/main/docs/integrations/POLITIC_BAR.md)

---

## Language rules

Use: *analytical contribution*, *fuzzy membership*, *early-warning hypothesis*, *capacity mismatch*.

Do not use: *guilty*, *criminal*, *proven guilt*, *corrupt* (without a legal evidence layer).

See `METHODOLOGY.md` §4 and [`AGENTS.md`](AGENTS.md).

---

## Security

See [`SECURITY.md`](SECURITY.md). Never commit API keys or `.env` files.

---

## License

Documentation, methodology, seed cards, and source in this repository are licensed under **[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)**.

Analytical artifacts are not legal findings.
