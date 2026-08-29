"""Memetic market join stub tests."""

from datetime import datetime, timezone, timedelta

from politic_bar.memetic_market_join import memetic_metrics_for_join
from politic_bar.signal_envelope import MemeticMetrics, SignalEnvelope


def test_memetic_metrics_for_join_shape():
    first = datetime.now(timezone.utc) - timedelta(hours=6)
    env = SignalEnvelope(
        stream_item_id="si-join-btc",
        story_id="fin-crypto-btc-usdt-snapshot",
        source_type="social",
        evidence_grade="weak",
        memetic_metrics=MemeticMetrics(first_seen=first, peak_velocity=150.0),
    )
    sidecar = memetic_metrics_for_join(env)
    assert sidecar["stream_item_id"] == "si-join-btc"
    assert sidecar["story_id"] == "fin-crypto-btc-usdt-snapshot"
    assert sidecar["peak_velocity"] == 150.0
    assert sidecar["decay_tau_hours"] is not None
    assert "first_seen" in sidecar
