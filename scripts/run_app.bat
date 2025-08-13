@echo off
echo Starting Python Quiz API server...
echo The API will be available at http://localhost:8000
echo API documentation will be available at http://localhost:8000/docs
echo Press Ctrl+C to stop the server
echo.
cd ..
.venv\Scripts\python src\launcher.py api
