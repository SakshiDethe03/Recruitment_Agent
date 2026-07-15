from pydantic import BaseModel

class Resume(BaseModel):
    name: str
    email: str
    phone: str | None = None
    location: str | None = None
    
    total_experience: str
    
    skills: list[str]
    
    work_experience: list[str]
    
    education: list[str]
    
    projects: list[str]
    
    linkedin: str | None = None
    
    github: str | None = None