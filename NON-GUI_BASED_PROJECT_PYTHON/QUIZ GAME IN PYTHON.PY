import sys

def exit():
    input("Press Enter To Exit...")
    sys.exit()

# Making a dictionary with questions & options.
quiz_game = {
    1: "What is the capital of France?\n""a) Berlin\n""b) Rome\n""c) Paris\n""d) Madrid",
    2: "Which planet is known as the 'Red Planet'?\n""a) Earth\n""b) Mars\n""c) Venus\n""d) Jupiter",
    3: "What is the chemical symbol for water?\n""a) H2O\n""b) CO2\n""c) O2\n""d) NaCl",
    4: "In what year did World War II end?\n""a) 1918\n""b) 1945\n""c) 1939\n""d) 1948",
    5: "What is the largest ocean on Earth?\n""a) Atlantic Ocean\n""b) Indian Ocean\n""c) Arctic Ocean\n""d) Pacific Ocean"
}

quiz_sol = {
    1: "c",
    2: "b",
    3: "a",
    4: "b",
    5: "d"
}

score = 0

def play():
    choice = input("Do you want to play (y/n): ").lower()
    if choice == "y":
        print("-Let's get started-\n")
    else:
        print("--Thanks for playing--")
        exit()

def length_quiz():
    return len(quiz_game)

def play_quiz():
    global score
    for i in range(1, length_quiz() + 1):
        print(f"Q{i}: {quiz_game[i]}")
        answer = input("Your Answer: ").lower()
        if answer == quiz_sol[i]:
            print("Correct\n")
            score += 1
        else:
            print(f"Incorrect, Correct Answer is: {quiz_sol[i]}\n")
    print(f"Your final score is: {score}/{length_quiz()}")

print("-----WELCOME TO QUIZ GAME-----\n")
play()
play_quiz()
exit()