# Step 1: Define a list of dictionaries for questions, options, and correct answers
quiz_data = [
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Tokyo", "B. Seoul", "C. Beijing", "D. Bangkok"],
        "answer": "A",
        "explanation": "The capital of Japan is Tokyo."
    },
    {
        "question": "Which element is represented by the symbol 'O'?",
        "options": ["A. Oxygen", "B. Gold", "C. Silver", "D. Hydrogen"],
        "answer": "A",
        "explanation": "'O' represents Oxygen in the periodic table."
    },
    {
        "question": "Which of the following is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "B",
        "explanation": "Jupiter is the largest planet in our solar system."
    }
]

# Function to display questions and options
def display_question(question_data):
    print("\n" + question_data["question"])
    for option in question_data["options"]:
        print(option)

# Function to validate user input
def get_user_answer():
    user_answer = input("Your answer (A/B/C/D): ").upper().strip()
    
    # Validate input to ensure user enters a valid option
    while user_answer not in ['A', 'B', 'C', 'D']:
        print("Invalid input! Please choose A, B, C, or D.")
        user_answer = input("Your answer (A/B/C/D): ").upper().strip()
    
    return user_answer

# Function to check if the answer is correct and give feedback
def check_answer(user_answer, question_data):
    if user_answer == question_data["answer"]:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! {question_data['explanation']}")
        return False

# Function to run the quiz
def run_quiz():
    print("Welcome to the Quiz Game!")
    score = 0
    total_questions = len(quiz_data)

    # Step 2: Iterate through each question
    for question_data in quiz_data:
        display_question(question_data)
        user_answer = get_user_answer()
        is_correct = check_answer(user_answer, question_data)
        
        # Step 3: Update the score based on whether the answer was correct
        if is_correct:
            score += 1

    # Step 4: Display the final score
    print(f"\nQuiz completed! Your final score is {score}/{total_questions}.")

    # Provide feedback based on the final score
    if score == total_questions:
        print("Excellent! You got all the questions correct!")
    elif score >= total_questions // 2:
        print("Good job! You got more than half of the questions right.")
    else:
        print("Keep trying! Practice makes perfect.")

# Step 5: Start the quiz
run_quiz()
