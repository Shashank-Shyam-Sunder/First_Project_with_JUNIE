@echo off
echo Starting Python Quiz Web UI...
cd ..
call .venv\Scripts\activate
.venv\Scripts\python src\launcher.py ui
