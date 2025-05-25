"""
Python Quiz Application

This is the main entry point for the Python Quiz application.
It provides options to run the application in different modes:
- API server mode
- Web UI mode
- Command-line interface mode
"""

import sys
import os

def print_usage():
    """Print usage instructions"""
    print("Python Quiz Application")
    print("======================")
    print("Usage:")
    print("  python main.py [mode]")
    print()
    print("Available modes:")
    print("  api     - Start the API server only")
    print("  ui      - Start the web UI (includes API server)")
    print("  cli     - Start the command-line interface")
    print("  test    - Run the API tests")
    print("  verify  - Verify the application setup")
    print()
    print("If no mode is specified, this help message is displayed.")

def main():
    """Main entry point for the application"""
    # Check if a mode was specified
    if len(sys.argv) < 2:
        print_usage()
        return

    # Get the mode from command line arguments
    mode = sys.argv[1].lower()

    # Execute the appropriate mode
    if mode == "api":
        print("Starting API server mode...")
        from api import run_server
        # The run_server module will handle execution

    elif mode == "ui":
        print("Starting Web UI mode...")
        from utils import run_ui
        # The run_ui module will handle execution

    elif mode == "cli":
        print("Starting command-line interface mode...")
        from cli import python_quiz_chatbot
        python_quiz_chatbot.main()

    elif mode == "test":
        print("Running API tests...")
        from tests import test_api
        test_api.run_all_tests()

    elif mode == "verify":
        print("Verifying application setup...")
        from tests import verify_app
        # The verify_app module will handle execution

    else:
        print(f"Unknown mode: {mode}")
        print_usage()

if __name__ == "__main__":
    main()
