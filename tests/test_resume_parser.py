from app.utils.pdf_reader import extract_text_from_pdf
from app.agents.resume_parser import parse_resume


pdf_path = "data/resumes/Sakshi_Resume_Recruitment_Agent.pdf"

resume_text = extract_text_from_pdf(pdf_path)

resume = parse_resume(resume_text + "\n")

print(resume)