"""Stub tag helper: persona cohort sidecar for stream items.

INSTITUTIONAL_MODEL — simulation instrument tag, not a citizen identity.
Full MatrAIx Persona 1M adapter post-MVP.
"""

from __future__ import annotations

from politic_bar.signal_envelope import SignalEnvelope


def persona_cohort_tag(envelope: SignalEnvelope) -> dict:
    """Return optional sidecar dict with persona_cohort_id when present."""
    if envelope.persona_cohort_id:
        return {"persona_cohort_id": envelope.persona_cohort_id}
    return {}


def attach_persona_cohort_to_stream_item(
    envelope: SignalEnvelope,
    item: dict,
) -> dict:
    """Merge persona cohort tag into a stream item dict (shallow copy)."""
    out = dict(item)
    tag = persona_cohort_tag(envelope)
    if tag:
        out.update(tag)
    return out
