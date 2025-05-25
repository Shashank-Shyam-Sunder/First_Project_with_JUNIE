# Tests Directory

This directory contains tests and verification scripts for the Python Quiz application.

## Files

- `test_api.py`: Tests for the API endpoints.
- `test_imports.py`: Tests that all required modules can be imported.
- `verify_app.py`: Verifies that the application is set up correctly.

## Usage

The tests can be run directly from this directory:

```bash
python test_api.py
```

Or from the root directory using the main entry point:

```bash
python main.py test
```

To verify the application setup:

```bash
python main.py verify
```

## Notes

- Make sure the API server is running before running the API tests.
- The verification script checks that all required dependencies are installed and that the application modules can be imported.