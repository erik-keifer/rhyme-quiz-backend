from fastapi import FastAPI
import json

app = FastAPI()

# Load the questions from the JSON file
with open("questions.json", "r") as file:
    questions = json.load(file)

# Route to get all questions
@app.get("/get_all_questions")
def get_all_questions():
    return {"questions": questions}

# Route to get a random question
@app.get("/get_question")
def get_question():
    import random
    return random.choice(questions)

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
