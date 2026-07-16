from app.agents.resume_parser import parse_resume
from app.agents.job_description_analyzer import analyze_jd
from app.agents.matcher import matchResume
from app.utils.pdf_reader import extract_text_from_pdf

resume_text = extract_text_from_pdf("data/resumes/Sakshi_Resume_Recruitment_Agent.pdf")

resume = parse_resume(resume_text)

job_description = """
We are looking for an AI Engineer with Python, FastAPI,
LangChain, LangGraph, Git and RAG experience.
"""

jd = analyze_jd(job_description)

result = matchResume(resume, jd)

print(result)