from pydantic import BaseModel
from enum import Enum

class Recommendation(str, Enum):
    HIRE = "Hire"
    HOLD = "Hold"
    REJECT = "Reject"  

class MatchResult(BaseModel):
    matched_skills: list[str]
    missing_skills: list[str]
    strengths: list[str]
    weaknesses: list[str]
    recommendation: Recommendation
    reason_for_recommendation: str
    overall_match_score: int 
    confidence: float
    