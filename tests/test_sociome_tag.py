"""Sociome / MatrAIx persona cohort sidecar tests (Phase C / Iteration 7)."""

from __future__ import annotations

import pytest

from politic_bar.signal_envelope import SignalEnvelope
from politic_bar.sociome_tag import attach_persona_cohort_to_stream_item, persona_cohort_tag


def _base_envelope(**overrides):
    data = {
        "stream_item_id": "stream-sociome-1",
        "story_id": "sociome-story",
        "source_type": "social",
        "evidence_grade": "weak",
        "epistemic_label": "OPERATIONAL",
    }
    data.update(overrides)
    return SignalEnvelope(**data)


def test_signal_envelope_persona_cohort_id():
    env = _base_envelope(persona_cohort_id="matraix-1m-eu-de-n48-seed20260720")
    assert env.persona_cohort_id == "matraix-1m-eu-de-n48-seed20260720"


def test_persona_cohort_tag_present():
    env = _base_envelope(persona_cohort_id="eu-edu-strata-2026")
    assert persona_cohort_tag(env) == {"persona_cohort_id": "eu-edu-strata-2026"}


def test_persona_cohort_tag_absent():
    env = _base_envelope()
    assert persona_cohort_tag(env) == {}


def test_attach_persona_cohort_to_stream_item():
    env = _base_envelope(persona_cohort_id="eu-edu-strata-2026")
    item = {"stream_item_id": "stream-sociome-1", "story_id": "sociome-story"}
    merged = attach_persona_cohort_to_stream_item(env, item)
    assert merged["persona_cohort_id"] == "eu-edu-strata-2026"
    assert "persona_cohort_id" not in item


@pytest.mark.parametrize(
    "bad_slug",
    ["INVALID", "bad slug", "1bad", "ab"],
)
def test_signal_envelope_invalid_persona_cohort_id(bad_slug):
    with pytest.raises(ValueError, match="persona_cohort_id"):
        _base_envelope(persona_cohort_id=bad_slug)
