import random # to enable shuffling
import time # to enable the timer

# Quiz data categorized by topics
quiz_data = {
    "General Knowledge": [
        {
            "question": "Which country has the highest life expectancy?",
            "options": ["A. Japan", "B. Hong Kong", "C. South Korea", "D. China"],
            "correct": "B"
        },
        {
            "question": "Aureolin is a shade of what color?",
            "options": ["A. Blue", "B. Red", "C. Yellow", "D. Green"],
            "correct": "C"
        },
        {
            "question": "How many dots appear on a pair of dice?",
            "options": ["A. 42", "B. 16", "C. 43", "D. 28"],
            "correct": "A"
        },
        {
            "question": "What is the largest Spanish-speaking city in the world?",
            "options": ["A. Barcelona", "B. Mexico City", "C. Madrid", "D. Havana"],
            "correct": "B"
        },
        {
            "question": "Which is the only continent with land in all four hemispheres?",
            "options": ["A. Oceania", "B. Asia", "C. South America", "D. Africa"],
            "correct": "D"
        }
    ],
    "Math": [
        {
            "question": "What is the square root of 64?",
            "options": ["A. 6", "B. 8", "C. 7", "D. 9"],
            "correct": "B"
        },
        {
            "question": "What is 7 * 6?",
            "options": ["A. 42", "B. 36", "C. 48", "D. 40"],
            "correct": "A"
        },
        {
            "question": "What is the value of pi (approx)?",
            "options": ["A. 3.14", "B. 3.41", "C. 3.04", "D. 4.13"],
            "correct": "A"
        }
    ]
}

def quiz_game():
    print("Quiz Game")
    print("Choose a category:")
    categories = list(quiz_data.keys())

    for idx, cat in enumerate(categories, start=1):
        print(f"{idx}. {cat}")

    while True:
        try:
            cat_choice = int(input("Enter category number: "))
            if not 1 <= cat_choice <= len(categories):
                raise ValueError("Invalid number")
            break
        except ValueError:
            print("Please enter a valid number corresponding to a category.")

    selected_category = categories[cat_choice - 1]
    questions = quiz_data[selected_category]
    random.shuffle(questions)

    score = 0
    print(f"\nStarting quiz on: {selected_category}")
    print("You have 10 seconds to answer each question!\n")

    for i, item in enumerate(questions):
        print(f"Question {i + 1}: {item['question']}")
        for option in item['options']:
            print(option)

        start_time = time.time()
        try:
            user_input = input("Your answer (A, B, C, or D): ").strip().upper()
            if time.time() - start_time > 10:
                raise TimeoutError
            if user_input not in ['A', 'B', 'C', 'D']:
                raise ValueError("Invalid choice.")
        except TimeoutError:
            print("⏰ Time's up! Moving to the next question.\n")
            continue
        except ValueError as e:
            print(f"{e} Skipping this question.\n")
            continue

        if user_input == item["correct"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {item['correct']}.\n")

    total = len(questions)
    print("Quiz Completed :)")
    print(f"Your final score: {score}/{total}")

    percentage = (score / total) * 100
    if percentage == 100:
        print("🎉 Excellent! You got everything right!")
    elif percentage >= 60:
        print("👍 Good job!")
    else:
        print("😕 Try again. Practice makes perfect!")

# Run the quiz
quiz_game()
