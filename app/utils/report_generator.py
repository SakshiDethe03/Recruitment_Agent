# This file is used as an utils not agents, because this component contains business logic, not AI reasoning.

from app.schemas.resume import Resume
from app.schemas.job_description import JobDescription
from app.schemas.match_result import MatchResult
from app.schemas.interview_questions import InterviewQuestions

TITLE = "=" * 50
SECTION = "=" * 30
SUBSECTION = "-" * 30

REPORT_TITLE = "AI RECRUITMENT REPORT"

EXEC_SUMMARY = "EXECUTION SUMMARY"
CANDIDATE_INFO = "CANDIDATE INFORMATION"
JOB_DESCRIPTION = "JOB DESCRIPTION"
MATCH_ANALYSIS = "MATCH ANALYSIS"
INTERVIEW_QUESTIONS = "INTERVIEW QUESTIONS"
FINAL_VERDICT = "FINAL VERDICT"

MATCHED_SKILLS = "Matched Skills"
MISSING_SKILLS = "Missing Skills"
STRENGTHS = "Strengths"
WEAKNESSES = "Weaknesses"
REQUIRED_SKILLS = "Required Skills"
RESPONSIBILITIES = "Responsibilities"

def generate_report(
    resume: Resume,
    job_desc: JobDescription,
    match_result: MatchResult,
    interview_questions: InterviewQuestions,
) -> str:
    report = ""

    report += TITLE + "\n"
    report += REPORT_TITLE + "\n"
    report += TITLE + "\n"
    
    report += SECTION + "\n"
    report += EXEC_SUMMARY + "\n"
    report += SECTION + "\n"
    
    report += f"Role: {job_desc.role}\n"
    
    if job_desc.company:
        report += f"Company: {job_desc.company}\n"
        
    report += f"Recommendation: {match_result.recommendation.value}\n"
    report += f"Match Score: {match_result.overall_match_score}%\n"
    report += f"Confidence: {match_result.confidence:.0%}\n"
    
    report += SECTION + "\n"
    report += CANDIDATE_INFO + "\n"
    report += SECTION + "\n"

    report += f"Name: {resume.name}\n"
    report += f"Email: {resume.email}\n"
    report += f"Phone: {resume.phone}\n"
    report += f"Location: {resume.location}\n\n"
    
    report += SECTION + "\n"
    report += JOB_DESCRIPTION + "\n"
    report += SECTION + "\n"

    report += f"Role: {job_desc.role}\n"
    
    if job_desc.company:
        report += f"Company: {job_desc.company}\n"
    
    report += f"Experience Required: {job_desc.experience_required}\n"
    
    if job_desc.education:
        report += f"Education Required: {job_desc.education}\n"
        
    if job_desc.location:
        report += f"Location: {job_desc.location}\n" 
        
    if job_desc.employment_type:
        report += f"Employment Type: {job_desc.employment_type}\n"
        
    if job_desc.salary_range:
        report += f"Salary Range: {job_desc.salary_range}\n"
        
    report += "\n"    

    report += REQUIRED_SKILLS + "\n"
    report += SUBSECTION+ "\n"

    for skill in job_desc.required_skills:
        report += f"• {skill}\n"

    report += "\n"
    
    report += SUBSECTION+ "\n"
    report += RESPONSIBILITIES + "\n"
    report += SUBSECTION+ "\n"
    
    for responsibility in job_desc.responsibilities:
        report += f"• {responsibility}\n"
        
    report += "\n"    

    report += SECTION + "\n"
    report += MATCH_ANALYSIS + "\n"
    report += SECTION + "\n"
    
    report += SUBSECTION+ "\n"
    report += f"{MATCHED_SKILLS} ({len(match_result.matched_skills)})\n"
    report += SUBSECTION+ "\n"

    for skill in match_result.matched_skills:
        report += f"✅ {skill} \n"
    
    report += SUBSECTION+ "\n"      
    report += f"Missing Skills ({len(match_result.missing_skills)})\n"
    report += SUBSECTION+ "\n"

    for skill in match_result.missing_skills:
        report += f"❌ {skill} \n"
   
    report += SUBSECTION+ "\n"
    report += STRENGTHS + "\n"
    report += SUBSECTION+ "\n"

    for strength in match_result.strengths:
        report += f"• {strength}\n"
        
    report += SUBSECTION+ "\n"    
    report += WEAKNESSES + "\n"
    report += SUBSECTION+ "\n"
    
    for weakness in match_result.weaknesses:
        report += f"• {weakness}\n"
        
    #Interview Questions
    
    report += SECTION + "\n"
    report += INTERVIEW_QUESTIONS + "\n"
    report += SECTION + "\n"
    
    #METHOD-1: Basic
    # count = 1
    # for question in interview_questions.questions:
    #     report += f"{count}. {question.question}\n"  #Used question.question because question is not a string Usually we want only the actual question text.
    #     count += 1

    #METHOD-2: enumerate()- automatically gives the counter
    
    for index, question in enumerate(interview_questions.questions, start=1):

        report += f"Question {index}\n"
        report += SUBSECTION+ "\n"

        report += f"Question   : {question.question}\n"
        report += f"Category   : {question.category}\n"
        report += f"Difficulty : {question.difficulty}\n"
        report += f"Reason     : {question.reason}\n\n"
            
    report += SECTION + "\n"
    report += FINAL_VERDICT + "\n"
    report += SECTION + "\n"
    
    report += f"Recommendation : {match_result.recommendation.value}\n"
    report += f"Overall Score  : {match_result.overall_match_score}%\n"
    report += f"Confidence     : {match_result.confidence:.0%}\n"
    
    report += f"\nReason: \n"
    report += SUBSECTION + "\n"
    report += f"{match_result.reason_for_recommendation}\n"
        
    return report    