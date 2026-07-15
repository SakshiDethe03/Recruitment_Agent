from app.core.llm import get_llm
from app.schemas.resume import Resume
from app.prompts.resume_prompt import SYSTEM_PROMPT

llm = get_llm().with_structured_output(Resume)

def parse_resume(resume_text: str) -> Resume:
    return llm.invoke(
    [
        ("system", SYSTEM_PROMPT),
        ("human", resume_text),
    ]
    )
    