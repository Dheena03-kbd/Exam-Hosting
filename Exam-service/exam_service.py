from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

exam_questions = []

@app.route('/exams', methods=['POST'])
def create_exam():
    data = request.get_json()
    questions = data.get('questions', [])
    exam = {
        'id': len(exam_questions) + 1,
        'questions': questions,
        'duration': data['duration']
    }
    exam_questions.append(exam)
    return jsonify({'message': 'Exam created successfully', 'exam_id': exam['id']}), 201

@app.route('/exams/<int:exam_id>', methods=['GET'])
def get_exam(exam_id):
    exam = next((e for e in exam_questions if e['id'] == exam_id), None)
    if exam:
        return jsonify(exam)
    return jsonify({'message': 'Exam not found'}), 404

if __name__ == '__main__':
    app.run(port=5002)
