import os
import subprocess
import threading
import webbrowser
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler

def run_api_server():
    """Run the FastAPI server in a separate process"""
    print("Starting Python Quiz API server...")
    print("The API will be available at http://localhost:8000")
    print("API documentation will be available at http://localhost:8000/docs")
    
    # Use subprocess to run the API server
    subprocess.Popen(["venv\\Scripts\\python", "-m", "api.run_server"], 
                    creationflags=subprocess.CREATE_NEW_CONSOLE)

def run_frontend_server():
    """Run a simple HTTP server to serve the frontend files"""
    # Change to the frontend directory
    os.chdir("frontend")
    
    # Create an HTTP server
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    print("Starting frontend server...")
    print("The frontend will be available at http://localhost:8080")
    print("Press Ctrl+C to stop the server")
    
    # Start the server
    httpd.serve_forever()

def open_browser():
    """Open the browser to the frontend URL after a short delay"""
    time.sleep(2)  # Wait for servers to start
    webbrowser.open('http://localhost:8080')

if __name__ == "__main__":
    print("Starting Python Quiz Application in UI mode...")
    
    # Start the API server
    run_api_server()
    
    # Open the browser after a short delay
    threading.Thread(target=open_browser).start()
    
    # Run the frontend server (this will block until the server is stopped)
    run_frontend_server()