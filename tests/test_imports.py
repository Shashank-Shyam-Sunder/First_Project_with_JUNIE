from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import requests

print("All imports successful!")

# Try to import the application modules
from api.models import Question, QuestionOption, QuestionResponse, AnswerRequest, AnswerResponse
from api.main import app

print("Application modules imported successfully!")
print("FastAPI application created successfully!")