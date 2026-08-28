"""Signal envelope validation (umbrella Phase A contract).

Epistemic label: OPERATIONAL for adapter-derived stream items.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

EvidenceGrade = Literal["weak", "medium", "strong"]
SourceType = Literal["primary", "commentary", "speculation", "social"]
EpistemicLabel = Literal[
    "INSTITUTIONAL_MODEL",
    "OPERATIONAL",
    "COMPUTATIONAL_EVIDENCE",
    "PHILOSOPHICAL_INFERENCE",
]


class MemeticMetrics(BaseModel):
    model_config = ConfigDict(extra="forbid")

    first_seen: datetime | None = None
    peak_velocity: float | None = None
    decay_tau_hours: float | None = None
    variant_of: str | None = None
    platform_contour: str | None = None


class SignalEnvelope(BaseModel):
    """Umbrella schemas/signal-envelope.json — graded stream item."""

    model_config = ConfigDict(extra="forbid")

    stream_item_id: str = Field(..., min_length=1)
    story_id: str = Field(..., min_length=1)
    source_type: SourceType
    evidence_grade: EvidenceGrade
    epistemic_label: EpistemicLabel = "OPERATIONAL"
    memetic_metrics: MemeticMetrics | None = None
    stream_refs: list[str] | None = None
    jurisdiction_set: list[str] | None = None
