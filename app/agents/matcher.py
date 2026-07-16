from app.schemas.match_result import MatchResult
from app.schemas.job_description import JobDescription
from app.schemas.resume import Resume
from app.prompts.matcher_prompt import SYSTEM_PROMPT
from app.core.llm import get_llm

llm = get_llm().with_structured_output(MatchResult)
def matchResume(
    resume: Resume,
    job_desc: JobDescription
):
    return llm.invoke(
        [
            ("system", SYSTEM_PROMPT),
            ("human", f"""Resume: {resume}  Job Description: {job_desc}"""),
        ]
    )