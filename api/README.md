# API Directory

This directory contains the backend API for the Python Quiz application.

## Files

- `main.py`: The FastAPI application that defines the API endpoints.
- `models.py`: The Pydantic models used by the API.
- `run_server.py`: A script to start the API server.

## Usage

The API can be started directly from this directory:

```bash
python run_server.py
```

Or from the root directory using the main entry point:

```bash
python main.py api
```

## API Endpoints

- `GET /`: Welcome message
- `GET /questions`: Get all questions
- `GET /questions/random`: Get a random question
- `GET /questions/{question_id}`: Get a specific question by ID
- `POST /questions/{question_id}/answer`: Submit an answer for a question
- `POST /quit`: Quit the application