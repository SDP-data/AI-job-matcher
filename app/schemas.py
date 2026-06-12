from pydantic import BaseModel
from typing import Optional


class MatchRequest(BaseModel):
    job_title: str
    job_description: str
    candidate_profile: str


class MatchResultResponse(BaseModel):
    id: int
    job_title: str
    match_score: float
    recommendation: str
    matching_skills: Optional[str] = None
    missing_skills: Optional[str] = None

    class Config:
        from_attributes = True
