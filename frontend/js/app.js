/**
 * Main Application for Python Quiz
 * Handles UI interactions and quiz logic
 */

document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const welcomeScreen = document.getElementById('welcome-screen');
    const questionScreen = document.getElementById('question-screen');
    const resultScreen = document.getElementById('result-screen');
    const allQuestionsScreen = document.getElementById('all-questions-screen');
    const feedbackContainer = document.getElementById('feedback-container');

    const questionText = document.getElementById('question-text');
    const optionsContainer = document.getElementById('options-container');
    const questionNumber = document.getElementById('question-number');
    const scoreValue = document.getElementById('score-value');
    const percentageValue = document.getElementById('percentage-value');
    const resultMessage = document.getElementById('result-message');
    const questionsList = document.getElementById('questions-list');

    // Buttons
    const startQuizBtn = document.getElementById('start-quiz');
    const viewAllBtn = document.getElementById('view-all');
    const submitAnswerBtn = document.getElementById('submit-answer');
    const nextQuestionBtn = document.getElementById('next-question');
    const restartQuizBtn = document.getElementById('restart-quiz');
    const viewAllFromResultsBtn = document.getElementById('view-all-from-results');
    const backToWelcomeBtn = document.getElementById('back-to-welcome');
    const quitQuizBtn = document.getElementById('quit-quiz');
    const quitFromQuestionBtn = document.getElementById('quit-from-question');
    const quitFromResultsBtn = document.getElementById('quit-from-results');

    // Quiz State
    let currentQuestions = [];
    let currentQuestionIndex = 0;
    let selectedOption = null;
    let score = 0;
    let answeredQuestions = new Set();

    // Initialize the application
    function init() {
        attachEventListeners();
    }

    // Attach event listeners to buttons
    function attachEventListeners() {
        startQuizBtn.addEventListener('click', startQuiz);
        viewAllBtn.addEventListener('click', viewAllQuestions);
        submitAnswerBtn.addEventListener('click', submitAnswer);
        nextQuestionBtn.addEventListener('click', showNextQuestion);
        restartQuizBtn.addEventListener('click', startQuiz);
        viewAllFromResultsBtn.addEventListener('click', viewAllQuestions);
        backToWelcomeBtn.addEventListener('click', showWelcomeScreen);

        // Add event listeners for quit buttons
        quitQuizBtn.addEventListener('click', quitQuiz);
        quitFromQuestionBtn.addEventListener('click', quitQuiz);
        quitFromResultsBtn.addEventListener('click', quitQuiz);
    }

    // Quit the quiz application
    async function quitQuiz() {
        try {
            // Show a confirmation dialog
            if (confirm('Are you sure you want to quit the quiz? This will close the application.')) {
                // Call the API to quit the application
                await ApiService.quitQuiz();
                // Close the window (this may not work in all browsers due to security restrictions)
                window.close();
            }
        } catch (error) {
            showError('Failed to quit quiz: ' + error.message);
            // Try to close the window anyway
            window.close();
        }
    }

    // Show only the specified screen
    function showScreen(screen) {
        welcomeScreen.classList.remove('active');
        questionScreen.classList.remove('active');
        resultScreen.classList.remove('active');
        allQuestionsScreen.classList.remove('active');

        screen.classList.add('active');
    }

    // Show welcome screen
    function showWelcomeScreen() {
        showScreen(welcomeScreen);
    }

    // Start the quiz
    async function startQuiz() {
        try {
            // Reset quiz state
            currentQuestionIndex = 0;
            score = 0;
            answeredQuestions.clear();

            // Fetch all questions
            currentQuestions = await ApiService.getAllQuestions();

            if (currentQuestions.length === 0) {
                showError('No questions available');
                return;
            }

            // Show the first question
            showQuestion(currentQuestions[0]);
            showScreen(questionScreen);
        } catch (error) {
            showError('Failed to start quiz: ' + error.message);
        }
    }

    // Show a specific question
    function showQuestion(question) {
        // Update question text and number
        questionText.textContent = question.question;
        questionNumber.textContent = `Question ${currentQuestionIndex + 1}/${currentQuestions.length}`;

        // Clear previous options and selected option
        optionsContainer.innerHTML = '';
        selectedOption = null;

        // Hide the next button and feedback
        nextQuestionBtn.classList.add('hidden');
        feedbackContainer.classList.add('hidden');

        // Enable submit button
        submitAnswerBtn.disabled = false;

        // Create option elements
        question.options.forEach(option => {
            const optionElement = document.createElement('div');
            optionElement.className = 'option';
            optionElement.dataset.id = option.id;

            const optionId = document.createElement('span');
            optionId.className = 'option-id';
            optionId.textContent = option.id.toUpperCase();

            const optionText = document.createElement('span');
            optionText.className = 'option-text';
            optionText.textContent = option.text;

            optionElement.appendChild(optionId);
            optionElement.appendChild(optionText);

            // Add click event to select option
            optionElement.addEventListener('click', () => selectOption(optionElement, option.id));

            optionsContainer.appendChild(optionElement);
        });
    }

    // Select an option
    function selectOption(optionElement, optionId) {
        // If already submitted, don't allow selection
        if (submitAnswerBtn.disabled) return;

        // Remove selected class from all options
        const options = optionsContainer.querySelectorAll('.option');
        options.forEach(opt => opt.classList.remove('selected'));

        // Add selected class to clicked option
        optionElement.classList.add('selected');

        // Update selected option
        selectedOption = optionId;
    }

    // Submit the answer
    async function submitAnswer() {
        if (!selectedOption) {
            showFeedback('Please select an option', false);
            return;
        }

        try {
            const currentQuestion = currentQuestions[currentQuestionIndex];
            const response = await ApiService.submitAnswer(currentQuestion.id, selectedOption);

            // Disable submit button
            submitAnswerBtn.disabled = true;

            // Show feedback
            showFeedback(response.message, response.correct);

            // Update score if correct
            if (response.correct) {
                score++;
            }

            // Mark question as answered
            answeredQuestions.add(currentQuestion.id);

            // Show correct/incorrect styling
            const options = optionsContainer.querySelectorAll('.option');
            options.forEach(opt => {
                if (opt.dataset.id === selectedOption) {
                    opt.classList.add(response.correct ? 'correct' : 'incorrect');
                }
                if (!response.correct && opt.dataset.id === response.correct_answer) {
                    opt.classList.add('correct');
                }
            });

            // Show next button if not the last question
            if (currentQuestionIndex < currentQuestions.length - 1) {
                nextQuestionBtn.classList.remove('hidden');
            } else {
                // If last question, show finish button
                nextQuestionBtn.textContent = 'Finish Quiz';
                nextQuestionBtn.classList.remove('hidden');
            }
        } catch (error) {
            showError('Failed to submit answer: ' + error.message);
        }
    }

    // Show the next question
    function showNextQuestion() {
        currentQuestionIndex++;

        if (currentQuestionIndex < currentQuestions.length) {
            // Show next question
            showQuestion(currentQuestions[currentQuestionIndex]);
            nextQuestionBtn.textContent = 'Next Question';
        } else {
            // End of quiz, show results
            showResults();
        }
    }

    // Show quiz results
    function showResults() {
        scoreValue.textContent = score;
        const percentage = Math.round((score / currentQuestions.length) * 100);
        percentageValue.textContent = percentage;

        // Set result message based on score
        if (percentage >= 80) {
            resultMessage.textContent = 'Excellent! You have a great understanding of Python!';
        } else if (percentage >= 60) {
            resultMessage.textContent = 'Good job! You have a solid understanding of Python.';
        } else if (percentage >= 40) {
            resultMessage.textContent = 'Not bad, but you might want to review some Python concepts.';
        } else {
            resultMessage.textContent = 'You should spend more time learning Python basics.';
        }

        showScreen(resultScreen);
    }

    // View all questions
    async function viewAllQuestions() {
        try {
            // Fetch all questions if not already loaded
            if (currentQuestions.length === 0) {
                currentQuestions = await ApiService.getAllQuestions();
            }

            // Clear previous questions
            questionsList.innerHTML = '';

            // Create elements for each question
            currentQuestions.forEach((question, index) => {
                const questionItem = document.createElement('div');
                questionItem.className = 'question-item';

                const questionHeader = document.createElement('h3');
                questionHeader.textContent = `${index + 1}. ${question.question}`;

                const optionsList = document.createElement('div');
                optionsList.className = 'options-list';

                question.options.forEach(option => {
                    const optionItem = document.createElement('div');
                    optionItem.className = 'option';

                    const optionId = document.createElement('span');
                    optionId.className = 'option-id';
                    optionId.textContent = option.id.toUpperCase();

                    const optionText = document.createElement('span');
                    optionText.className = 'option-text';
                    optionText.textContent = option.text;

                    optionItem.appendChild(optionId);
                    optionItem.appendChild(optionText);
                    optionsList.appendChild(optionItem);
                });

                questionItem.appendChild(questionHeader);
                questionItem.appendChild(optionsList);
                questionsList.appendChild(questionItem);
            });

            showScreen(allQuestionsScreen);
        } catch (error) {
            showError('Failed to load questions: ' + error.message);
        }
    }

    // Show feedback message
    function showFeedback(message, isSuccess) {
        feedbackContainer.textContent = message;
        feedbackContainer.className = 'feedback-container';
        feedbackContainer.classList.add(isSuccess ? 'success' : 'error');
        feedbackContainer.classList.remove('hidden');
    }

    // Show error message
    function showError(message) {
        console.error(message);
        showFeedback(message, false);
    }

    // Initialize the application
    init();
});
