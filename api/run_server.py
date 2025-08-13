import uvicorn
from api.main import app

if __name__ == "__main__":
    print("Starting Python Quiz API server...")
    print("The API will be available at http://localhost:8000")
    print("API documentation will be available at http://localhost:8000/docs")
    print("Press Ctrl+C to stop the server")
    
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)