"""
Python Quiz Chatbot

This program implements a simple chatbot that asks the user beginner-level
Python questions, accepts their answers, and provides feedback on whether
the response is correct.
"""

def main():
    # Define a list of questions with their answers and options
    questions = [
        {
            "question": "What is the correct way to comment a single line in Python?",
            "options": ["a) // This is a comment", "b) /* This is a comment */", "c) # This is a comment", "d) <!-- This is a comment -->"],
            "answer": "c"
        },
        {
            "question": "Which of the following is used to define a function in Python?",
            "options": ["a) function", "b) def", "c) define", "d) func"],
            "answer": "b"
        },
        {
            "question": "What is the output of print(2 + 3 * 4)?",
            "options": ["a) 20", "b) 14", "c) 24", "d) 11"],
            "answer": "b"
        },
        {
            "question": "Which data type is used to store a sequence of items in Python?",
            "options": ["a) list", "b) integer", "c) float", "d) boolean"],
            "answer": "a"
        },
        {
            "question": "How do you create a variable named 'age' with the value 25?",
            "options": ["a) var age = 25", "b) age := 25", "c) age = 25", "d) int age = 25"],
            "answer": "c"
        }
    ]
    
    print("Welcome to the Python Quiz Chatbot!")
    print("I'll ask you some beginner-level Python questions.")
    print("Type the letter of your answer (a, b, c, or d).")
    print("Type 'quit' at any time to exit the chat.")
    print()
    
    # Main loop
    while True:
        # Randomly select a question
        import random
        question_data = random.choice(questions)
        
        # Display the question and options
        print(question_data["question"])
        for option in question_data["options"]:
            print(option)
        
        # Get user input
        user_answer = input("Your answer: ").lower().strip()
        
        # Check if user wants to quit
        if user_answer == "quit":
            print("Thank you for using the Python Quiz Chatbot. Goodbye!")
            break
        
        # Check if the answer is correct
        if user_answer == question_data["answer"]:
            print("Correct! Well done!\n")
        else:
            correct_option = question_data["options"][ord(question_data["answer"]) - ord('a')]
            print(f"Sorry, that's incorrect. The correct answer is {question_data['answer']}) {correct_option.split(') ')[1]}\n")
        
        # Ask if the user wants to continue
        continue_quiz = input("Would you like another question? (yes/no): ").lower().strip()
        if continue_quiz != "yes" and continue_quiz != "y":
            print("Thank you for using the Python Quiz Chatbot. Goodbye!")
            break
        
        print()  # Add a blank line for better readability

if __name__ == "__main__":
    main()