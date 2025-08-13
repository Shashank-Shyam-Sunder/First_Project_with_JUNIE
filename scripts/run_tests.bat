@echo off
echo Running Python Quiz API tests...
echo Make sure the API server is running at http://localhost:8000
echo.
cd ..
.venv\Scripts\python src\launcher.py test
