try:
    # Import the application modules
    from api.models import Question, QuestionOption, QuestionResponse, AnswerRequest, AnswerResponse
    from api.main import app
    
    # Print success message
    print("Application modules imported successfully!")
    print("FastAPI application created successfully!")
    print("All dependencies are properly installed.")
    print("The application should be ready to run with 'python -m api.run_server'")
    
except ImportError as e:
    print(f"Import error: {e}")
    print("Some dependencies might be missing. Try reinstalling from requirements.txt")
    
except Exception as e:
    print(f"Error: {e}")
    print("There might be an issue with the application code.")