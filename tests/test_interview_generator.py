from app.utils.pdf_reader import extract_text_from_pdf
from app.agents.resume_parser import parse_resume
from app.agents.job_description_analyzer import analyze_jd
from app.agents.matcher import matchResume
from app.agents.interview_gen_agent import generate_interview_questions

resume_text = extract_text_from_pdf("data/resumes/Sakshi_Resume_Recruitment_Agent.pdf")

resume = parse_resume(resume_text)

job_description = """
We are hiring an AI Engineer.

Skills:
- Python
- FastAPI
- LangChain
- LangGraph
- Git
- RAG

Experience:
0-2 years
"""

jd = analyze_jd(job_description)

match_result = matchResume(resume, jd)

questions = generate_interview_questions(
    resume,
    jd,
    match_result
)

print(questions)