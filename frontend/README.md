# Python Quiz Frontend

This is the frontend interface for the Python Quiz REST API. It provides a user-friendly way to interact with the quiz application.

## Features

- Interactive quiz interface
- View all questions at once
- Real-time feedback on answers
- Score tracking and results summary
- Responsive design for all device sizes

## Setup

1. Make sure the Python Quiz REST API is running on http://localhost:8000
   ```
   python run_server.py
   ```
   
2. Open the frontend application by opening the `index.html` file in your web browser:
   - Double-click on the `index.html` file
   - Or open it via your browser's File > Open menu

## Usage

1. **Home Screen**
   - Click "Start Quiz" to begin the quiz
   - Click "View All Questions" to see all available questions

2. **Quiz Screen**
   - Read the question and select an answer
   - Click "Submit Answer" to check your answer
   - After submitting, click "Next Question" to proceed

3. **Results Screen**
   - View your final score and percentage
   - Read feedback based on your performance
   - Choose to restart the quiz or view all questions

## Technical Details

The frontend is built using:
- HTML5 for structure
- CSS3 for styling
- JavaScript (ES6+) for functionality

It communicates with the backend API using the Fetch API for:
- Retrieving questions
- Submitting answers
- Checking answer correctness

## Browser Compatibility

The application is compatible with all modern browsers:
- Chrome (recommended)
- Firefox
- Safari
- Edge

## Troubleshooting

If you encounter issues:

1. Make sure the backend API is running on http://localhost:8000
2. Check your browser console for any JavaScript errors
3. Ensure you have an active internet connection
4. Try clearing your browser cache and reloading the page