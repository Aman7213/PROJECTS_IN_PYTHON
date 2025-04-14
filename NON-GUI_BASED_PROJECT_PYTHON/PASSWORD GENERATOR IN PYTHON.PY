# Strong Password Generator In Python

import random
import string
import sys

def exit():
    input("Press Enter To Exit...")
    sys.exit()

print("---STRONG PASSWORD GENERATOR---")

while True:

    print("1) Generate Password\n2) Exit")

    choice = input("Enter Your Choice (1/2): ")

    if choice == "1":
        len = int(input("Enter the length of the password: "))

        all = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation

        temp = "".join(random.choices(all, k=len))

        print(temp)

        save = input("Do you want to save the file(Y/N): ").upper()
        if save == "Y":
            with open("pass.txt", "w") as file:
                file.write(temp)
                print("File is saved\n")
        else:
            continue
    else:
        exit()

