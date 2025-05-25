# Python Quiz Application

This project is a Python Quiz application with multiple interfaces:
1. A REST API implementation using FastAPI
2. A command-line interface (CLI)
3. A web-based user interface

## Features

- Get all available quiz questions
- Get a specific question by ID
- Get a random question
- Submit and validate answers
- Automatic API documentation with Swagger UI
- Command-line interface for interactive quizzes
- Web-based user interface for a visual quiz experience

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-quiz-api
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application in one of the following modes:

   a. REST API only:
   ```
   python run_server.py
   ```

   On Windows, you can use the provided batch file:
   ```
   run_app.bat
   ```

   For a complete setup that creates the virtual environment, installs dependencies, and runs the API:
   ```
   setup_and_run.bat
   ```

   Alternatively, you can use uvicorn directly:
   ```
   uvicorn main:app --reload
   ```

   The API will be available at http://localhost:8000

   b. Command-line interface (CLI):
   ```
   python python_quiz_chatbot.py
   ```

   This will start an interactive quiz in the terminal.

   c. Web-based user interface:
   ```
   python run_ui.py
   ```

   On Windows, you can use the provided batch file:
   ```
   run_ui.bat
   ```

   This will start both the API server and a web server for the frontend.
   The web UI will be available at http://localhost:8080

## API Documentation

Once the application is running, you can access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Endpoints

#### GET /

Returns a welcome message.

**Example:**
```bash
curl -X GET http://localhost:8000/
```

**Response:**
```json
{
  "message": "Welcome to the Python Quiz API"
}
```

#### GET /questions

Returns a list of all available quiz questions.

**Example:**
```bash
curl -X GET http://localhost:8000/questions
```

**Response:**
```json
[
  {
    "id": 1,
    "question": "What is the correct way to comment a single line in Python?",
    "options": [
      {"id": "a", "text": "// This is a comment"},
      {"id": "b", "text": "/* This is a comment */"},
      {"id": "c", "text": "# This is a comment"},
      {"id": "d", "text": "<!-- This is a comment -->"}
    ]
  },
  ...
]
```

#### GET /questions/random

Returns a random quiz question.

**Example:**
```bash
curl -X GET http://localhost:8000/questions/random
```

**Response:**
```json
{
  "id": 3,
  "question": "What is the output of print(2 + 3 * 4)?",
  "options": [
    {"id": "a", "text": "20"},
    {"id": "b", "text": "14"},
    {"id": "c", "text": "24"},
    {"id": "d", "text": "11"}
  ]
}
```

#### GET /questions/{question_id}

Returns a specific quiz question by ID.

**Example:**
```bash
curl -X GET http://localhost:8000/questions/2
```

**Response:**
```json
{
  "id": 2,
  "question": "Which of the following is used to define a function in Python?",
  "options": [
    {"id": "a", "text": "function"},
    {"id": "b", "text": "def"},
    {"id": "c", "text": "define"},
    {"id": "d", "text": "func"}
  ]
}
```

#### POST /questions/{question_id}/answer

Submit an answer for a specific question.

**Example:**
```bash
curl -X POST http://localhost:8000/questions/1/answer \
  -H "Content-Type: application/json" \
  -d '{"answer": "c"}'
```

**Response (correct answer):**
```json
{
  "correct": true,
  "message": "Correct! Well done!"
}
```

**Response (incorrect answer):**
```json
{
  "correct": false,
  "correct_answer": "c",
  "correct_option_text": "# This is a comment",
  "message": "Sorry, that's incorrect. The correct answer is c) # This is a comment"
}
```

## Command-Line Interface

The application includes a command-line interface (CLI) in the `python_quiz_chatbot.py` file. This CLI provides:

- An interactive quiz experience in the terminal
- Random questions from the quiz database
- Immediate feedback on answers
- Option to continue with more questions or exit

To use the CLI:

1. Run the CLI script:
   ```
   python python_quiz_chatbot.py
   ```

2. Follow the prompts to answer questions
3. Type the letter of your answer (a, b, c, or d)
4. Type 'quit' at any time to exit the quiz

## Web User Interface

The application includes a complete web-based user interface in the `frontend` directory. This UI provides:

- A welcome screen with options to start the quiz or view all questions
- Interactive quiz questions with multiple-choice options
- Immediate feedback on answers
- A results screen showing your score and performance
- A view of all available questions

To use the web UI:

1. Run the application in web UI mode as described in the Installation section:
   ```
   python run_ui.py
   ```
   or
   ```
   run_ui.bat
   ```

2. Open your browser to http://localhost:8080
3. Interact with the quiz through the user-friendly interface

## Custom Frontend Integration

If you want to build your own custom frontend application, you can integrate with the API:

1. Make API requests to the endpoints described above
2. Display questions and options to the user
3. Submit user answers to the answer endpoint
4. Display feedback based on the response

Example JavaScript fetch for getting a random question:
```javascript
fetch('http://localhost:8000/questions/random')
  .then(response => response.json())
  .then(data => {
    // Display the question and options to the user
    console.log(data);
  });
```

Example JavaScript fetch for submitting an answer:
```javascript
fetch(`http://localhost:8000/questions/1/answer`, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ answer: 'c' }),
})
  .then(response => response.json())
  .then(data => {
    // Display feedback to the user
    console.log(data);
  });
```

## Testing

To test the API endpoints, you can use the included test script:

```bash
python test_api.py
```

On Windows, you can use the provided batch file:
```
run_tests.bat
```

This script will:
1. Test all API endpoints
2. Verify correct responses
3. Display detailed information about each test

Make sure the API server is running before executing the test script.

## License

[MIT License](LICENSE)
