from flask import Flask, request, jsonify

app = Flask(__name__)

questions = []

@app.route('/questions', methods=['POST'])
def create_question():
    data = request.get_json()
    question = {
        'id': len(questions) + 1,
        'text': data['text'],
        'options': data['options'],
        'correct_option': data['correct_option']
    }
    questions.append(question)
    return jsonify({'message': 'Question created successfully', 'question_id': question['id']}), 201

@app.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = next((q for q in questions if q['id'] == question_id), None)
    if question:
        return jsonify(question)
    return jsonify({'message': 'Question not found'}), 404

if __name__ == '__main__':
    app.run(port=5001)
