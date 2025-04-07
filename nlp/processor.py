import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Initialize the model using a free-tier-supported model
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

def generate_answer(question):
    try:
        # Educational prompt
        prompt = f"""You are an educational assistant. Please provide a clear and educational response to the following question.
        Question: {question}
        
        Please provide a detailed, accurate, and educational response. If the question is not educational in nature, 
        kindly redirect the user to ask an educational question."""
        
        # Generate response
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating answer: {str(e)}"
