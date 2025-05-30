# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from nlp.processor import generate_answer

app = Flask(__name__)
CORS(app)

@app.route('/nlp/asks', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question')

    if not question:
        return jsonify({'error': 'Question is required'}), 400

    # Normalize the question
    question = question.strip()
    if not question.endswith('?'):
        question += '?'

    # Call generate_answer and return its output
    response = generate_answer(question)
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='192.168.11.232', port=5000, debug=True)
