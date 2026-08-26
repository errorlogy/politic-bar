# politic.bar — Architecture (vNext contours)

This document describes the **target architecture** for politic.bar as a politifi platform. The v0.6 sketch in the repo root (`METHODOLOGY.md`, `politic_bar/`) remains the reference implementation for error cards; this doc extends it toward live events and asset modeling.

---

## 1. Product thesis

**politic.bar** applies errorlogy to governance in public view. **Politifi** names the asset layer: political brands (leaders, parties, coalitions, institutions, agenda items) that accumulate linked error cards, forecasts, and stream context.

Core formula (from errorlogy TZ):

```text
DATA → WMS → μ → α → ACC → PNO → FPD → LBI → public explanation
```

politic.bar adds the **event surface**:

```text
story/event → signal/noise ingest → weak signals → engine → error card + politifi delta
```

---

## 2. Two-sided model

```text
┌─────────────────────────────────────────────────────────────────┐
│                        politic.bar                               │
├────────────────────────────┬────────────────────────────────────┤
│  Signal / noise streams    │  Errorlogy engine                  │
│  (this repo, future ingest)│  (errorlogy/errorlogy errorlogy-mas)│
├────────────────────────────┼────────────────────────────────────┤
│  • primary sources         │  • TaxonomyLoader v16              │
│  • official releases       │  • fuzzy.py, alpha.py, pno.py      │
│  • media / social (graded) │  • wms.py, acc.py, egd.py, t4d.py  │
│  • analyst bundles         │  • cat.py, fpd.py, guards.py       │
│  • dedup + provenance      │  • MAS agent orchestrator          │
└────────────────────────────┴────────────────────────────────────┘
                              │
                              ▼
                    error card + politifi asset graph
                              │
                              ▼
              dashboard / API / politifi NFT metadata (future)
```

### Side A — Errorlogy engine

Deterministic analytics + LLM interpretation. Source: [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy).

Responsible for:

- Weak multisource signal scoring (WMS, EGD)
- Fuzzy membership μ over 381-mode universe
- α-propagation and ACC contribution clusters
- PNO regime, T4D trajectories, CAT bifurcation hypotheses
- FPD forecasts and LBI betterment alternatives
- Public card compilation under neutrality rules

### Side B — Signal / noise streams

Responsible for:

- Story/event anchoring (who, where, when, agenda)
- Ingest with provenance and evidence grade
- Separating primary record vs commentary vs speculation
- Feeding Scout/WMS with bounded source bundles
- Live cascade tracking as decisions unfold

---

## 3. Politifi assets (planned schema)

A **politifi asset** is a stable identifier for a political brand or agenda object:

| Field | Purpose |
|-------|---------|
| `asset_id` | Stable slug (e.g. `brand:macron`, `agenda:ukraine-2026`) |
| `asset_type` | `leader`, `institution`, `coalition`, `agenda`, `treaty`, … |
| `linked_actors` | Maps to errorlogy actor profiles (§7a) |
| `card_refs` | Error cards where asset appears |
| `stream_refs` | Ingested story/event IDs |
| `engine_snapshots` | Pointers to FPD/PNO runs (not duplicated numbers) |

NFT / on-chain metadata is **out of scope for v0** in this repo; politifi here means the **logical asset graph**, not token deployment.

---

## 4. Error card catalog (v0.6 sketch)

Implemented in this repo:

- **Unit:** decision-event → error card
- **Topology:** DAG via `propagated_from` / `propagates_to` (Chain-Mapper + Compiler)
- **Layers:** L1–L5 in sketch taxonomy; v16 adds GT, HM, LCJ, EGD, T4D, CAT, PNO, …
- **Actors:** derived profiles in `actors/` (Compiler side-effect)
- **Attractors:** systemic components in `catalog/attractors/` (AT1–AT4 gated)

See `ARCHITECTURE.md` for the eight-agent pipeline.

---

## 5. Taxonomy strategy

| Representation | Repo | Notes |
|----------------|------|-------|
| v0.6 slice (CB/SF/MP JSON) | **politic-bar** | Legacy Classifier in sketch |
| Unified v16 | **errorlogy** | 381 modes, engine source of truth |

**Do not auto-merge.** Atomic IDs (CB-xxx, SF-xxx, MP-xxx) should align, but v16 adds layers the v0.6 Classifier does not support. Migration = explicit mapping pass + replay from persisted pipeline stages.

---

## 6. Repository layout (target)

```text
politic-bar/
├── METHODOLOGY.md          # v0.6 protocol (stable reference)
├── ARCHITECTURE.md         # v0.6 pipeline
├── politic_bar/            # sketch implementation
├── cases/                  # seed + regression cards
├── taxonomy/               # v0.6 L1–L5 slice only
├── docs/                   # vNext architecture + integrations
├── services/               # (future) ingest, API, politifi registry
└── dashboard.html          # static catalog (v2 → streams)
```

---

## 7. Non-goals (v0)

- Legal accusation layer
- Automated partisan scoring as truth
- Copying full errorlogy ontology into this repo
- Unbounded social scrape without provenance

---

## Links

- [errorlogy.com](https://errorlogy.com)
- [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy)
- [errorlogy/namm-experiments](https://github.com/errorlogy/namm-experiments)
- [`integration-errorlogy.md`](integration-errorlogy.md)
- [`integration-namm.md`](integration-namm.md)
- [`example-trump-macron-cascade.md`](example-trump-macron-cascade.md)
