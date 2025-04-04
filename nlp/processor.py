from transformers import pipeline

qa_pipeline = pipeline("question-answering")

def generate_answer(question, context="This is a basic educational assistant bot."):
    try:
        result = qa_pipeline(question=question, context=context)
        return result['answer']
    except Exception as e:
        return f"Error generating answer: {str(e)}"