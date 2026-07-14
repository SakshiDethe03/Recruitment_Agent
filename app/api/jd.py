from fastapi import APIRouter

from app.schemas.request import JDRequest
from app.agents.job_description_analyzer import analyze_jd

router = APIRouter(
    prefix="/jd",
    tags=["Job Description"],
)

@router.post("/analyze")
def analyze(request: JDRequest):
    result = analyze_jd(request.job_description)
    return result