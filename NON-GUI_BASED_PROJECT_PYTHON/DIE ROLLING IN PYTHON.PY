# Write a program that simulates rolling a pair of dice. Each time the program runs, it should randomly generate two numbers between 1 and 6 (inclusive), representing the result of each die. The program should then display the results and ask if the user would like to roll again.

# Importing random library to use "randint".
import random
import sys

# This "randint" of "random" library will give random number between range x to y (x, y).
def rand():
    random_num1 = (random.randint(1, 6))
    random_num2 = (random.randint(1, 6))
    print(f"{random_num1}, {random_num2}")

def exit():
    input("Press Enter to exit...")
    sys.exit()

# Def Again If user want to play again.
def again():
    choice1=input("Roll Again(y/n): ")
    if choice1=="y":
        choice()
    else:
        print("---Thanks For Playing---")
        exit()

# Give choice to user if they want to roll and roll again.
def choice():
    if option=="y":
        rand()
        again()
    else:
        print("---Thanks For Playing---")
        exit()
        
        

print("-----Do You Want To Roll The Dice-----")
option = input("Choose Your Option(y/n): ")

choice()