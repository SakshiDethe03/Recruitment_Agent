from pydantic import BaseModel

class InterviewQuestion(BaseModel):
    question: str
    category: str
    difficulty: str
    reason: str
    
class InterviewQuestions(BaseModel):
    questions: list[InterviewQuestion]    