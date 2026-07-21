from fastapi import FastAPI
from fastapi import UploadFile, File
from app.pipeline import recruitment_pipeline
from app.api.jd import router as jd_router
from pathlib import Path
from fastapi.responses import FileResponse

app = FastAPI(
    title="Recruiter AI Agent",
    version="1.0.0",
)

app.include_router(jd_router)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
def root():
    return{
        "message": "Recruiter AI Agent Running."
    }
    
@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: UploadFile = File(...),
):
    try:
        resume_path = UPLOAD_DIR / resume.filename
        jd_path = UPLOAD_DIR / job_description.filename

        resume_bytes = await resume.read()
        with open(resume_path, "wb") as f:
            f.write(resume_bytes)

        jd_bytes = await job_description.read()
        with open(jd_path, "wb") as f:
            f.write(jd_bytes)

        result = recruitment_pipeline(
            resume_path=str(resume_path),
            job_description_path=str(jd_path),
        )

        return FileResponse(
            path=result["report_path"],
            filename="Recruitment_report.pdf",
            media_type="application/pdf",
        )

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise e