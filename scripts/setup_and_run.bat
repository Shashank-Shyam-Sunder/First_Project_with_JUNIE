@echo off
echo Setting up and running Python Quiz API...
cd ..

REM Check if virtual environment exists
if not exist .venv (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment and install dependencies
echo Activating virtual environment and installing dependencies...
call .venv\Scripts\activate.bat
pip install -r requirements.txt

REM Verify application
echo Verifying application...
python src\launcher.py verify

REM Run the application
echo Starting the application...
echo The API will be available at http://localhost:8000
echo API documentation will be available at http://localhost:8000/docs
echo Press Ctrl+C to stop the server
python src\launcher.py api
