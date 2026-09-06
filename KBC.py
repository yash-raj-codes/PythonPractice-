""" Create a program capable of displaying questions to the user like KBC"""
# 1. Questions, Options, and Answers setup
questions = [
    "Which language is primarily used for Android App Development?",
    "What is the correct way to make a single-element tuple in Python?",
    "Which data structure is immutable in Python?"
]

options = [
    ["A. Python", "B. Java", "C. HTML", "D. CSS"],
    ["A. (5)", "B. [5]", "C. (5,)", "D. tuple(5)"],
    ["A. List", "B. Dictionary", "C. Set", "D. Tuple"]
]

# Storing the correct option characters
correct_answers = ["B", "C", "D"]

# Matching prize levels for each question
prize_pool = [1000, 5000, 10000]

total_winnings = 0

# 2. Main Game Loop
print("=== Welcome to Kaun Banega Crorepati (KBC) ===")

for i in range(len(questions)):
    print(f"\nQuestion {i+1} for Rs. {prize_pool[i]}:")
    print(questions[i])
    
    # Print the 4 options
    for option in options[i]:
        print(option)
        
    # Take user response and convert to uppercase to prevent case errors
    user_choice = input("Enter your choice (A/B/C/D): ").upper().strip()
    
    # Validate the answer
    if user_choice == correct_answers[i]:
        total_winnings = prize_pool[i]
        print(f"🎉 Correct Answer! You have won Rs. {total_winnings}")
    else:
        print(f"❌ Wrong Answer! The correct answer was {correct_answers[i]}.")
        print("Game Over!")
        break

# 3. Final Output
print(f"\n💰 Total cash prize you are taking home: Rs. {total_winnings}")
print("Thank you for playing KBC!")
