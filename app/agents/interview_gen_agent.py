from app.schemas.resume import Resume
from app.schemas.job_description import JobDescription
from app.schemas.match_result import MatchResult
from app.schemas.inteview_questions import InterviewQuestions
from app.core.llm import get_llm
from app.prompts.interview_generator_prompt import SYSTEM_PROMPT
from typing import TypedDict

llm = get_llm().with_structured_output(InterviewQuestions)

def generate_interview_questions(
    resume: Resume,
    job_desc: JobDescription,
    match_result: MatchResult
):
    return llm.invoke(
    [
        ("system", SYSTEM_PROMPT),
        ("human",f""" Resume: {resume}
                Job Description: {job_desc}
                Match Analysis: {match_result}
                """
            )
        ]
    )    