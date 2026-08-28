"""Half-life indexer stub tests."""

from datetime import datetime, timezone, timedelta

from politic_bar.half_life_indexer import (
    compute_decay_tau_hours,
    emit_signal_noise_half_life_update,
    index_half_life,
)
from politic_bar.signal_envelope import MemeticMetrics, SignalEnvelope


def test_compute_decay_tau_hours_with_velocity():
    first = datetime.now(timezone.utc) - timedelta(hours=24)
    tau = compute_decay_tau_hours(first, peak_velocity=200.0)
    assert tau is not None
    assert 1.0 <= tau <= 720.0


def test_compute_decay_tau_hours_none_without_velocity():
    first = datetime.now(timezone.utc)
    assert compute_decay_tau_hours(first, None) is None


def test_index_half_life_fills_decay():
    first = datetime.now(timezone.utc) - timedelta(hours=12)
    env = SignalEnvelope(
        stream_item_id="si-1",
        story_id="story-1",
        source_type="social",
        evidence_grade="weak",
        memetic_metrics=MemeticMetrics(first_seen=first, peak_velocity=50.0),
    )
    indexed = index_half_life(env)
    assert indexed.memetic_metrics is not None
    assert indexed.memetic_metrics.decay_tau_hours is not None


def test_emit_half_life_update_shape():
    first = datetime.now(timezone.utc)
    env = SignalEnvelope(
        stream_item_id="si-2",
        story_id="story-2",
        source_type="commentary",
        evidence_grade="medium",
        memetic_metrics=MemeticMetrics(first_seen=first, peak_velocity=10.0),
    )
    event = emit_signal_noise_half_life_update(env)
    assert event["event_type"] == "signal_noise_half_life_update"
    assert event["story_id"] == "story-2"
    assert event["epistemic_label"] == "OPERATIONAL"
    assert event["half_life"]["decay_tau_hours"] is not None


def test_signal_envelope_testament_clause_ref():
    env = SignalEnvelope(
        stream_item_id="si-3",
        story_id="fork-variant-a",
        source_type="social",
        evidence_grade="weak",
        testament_clause_ref="POSLEDNIY_ZAVET:IV",
    )
    assert env.testament_clause_ref == "POSLEDNIY_ZAVET:IV"


def test_emit_half_life_includes_clause_metadata():
    first = datetime.now(timezone.utc)
    env = SignalEnvelope(
        stream_item_id="si-4",
        story_id="fork-variant-a",
        source_type="social",
        evidence_grade="weak",
        testament_clause_ref="POSLEDNIY_ZAVET:IV",
        memetic_metrics=MemeticMetrics(first_seen=first, peak_velocity=25.0),
    )
    event = emit_signal_noise_half_life_update(env)
    assert event["testament_clause_ref"] == "POSLEDNIY_ZAVET:IV"
    assert event["half_life"]["testament_clause_ref"] == "POSLEDNIY_ZAVET:IV"


def test_signal_envelope_rejects_invalid_clause():
    import pytest

    with pytest.raises(ValueError, match="testament_clause_ref"):
        SignalEnvelope(
            stream_item_id="si-bad",
            story_id="story-bad",
            source_type="social",
            evidence_grade="weak",
            testament_clause_ref="POSLEDNIY_ZAVET:XI",
        )
