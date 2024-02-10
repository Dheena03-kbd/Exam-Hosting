// front-end/script.js
function createQuestion() {
    const questionText = document.getElementById('question-text').value;
    const options = document.getElementById('options').value.split(',');
    const correctOption = document.getElementById('correct-option').value;

    fetch('http://localhost:5001/questions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            text: questionText,
            options: options,
            correct_option: correctOption,
        }),
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
}

function createExam() {
    const duration = document.getElementById('exam-duration').value;
    const questions = document.getElementById('exam-questions').value.split(',');

    fetch('http://localhost:5002/exams', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            duration: duration,
            questions: questions,
        }),
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
}
