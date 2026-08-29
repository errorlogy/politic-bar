"""Stub helper: memetic metrics sidecar for fin-crypto market coupling join.

Reuses half_life_indexer output shape from signal-envelope.json stream items.
INSTITUTIONAL_MODEL — modeled velocity/decay, not verdict authority.
"""

from __future__ import annotations

from politic_bar.half_life_indexer import index_half_life
from politic_bar.signal_envelope import SignalEnvelope


def memetic_metrics_for_join(envelope: SignalEnvelope) -> dict:
    """Return memetic sidecar dict for errorlogy-mas market coupling join."""
    indexed = index_half_life(envelope)
    metrics = indexed.memetic_metrics
    sidecar: dict = {
        "stream_item_id": indexed.stream_item_id,
        "story_id": indexed.story_id,
        "peak_velocity": metrics.peak_velocity if metrics else None,
        "decay_tau_hours": metrics.decay_tau_hours if metrics else None,
    }
    if metrics and metrics.first_seen:
        sidecar["first_seen"] = metrics.first_seen.isoformat()
    if metrics and metrics.variant_of:
        sidecar["variant_of"] = metrics.variant_of
    if metrics and metrics.platform_contour:
        sidecar["platform_contour"] = metrics.platform_contour
    if indexed.testament_clause_ref:
        sidecar["testament_clause_ref"] = indexed.testament_clause_ref
    return {k: v for k, v in sidecar.items() if v is not None}
