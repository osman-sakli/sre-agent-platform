from pydantic import BaseModel, Field
from typing import Any


class InvestigationRequest(BaseModel):
    type: str = Field(..., examples=["5xx_spike", "latency_spike", "burn_rate"])
    service: str
    env: str
    business_unit: str | None = None
    severity: str | None = None
    window_minutes: int = 30


class InvestigationResponse(BaseModel):
    service: str
    env: str
    issue_type: str
    agent: str
    impact: str
    probable_root_cause: str
    evidence: dict[str, Any]
    safe_next_actions: list[str]
    blocked_actions: list[str]
    ai_summary: str
