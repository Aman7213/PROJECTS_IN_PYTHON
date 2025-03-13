# Write a program to have the computer randomly select a number between 1 and 100, and then prompt the player to guess the number. The program should give hints if the guess is too high or too low.

import random

# This will give random number between 1 to 100.
def ran():
    return random.randint(1, 100)

# If user wants to play the game.
def want_play():
    play = input("Do you want to play(y/n): ")
    if play == "y":
        print("---GUESS THE NUMBER---")
        user_input(ran())
    elif play == "n":
        print("---Thanks For Playing---")
        exit()

# Input Guess from user.
def user_input(number):
    while True:
        try:
            guess = int(input("Choose a Number Between (1-100): "))
            if guess < 1 or guess > 100:
                print("---Invalid Number. Please choose a number between 1 and 100.---")
                continue
            if guess == number:
                print("---Winner---")
                again = input("Do you want to play again(y/n): ")
                if again == "y":
                    play()
                else:
                    print("---Thanks For Playing---")
                    exit()
            elif guess < number:
                print("Low!")
            elif guess > number:
                print("High!")
        except ValueError:
            print("---Invalid Input! Please enter a valid number.---")

def play():
    want_play()

print("-----GUESS THE NUMBER GAME-----")

play()