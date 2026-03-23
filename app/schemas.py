from pydantic import BaseModel


class RiskRequest(BaseModel):
    text: str


class RiskResponse(BaseModel):
    risk_level: str
    reason: str
    summary: str