from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import random

app = FastAPI()

# Enable CORS for all origins (replace with specific origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load questions from the JSON file
with open("questions.json", "r") as file:
    questions = json.load(file)

# Route to get all questions
@app.get("/get_all_questions")
def get_all_questions():
    return {"questions": questions}

# Route to check the user's answer
@app.post("/check_answer")
def check_answer(question: str, user_answer: str):
    for q in questions:
        if q["question"] == question:
            if q["answer"] == user_answer.lower():
                return {"result": "correct"}
            else:
                return {"result": "incorrect"}
    return {"result": "error: question not found"}

# Default route
@app.get("/")
def home():
    return {"message": "Welcome to the Rhyme Quiz API! Use /get_all_questions to get questions."}



