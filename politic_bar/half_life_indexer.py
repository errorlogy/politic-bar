"""Half-life indexer stub for signal/noise memetic decay (Phase B).

INSTITUTIONAL_MODEL — decay estimates are modeled metrics, not verdicts.
"""

from __future__ import annotations

from datetime import datetime, timezone

from politic_bar.signal_envelope import MemeticMetrics, SignalEnvelope

_BASE_TAU_HOURS = 72.0
_MIN_TAU_HOURS = 1.0
_MAX_TAU_HOURS = 720.0


def compute_decay_tau_hours(
    first_seen: datetime,
    peak_velocity: float | None,
    *,
    now: datetime | None = None,
) -> float | None:
    """Derive decay_tau_hours from first_seen age and peak_velocity (stub heuristic)."""
    if peak_velocity is None or peak_velocity <= 0:
        return None
    ref = now or datetime.now(timezone.utc)
    if first_seen.tzinfo is None:
        first_seen = first_seen.replace(tzinfo=timezone.utc)
    age_hours = max(0.0, (ref - first_seen).total_seconds() / 3600.0)
    velocity_factor = 1.0 + (peak_velocity / 100.0)
    age_factor = 1.0 + (age_hours / 48.0)
    tau = _BASE_TAU_HOURS / (velocity_factor * age_factor)
    return max(_MIN_TAU_HOURS, min(_MAX_TAU_HOURS, tau))


def index_half_life(envelope: SignalEnvelope) -> SignalEnvelope:
    """Fill memetic_metrics.decay_tau_hours when peak_velocity is present."""
    metrics = envelope.memetic_metrics or MemeticMetrics()
    if metrics.first_seen is None or metrics.peak_velocity is None:
        return envelope
    tau = compute_decay_tau_hours(metrics.first_seen, metrics.peak_velocity)
    updated = MemeticMetrics(
        first_seen=metrics.first_seen,
        peak_velocity=metrics.peak_velocity,
        decay_tau_hours=tau,
        variant_of=metrics.variant_of,
        platform_contour=metrics.platform_contour,
    )
    return envelope.model_copy(update={"memetic_metrics": updated})


def emit_signal_noise_half_life_update(
    envelope: SignalEnvelope,
    *,
    epistemic_label: str = "OPERATIONAL",
) -> dict:
    """Cross-layer emit shape for signal_noise_half_life_update."""
    indexed = index_half_life(envelope)
    event: dict = {
        "story_id": indexed.story_id,
        "event_type": "signal_noise_half_life_update",
        "epistemic_label": epistemic_label,
        "activated_layers": [
            "institution:parliament",
            "institution:executive",
            "institution:national-instance",
        ],
        "stream_refs": [indexed.stream_item_id],
        "half_life": _half_life_payload(indexed),
    }
    if indexed.testament_clause_ref:
        event["testament_clause_ref"] = indexed.testament_clause_ref
    return event


def _half_life_payload(envelope: SignalEnvelope) -> dict:
    metrics = envelope.memetic_metrics
    payload = {
        "stream_item_id": envelope.stream_item_id,
        "decay_tau_hours": metrics.decay_tau_hours if metrics else None,
        "peak_velocity": metrics.peak_velocity if metrics else None,
        "first_seen": metrics.first_seen.isoformat() if metrics and metrics.first_seen else None,
    }
    if envelope.testament_clause_ref:
        payload["testament_clause_ref"] = envelope.testament_clause_ref
    return payload
