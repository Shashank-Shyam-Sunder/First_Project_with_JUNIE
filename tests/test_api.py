import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:8000"

def test_welcome_endpoint():
    """Test the welcome endpoint"""
    response = requests.get(f"{BASE_URL}/")
    data = response.json()
    
    print("Testing welcome endpoint:")
    print(f"Status code: {response.status_code}")
    print(f"Response: {json.dumps(data, indent=2)}")
    print("-----------------------------------")
    
    assert response.status_code == 200
    assert "message" in data

def test_get_all_questions():
    """Test getting all questions"""
    response = requests.get(f"{BASE_URL}/questions")
    data = response.json()
    
    print("Testing get all questions endpoint:")
    print(f"Status code: {response.status_code}")
    print(f"Number of questions: {len(data)}")
    print("-----------------------------------")
    
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_random_question():
    """Test getting a random question"""
    response = requests.get(f"{BASE_URL}/questions/random")
    data = response.json()
    
    print("Testing get random question endpoint:")
    print(f"Status code: {response.status_code}")
    print(f"Question ID: {data.get('id')}")
    print(f"Question: {data.get('question')}")
    print("-----------------------------------")
    
    assert response.status_code == 200
    assert "id" in data
    assert "question" in data
    assert "options" in data

def test_get_specific_question():
    """Test getting a specific question by ID"""
    question_id = 1
    response = requests.get(f"{BASE_URL}/questions/{question_id}")
    data = response.json()
    
    print(f"Testing get question {question_id} endpoint:")
    print(f"Status code: {response.status_code}")
    print(f"Question: {data.get('question')}")
    print("-----------------------------------")
    
    assert response.status_code == 200
    assert data["id"] == question_id

def test_submit_correct_answer():
    """Test submitting a correct answer"""
    question_id = 1  # Question about Python comments
    answer = "c"     # Correct answer is 'c'
    
    response = requests.post(
        f"{BASE_URL}/questions/{question_id}/answer",
        json={"answer": answer}
    )
    data = response.json()
    
    print("Testing submit correct answer endpoint:")
    print(f"Status code: {response.status_code}")
    print(f"Response: {json.dumps(data, indent=2)}")
    print("-----------------------------------")
    
    assert response.status_code == 200
    assert data["correct"] is True

def test_submit_incorrect_answer():
    """Test submitting an incorrect answer"""
    question_id = 1  # Question about Python comments
    answer = "a"     # Incorrect answer
    
    response = requests.post(
        f"{BASE_URL}/questions/{question_id}/answer",
        json={"answer": answer}
    )
    data = response.json()
    
    print("Testing submit incorrect answer endpoint:")
    print(f"Status code: {response.status_code}")
    print(f"Response: {json.dumps(data, indent=2)}")
    print("-----------------------------------")
    
    assert response.status_code == 200
    assert data["correct"] is False
    assert "correct_answer" in data
    assert "correct_option_text" in data

def run_all_tests():
    """Run all tests"""
    print("Running API tests...\n")
    
    try:
        test_welcome_endpoint()
        test_get_all_questions()
        test_get_random_question()
        test_get_specific_question()
        test_submit_correct_answer()
        test_submit_incorrect_answer()
        
        print("\nAll tests passed successfully!")
    except AssertionError as e:
        print(f"\nTest failed: {e}")
    except requests.exceptions.ConnectionError:
        print("\nConnection error: Make sure the API server is running at http://localhost:8000")

if __name__ == "__main__":
    print("Python Quiz API Test Script")
    print("==========================")
    print("This script tests all endpoints of the Python Quiz API.")
    print("Make sure the API server is running before executing this script.")
    print("To start the server, run: python -m api.run_server")
    print("==========================\n")
    
    run_all_tests()