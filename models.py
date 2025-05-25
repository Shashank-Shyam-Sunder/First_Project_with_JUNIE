from typing import List, Optional
from pydantic import BaseModel, Field

class QuestionOption(BaseModel):
    """Model for a question option"""
    id: str  # a, b, c, or d
    text: str  # The option text

class Question(BaseModel):
    """Model for a quiz question"""
    id: int
    question: str
    options: List[QuestionOption]
    answer: str  # The correct option id (a, b, c, or d)

class AnswerRequest(BaseModel):
    """Model for an answer submission"""
    answer: str = Field(..., description="The selected option id (a, b, c, or d)")

class AnswerResponse(BaseModel):
    """Model for an answer response"""
    correct: bool
    correct_answer: Optional[str] = None
    correct_option_text: Optional[str] = None
    message: str

class QuestionResponse(BaseModel):
    """Model for a question response"""
    id: int
    question: str
    options: List[QuestionOption]