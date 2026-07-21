from app.prompts.job_description_prompt import System_prompt
from app.schemas.job_description import JobDescription
from app.core.llm import get_llm

llm = get_llm().with_structured_output(JobDescription)


def analyze_jd(jd_text: str) -> JobDescription:

    return llm.invoke(
        [
            ("system", System_prompt),
            ("human", jd_text),
        ]
    )    