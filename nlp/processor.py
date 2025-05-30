import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize a local storage for questions and answers
qa_storage_path = os.getenv('QA_STORAGE_PATH', 'data/qa_storage.json')

# Load existing questions and answers from storage
if os.path.exists(qa_storage_path):
    with open(qa_storage_path, 'r') as file:
        qa_storage = json.load(file)
else:
    qa_storage = {}

def generate_answer(question):
    try:
        # Normalize the question for comparison
        normalized_question = question.strip().lower()
        if not normalized_question.endswith('?'):
            normalized_question += '?'

        # Check if the normalized question already exists in storage
        for entry in qa_storage.get("questions", []):
            if entry["question"].strip().lower() == normalized_question:
                return {"answer": entry["answer"]}
        
        # Prompt user to provide an answer for learning
        answer = input(f"No answer found for: '{question}'. Please provide an answer: ")
        
        # Store the new question and answer
        qa_storage.setdefault("questions", []).append({"question": question, "answer": answer})
        with open(qa_storage_path, 'w') as file:
            json.dump(qa_storage, file, indent=4)
        
        return {"answer": answer}
    except Exception as e:
        return {"answer": f"Error generating answer: {str(e)}"}
