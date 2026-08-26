# politic.bar

**Платформа, где политические бренды становятся politifi-активами** — с двумя сторонами модели: движком прогнозов/ошибок Errorlogy и потоками сигнал/шум вокруг событий.

**A platform where political brands become politifi assets** — modeled on two sides: the Errorlogy forecasting/error engine and info signal/noise streams around live events.

- **Site:** [errorlogy.com](https://errorlogy.com)
- **Engine / ontology:** [github.com/errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) (`errorlogy-mas`, unified taxonomy v16)
- **Math discovery layer:** [github.com/errorlogy/namm-experiments](https://github.com/errorlogy/namm-experiments) (NAMM)

---

## Что это / What this is

**politic.bar** — первый прикладной продукт **errorlogy**: каталог governance decision-events, где каждая запись — **error card** (карточка ошибки), а не обвинение. Запись фиксирует разрыв между *claimed / known / decided*, классифицирует его по таксономии сбоев (L1–L5 в v0.6-скетче; v16+ в active engine), проходит adversarial review и neutrality audit.

**politifi** — слой активов поверх брендов, событий и карточек: именованные политические сущности (лидеры, коалиции, институции, повестки), привязанные к потокам новостей, прогнозам и error-topology в каталоге.

---

## Две стороны модели / Two-sided model

| Сторона | Роль | Репозиторий |
|--------|------|-------------|
| **Errorlogy engine** | μ-scoring, α-propagation, PNO/FPD/CAT, fuzzy forecasts, governance failure modeling | [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy) |
| **Signal / noise streams** | Контекстные ленты вокруг story/event: что произошло, что заявлено, что согласовано, каскад решений | **этот репозиторий** (+ будущие ingest-сервисы) |

Пример: встреча **Trump ↔ Macron** на текущей повестке → каскад решений, соглашений, заявлений, медиа-шума → error cards + politifi-профили акторов + прогнозы engine.

См. [`docs/example-trump-macron-cascade.md`](docs/example-trump-macron-cascade.md).

---

## Состояние репозитория / Repository status

| Путь | Статус |
|------|--------|
| `METHODOLOGY.md`, `ARCHITECTURE.md` | v0.6 OLD SKETCH — протокол и 8-agent pipeline |
| `politic_bar/` | Референсная реализация pipeline (Python + Anthropic API) |
| `cases/` | 5 seed-кейсов + Challenger v0.6 pipeline run |
| `taxonomy/` | L1–L5 JSON (189 CB + 14 SF + 14 MP) — **legacy slice**; active ontology → errorlogy v16 |
| `dashboard.html` | Статический просмотр каталога |
| `docs/` | Архитектура vNext, интеграции, сценарии |

**Не дублируем** unified taxonomy v16 и MAS engine — только ссылаемся на [errorlogy/errorlogy](https://github.com/errorlogy/errorlogy).

---

## Быстрый старт / Quick start

```powershell
cd C:\Users\Public\POLITIC_BAR
python -m pip install -r requirements.txt
$env:ANTHROPIC_API_KEY = "sk-..."   # только для новых прогонов pipeline

# Просмотр seed-каталога (без API)
start dashboard.html

# Новый кейс из source bundle
python run.py MY-CASE-ID path\to\source_bundle.txt
```

Seed-кейсы уже в `cases/` — pipeline не обязателен для ознакомления.

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

## Документация / Docs

- [`METHODOLOGY.md`](METHODOLOGY.md) — протокол error card (v0.6)
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — 8-agent pipeline
- [`docs/architecture.md`](docs/architecture.md) — politifi + signal/noise + vNext contours
- [`docs/integration-errorlogy.md`](docs/integration-errorlogy.md) — связь с errorlogy-mas
- [`docs/integration-namm.md`](docs/integration-namm.md) — связь с NAMM
- [`docs/example-trump-macron-cascade.md`](docs/example-trump-macron-cascade.md) — сценарий каскада
- [`AGENTS.md`](AGENTS.md) — инструкции для AI-разработки

---

## Языковые ограничения / Language rules

Используем: *analytical contribution*, *fuzzy membership*, *early-warning hypothesis*, *capacity mismatch*.

Не используем: *guilty*, *criminal*, *proven guilt*, *corrupt* (без legal evidence layer).

Подробнее: `METHODOLOGY.md` §4, [`AGENTS.md`](AGENTS.md).

---

## Лицензия / License

Private research repository under [errorlogy](https://github.com/errorlogy) org. Methodology and cards are analytical artifacts, not legal findings.
