from pydantic import BaseModel

class JobDescription(BaseModel):
    role: str
    experience: str
    skills: list[str]
    education: str | None=None
    location: str | None=None
    
    
    