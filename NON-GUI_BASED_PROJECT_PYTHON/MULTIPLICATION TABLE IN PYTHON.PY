# Print multiplication table of the x (Input taken from user).
# The formate of table should be in e.g. 2 x 2 = 4.

import sys

print("Hello! This Program will Print Multiplication Table")

def table():
    # To take input inpu from user to print table.
    x = int(input("Enter the number: "))
    for y in range(1, 10 +1):
        z = x*y
        print(f"{x} x {y} = {z}")

def again():
    x=input("Do you want to print another tabele?(y/n): ")
    if x=="y":
        final()
    elif x=="n":
        exit()
    else:
        print("--INVALID INPUT--")
        exit()

def exit():
    input("Press Enter Key To Exit...")
    sys.exit()

def final():
    table()
    again()

final()