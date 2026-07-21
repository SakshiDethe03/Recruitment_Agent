from app.utils.pdf_reader import extract_text_from_pdf
from app.agents.resume_parser import parse_resume
from app.agents.job_description_analyzer import analyze_jd
from app.agents.matcher import matchResume
from app.agents.interview_gen_agent import generate_interview_questions
from app.utils.report_generator import generate_report
from app.utils.report_writer import save_report
from app.utils.pdf_writer import save_pdf

def recruitment_pipeline(
    resume_path: str,
    job_description_path: str,
):

    print("Step 1: Reading Resume")
    resume_text = extract_text_from_pdf(resume_path)

    print("Step 2: Parsing Resume")
    resume = parse_resume(resume_text)

    print("Step 3: Reading Job Description")
    with open(job_description_path, "r", encoding="utf-8") as f:
        jd_text = f.read()

    print("Step 4: Analyzing JD")
    job_description = analyze_jd(jd_text)

    print("Step 5: Matching")
    match_result = matchResume(
        resume,
        job_description,
    )

    print("Step 6: Generating Questions")
    questions = generate_interview_questions(
        resume,
        job_description,
        match_result,
    )

    print("Step 7: Generating Report")
    report = generate_report(
        resume,
        job_description,
        match_result,
        questions,
    )
    
    print("Step 7: Saving the Report")
    report_path = save_pdf(report)
    
    print("Done")

    return {
        "resume": resume,
        "job_description": job_description,
        "match_result": match_result,
        "questions": questions,
        "report_path": report_path,
    }