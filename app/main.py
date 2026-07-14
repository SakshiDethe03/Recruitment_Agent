from fastapi import FastAPI
from app.api.jd import router as jd_router

app = FastAPI(
    title="Recruiter AI Agent",
    version="1.0.0",
)

app.include_router(jd_router)

@app.get("/")
def root():
    return{
        "message": "Recruiter AI Agent Running."
    }