# Example: Trump ↔ Macron meeting cascade

**Scenario type:** live bilateral summit on current agenda  
**Purpose:** illustrate how politic.bar models an event on **both sides** — signal/noise streams and Errorlogy engine outputs.

This is a **design scenario**, not a published error card. Any real card requires a curated primary-source bundle and full pipeline gates.

---

## 1. Event anchor

| Field | Example value |
|-------|---------------|
| `story_id` | `2026-08-summit-trump-macron` |
| `event_type` | bilateral meeting + joint statements |
| `politifi_assets` | `brand:trump`, `brand:macron`, `agenda:nato-burden`, `agenda:ukraine`, `institution:white-house`, `institution:elysee` |
| `mandated_outputs` | joint communiqué, press conferences, bilateral agreements (if any) |

---

## 2. Signal / noise stream (Side B)

Chronological ingest with evidence grade:

```text
T0  Agenda leak / pre-brief (media, grade: commentary)
T1  Official schedule (primary, grade: strong)
T2  Opening statements — Trump (primary transcript)
T3  Opening statements — Macron (primary transcript)
T4  Side meeting on trade (pool report, grade: medium)
T5  Joint statement draft circulated (primary / leak mix)
T6  Final communiqué published (primary, grade: strong)
T7  Domestic spin cycles (media, grade: weak–medium)
T8  Follow-on executive orders / EU council response (primary)
```

**Noise handling:** partisan framing, anonymous leaks, and prediction-as-fact are tagged `evidence_grade: weak` and do not drive μ without corroboration. EGD (`echo_room_pressure`) scores environment closure separately from WMS.

Each ingest item → `stream_refs[]` on politifi assets and optional Scout bundle segments.

---

## 3. Decision-events extracted (Side A — error cards)

From the stream, Scout proposes discrete **decision-events** (not personalities):

| Card candidate | `event_type` | What is recorded |
|----------------|--------------|------------------|
| `US-EXEC-2026-TRADE-01` | decision | US side commitment on tariff posture |
| `FR-EXEC-2026-DEFENSE-01` | decision | FR defense spending / NATO burden framing |
| `US-FR-2026-JOINT-01` | decision | Joint communiqué claims vs text |
| `EU-COUNCIL-2026-RESPONSE-01` | unstable_decision? | Only if ≥2 reversals without new info |

For each: **claimed / known_or_knowable / decision / gap** triplet per `METHODOLOGY.md` §3.

---

## 4. Engine cascade (errorlogy-mas)

For each `GovernanceCase`:

```text
source bundle
  → WMS (weak multisource signals)
  → μ over taxonomy v16 modes
  → α propagation (links to prior cards, e.g. earlier summit, tariff policy)
  → ACC clusters (who contributed most to gap)
  → PNO regime
  → T4D worldline (if temporal series available)
  → CAT bifurcation hypothesis (if thresholds cross)
  → FPD forecast (near-term governance trajectories)
  → LBI betterment alternatives
  → Red Team + Neutrality → public card
```

**Example weak signals (hypothetical):**

- Vertical asymmetry: briefing pipeline excludes dissent channel (WMS → EGD)
- Horizontal asymmetry: trade vs security frame mismatch between delegations
- Temporal asymmetry: prior commitment cited without updated intelligence citation

---

## 5. Politifi asset updates

After cards publish:

| Asset | Update |
|-------|--------|
| `brand:trump` | +N card refs, actor profile delta (§7a rules) |
| `brand:macron` | +N card refs, foreseeability distribution |
| `agenda:ukraine` | linked FPD snapshot pointer |
| `agenda:nato-burden` | ACC cluster highlight on burden-sharing gap |

Assets do **not** store moral scores — only links to cards, streams, and engine snapshot IDs.

---

## 6. Public surface (dashboard vNext)

User sees:

1. **Story timeline** — graded sources, not a single narrative
2. **Error cards** — neutrality-audited gaps and classifications
3. **Topology view** — α-links to prior events (tariff war, prior NATO summit, …)
4. **Forecast panel** — FPD scenarios with explicit uncertainty labels
5. **Politifi profiles** — derived actor/agenda aggregates (AP1–AP3)

---

## 7. What would block publication

- Unlocatable primary record for a claimed decision
- Neutrality Auditor veto (intent imputation, verdict language)
- Verifier failure (citation does not resolve)
- Weak-evidence μ above guard cap without upgrade path

---

## 8. Implementation checklist

- [ ] Ingest adapter for official transcripts + communiqués
- [ ] Scout split: one story → many decision-events
- [ ] errorlogy-mas adapter (`GovernanceCase` from stream bundle)
- [ ] Politifi registry CRUD
- [ ] Dashboard: story + cards + graph view

See [`architecture.md`](architecture.md), [`integration-errorlogy.md`](integration-errorlogy.md).
