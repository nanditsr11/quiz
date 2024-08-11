document.addEventListener('DOMContentLoaded', () => {
    let totalQuestions = 0;
    let correctAnswers = 0;
    let currentQuestion = {};

    function fetchQuestion() {
        fetch('/get_question')
            .then(response => response.json())
            .then(data => {
                currentQuestion = data;
                displayQuestion(data);
            });
    }

    function displayQuestion(question) {
        const questionEl = document.getElementById('question');
        const choicesEl = document.getElementById('choices');
        const submitBtn = document.getElementById('submit-btn');
        questionEl.textContent = question.question;
        choicesEl.innerHTML = '';

        question.choices.forEach(choice => {
            const choiceEl = document.createElement('button');
            choiceEl.textContent = choice;
            choiceEl.classList.add('choice');
            choiceEl.addEventListener('click', () => {
                document.querySelectorAll('.choice').forEach(btn => btn.classList.remove('selected'));
                choiceEl.classList.add('selected');
                submitBtn.disabled = false;
            });
            choicesEl.appendChild(choiceEl);
        });

        submitBtn.disabled = true;
        submitBtn.addEventListener('click', () => {
            const selectedChoice = document.querySelector('.choice.selected');
            if (selectedChoice) {
                checkAnswer(selectedChoice.textContent);
            }
        });
    }

    function checkAnswer(choice) {
        fetch('/check_answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_answer: choice, correct_answer: currentQuestion.correct_answer })
        })
        .then(response => response.json())
        .then(data => {
            totalQuestions++;
            if (data.is_correct) {
                correctAnswers++;
            } else {
                gameOver(data.correct_answer);
                return;
            }
            fetchQuestion();
        });
    }

    function gameOver(correctAnswer) {
        document.getElementById('quiz-container').style.display = 'none';
        const summary = `You answered ${correctAnswers} out of ${totalQuestions} questions correctly. (${((correctAnswers / totalQuestions) * 100).toFixed(2)}%)`;
        document.getElementById('summary').textContent = summary + `\nThe correct answer was: ${correctAnswer}`;
        document.getElementById('results-container').style.display = 'block';
    }

    fetchQuestion();
});
