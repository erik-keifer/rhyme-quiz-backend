# Import the JSON module
import json

# Load the JSON file
with open("questions.json", "r") as file:
    questions = json.load(file)

# Print the loaded questions
for question in questions:
    print(f"Question: {question['question']}, Answer: {question['answer']}")

