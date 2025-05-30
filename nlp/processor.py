import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize a local storage for questions and answers
qa_storage_path = os.getenv('QA_STORAGE_PATH', 'qa_storage.json')

# Load existing questions and answers from storage
if os.path.exists(qa_storage_path):
    with open(qa_storage_path, 'r') as file:
        qa_storage = json.load(file)
else:
    qa_storage = {}

def generate_answer(question):
    try:
        # Check if the question already exists in storage
        if question in qa_storage:
            return qa_storage[question]
        
        # Prompt user to provide an answer for learning
        answer = input(f"No answer found for: '{question}'. Please provide an answer: ")
        
        # Store the new question and answer
        qa_storage[question] = answer
        with open(qa_storage_path, 'w') as file:
            json.dump(qa_storage, file)
        
        return answer
    except Exception as e:
        return f"Error generating answer: {str(e)}"
