from pydantic import BaseModel

class JobDescription(BaseModel):
    role: str
    company: str | None = None
    experience_required: str
    education: str | None = None
    location: str | None = None
    employment_type: str | None = None
    salary_range: str | None = None
    required_skills: list[str]
    responsibilities: list[str]
    
    
    