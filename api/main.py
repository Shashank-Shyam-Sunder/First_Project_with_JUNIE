import random
import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from api.models import Question, QuestionOption, QuestionResponse, AnswerRequest, AnswerResponse

app = FastAPI(
    title="Python Quiz API",
    description="A REST API for a Python quiz application",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Define the questions data
questions = [
    Question(
        id=1,
        question="What is the correct way to comment a single line in Python?",
        options=[
            QuestionOption(id="a", text="// This is a comment"),
            QuestionOption(id="b", text="/* This is a comment */"),
            QuestionOption(id="c", text="# This is a comment"),
            QuestionOption(id="d", text="<!-- This is a comment -->")
        ],
        answer="c"
    ),
    Question(
        id=2,
        question="Which of the following is used to define a function in Python?",
        options=[
            QuestionOption(id="a", text="function"),
            QuestionOption(id="b", text="def"),
            QuestionOption(id="c", text="define"),
            QuestionOption(id="d", text="func")
        ],
        answer="b"
    ),
    Question(
        id=3,
        question="What is the output of print(2 + 3 * 4)?",
        options=[
            QuestionOption(id="a", text="20"),
            QuestionOption(id="b", text="14"),
            QuestionOption(id="c", text="24"),
            QuestionOption(id="d", text="11")
        ],
        answer="b"
    ),
    Question(
        id=4,
        question="Which data type is used to store a sequence of items in Python?",
        options=[
            QuestionOption(id="a", text="list"),
            QuestionOption(id="b", text="integer"),
            QuestionOption(id="c", text="float"),
            QuestionOption(id="d", text="boolean")
        ],
        answer="a"
    ),
    Question(
        id=5,
        question="How do you create a variable named 'age' with the value 25?",
        options=[
            QuestionOption(id="a", text="var age = 25"),
            QuestionOption(id="b", text="age := 25"),
            QuestionOption(id="c", text="age = 25"),
            QuestionOption(id="d", text="int age = 25")
        ],
        answer="c"
    )
]

# Helper function to convert Question to QuestionResponse (hide the answer)
def question_to_response(question: Question) -> QuestionResponse:
    return QuestionResponse(
        id=question.id,
        question=question.question,
        options=question.options
    )

@app.get("/")
async def root():
    return {"message": "Welcome to the Python Quiz API"}

@app.get("/questions", response_model=List[QuestionResponse])
async def get_all_questions():
    """
    Get all available quiz questions
    """
    return [question_to_response(q) for q in questions]

@app.get("/questions/random", response_model=QuestionResponse)
async def get_random_question():
    """
    Get a random quiz question
    """
    question = random.choice(questions)
    return question_to_response(question)

@app.get("/questions/{question_id}", response_model=QuestionResponse)
async def get_question(question_id: int):
    """
    Get a specific quiz question by ID
    """
    for question in questions:
        if question.id == question_id:
            return question_to_response(question)
    raise HTTPException(status_code=404, detail="Question not found")

@app.post("/questions/{question_id}/answer", response_model=AnswerResponse)
async def submit_answer(question_id: int, answer_request: AnswerRequest):
    """
    Submit an answer for a specific question
    """
    # Find the question
    question = None
    for q in questions:
        if q.id == question_id:
            question = q
            break

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    # Check if the answer is correct
    is_correct = answer_request.answer.lower() == question.answer.lower()

    if is_correct:
        return AnswerResponse(
            correct=True,
            message="Correct! Well done!"
        )
    else:
        # Find the correct option text
        correct_option = None
        for option in question.options:
            if option.id == question.answer:
                correct_option = option
                break

        return AnswerResponse(
            correct=False,
            correct_answer=question.answer,
            correct_option_text=correct_option.text if correct_option else None,
            message=f"Sorry, that's incorrect. The correct answer is {question.answer}) {correct_option.text if correct_option else ''}"
        )

@app.post("/quit")
async def quit_application():
    """
    Quit the application by terminating the process
    """
    # Return a response before terminating
    response = {"message": "Application is shutting down"}

    # Schedule the termination to happen after the response is sent
    # This is done by using os._exit(0) which immediately terminates the process
    # We use a separate thread to allow the response to be sent first
    import threading
    def terminate_app():
        import time
        time.sleep(1)  # Give the server time to send the response
        os._exit(0)  # Force terminate the process

    threading.Thread(target=terminate_app).start()

    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)