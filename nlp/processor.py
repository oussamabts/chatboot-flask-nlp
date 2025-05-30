import os
import json
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Load environment variables
load_dotenv()

# Initialize a local storage for questions and answers
qa_storage_path = os.getenv('QA_STORAGE_PATH', 'data/qa_storage.json')
serpapi_api_key = os.getenv('SERPAPI_API_KEY') 

# Load existing questions and answers from storage
if os.path.exists(qa_storage_path):
    with open(qa_storage_path, 'r') as file:
        qa_storage = json.load(file)
else:
    qa_storage = {}

def fetch_answer_from_google(question):
    try:
        search = GoogleSearch({"q": question, "api_key": serpapi_api_key})
        results = search.get_dict()
        answer = results.get("answer_box", {}).get("answer") or results.get("organic_results", [{}])[0].get("snippet")
        return answer
    except Exception as e:
        return f"Error fetching answer from Google: {str(e)}"

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
        
        # Fetch answer from Google if not found locally
        answer = fetch_answer_from_google(question)
        if not answer:
            answer = input(f"No answer found for: '{question}'. Please provide an answer: ")

        # Store the new question and answer
        qa_storage.setdefault("questions", []).append({"question": question, "answer": answer})
        with open(qa_storage_path, 'w') as file:
            json.dump(qa_storage, file, indent=4)
        
        return {"answer": answer}
    except Exception as e:
        return {"answer": f"Error generating answer: {str(e)}"}
