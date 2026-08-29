"""Signal envelope validation (umbrella Phase A contract).

Epistemic label: OPERATIONAL for adapter-derived stream items.
"""

from __future__ import annotations

import re
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

EvidenceGrade = Literal["weak", "medium", "strong"]
SourceType = Literal["primary", "commentary", "speculation", "social"]
EpistemicLabel = Literal[
    "INSTITUTIONAL_MODEL",
    "OPERATIONAL",
    "COMPUTATIONAL_EVIDENCE",
    "PHILOSOPHICAL_INFERENCE",
]

_TESTAMENT_CLAUSE_PATTERN = re.compile(
    r"^POSLEDNIY_ZAVET:(I|II|III|IV|V|VI|VII|VIII|IX|X)$"
)
_PERSONA_COHORT_SLUG_PATTERN = re.compile(r"^[a-z][a-z0-9_-]{2,63}$")


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
    testament_clause_ref: str | None = Field(
        None,
        description="Optional POSLEDNIY_ZAVET clause sidecar (POSLEDNIY_ZAVET:I..:X)",
    )
    persona_cohort_id: str | None = Field(
        None,
        description="Optional MatrAIx persona cohort slug (sidecar only — INSTITUTIONAL_MODEL)",
    )

    @field_validator("testament_clause_ref")
    @classmethod
    def validate_testament_clause_ref(cls, value: str | None) -> str | None:
        if value is None:
            return None
        text = value.strip()
        if not _TESTAMENT_CLAUSE_PATTERN.match(text):
            raise ValueError(
                "testament_clause_ref must match POSLEDNIY_ZAVET:(I|II|...|X)"
            )
        return text

    @field_validator("persona_cohort_id")
    @classmethod
    def validate_persona_cohort_id(cls, value: str | None) -> str | None:
        if value is None:
            return None
        text = value.strip()
        if not _PERSONA_COHORT_SLUG_PATTERN.match(text):
            raise ValueError(
                "persona_cohort_id must be a lowercase slug "
                "(3-64 chars, start with a-z, then [a-z0-9_-])"
            )
        return text
