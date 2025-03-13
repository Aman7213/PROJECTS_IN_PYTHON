# Make a Rock, Paper & Scissors Game

import random

print("-----WELCOME TO THE GAME-----")

def play():
    play=input("Do You Want To Play?(y/n): ")
    if play=="y":
        print("--Let's Play--")
    elif play=="n":
        print("---Thanks for Playing---")
        exit()
    else:
        print("--INVALID INPUT--")

def sign():
    print("Choose your option:\n""1) 🪨\n""2) 📰\n""3) ✂")

def user_input():

    random_num = random.randint(1, 3)
    i=(f"{random_num}")
    # print(i)

    user=input("Your Choice?(1/2/3): ")
    if i=="1":
        if user=="1":
            print(f"Computer Output: {i}")
            print("Draw")
        elif user=="2":
            print(f"Computer Output: {i}")
            print("Winner")
        elif user=="3":
            print(f"Computer Output: {i}")
            print("Loser")
        else:
            print("---INVALID INPUT---")
    elif i=="2":
        if user=="1":
            print(f"Computer Output: {i}")
            print("Loser")
        elif user=="2":
            print(f"Computer Output: {i}")
            print("Draw")
        elif user=="3":
            print(f"Computer Output: {i}")
            print("Winner")
        else:
            print("---INVALID INPUT---")
    elif i=="3":
        if user=="1":
            print(f"Computer Output: {i}")
            print("Winner")
        elif user=="2":
            print(f"Computer Output: {i}")
            print("Loser")
        elif user=="3":
            print(f"Computer Output: {i}")
            print("Draw")
        else:
            print("---INVALID INPUT---")

def again():
    play_again=input("Do You To Play Again?(y/n): ")
    if play_again=="y":
        start()
    elif play_again=="n":
        print("--Thanks For Playing--")
        exit()
    else:
        print("--Invalid Input--")
        exit()

def start():
    play()
    sign()
    user_input()
    again()

start()