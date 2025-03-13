
# Here is a dic that contai Question & Options.
Quiz_game = {
    1: "Q1: What is the name of main character in 'Naruto'?\n"
    "1) Sasuke\n""2) Naruto\n""3) Sakura\n""4) Itachi",

    2: "Q2: What is the name of main character in 'DeathNote'?\n"
    "1) Light\n""2) L\n""3) Misa\n""4) M",

    3: "Q3: Which anime has largest number of episode ?\n"
    "1) Naruto\n""2) Bleach\n""3) Onepiece\n""4) Hunter X Hunter"
}

print("-----Do You Want To Play A Quiz Game-----\n")

# This will confirm user if they want to play
play = input("Choose if you to play? (y/n): \n")
if play == "y":
        score = 0
        Name = input("Enter your name: ") 
else:
        exit()

print("-----Ok Let's Play The Game-----")

# This will print question 1 and give answer to choose.
print(f"{Quiz_game[1]}")
A1 = input("Choose your option(1/2/3/4): ")
if A1 == "2":
        print("Correct")
        score += 1
else:
        print("Incorrect")
y1 = input("Do you want to continue?(y/n): ")
while y1 != "y":
        exit()

# This will print question 2 and give answer to choose.
print(f"{Quiz_game[2]}")
A2 = input("Choose your option(1/2/3/4): ")
if A2 == "1":
        print("Correct")
        score += 1
else:
        print("Incorrect")
y1 = input("Do you want to continue?(y/n): ")
while y1 != "y":
        exit()

# This will print question 2 and give answer to choose.
print(f"{Quiz_game[3]}")
A3 = input("Choose your option(1/2/3/4): ")
if A3 == "3":
        print("Correct")
        score += 1
else:
        print("Incorrect")

print(f"Your Final Score is: {score}")
print(f"-----Thanks For Playing-----")
