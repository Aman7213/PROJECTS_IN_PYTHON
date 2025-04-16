import sys

def exit():
    input("Press enter to exit...")
    sys.exit()

Balance = 0.0

while True:
    print("Welcome to the ATM!\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your balance is: ${Balance}")
    elif choice == 2:
        amount = int(input("Enter amount to be deposited: "))
        Balance += amount
        print(f"Your updated balance is: ${Balance}")
    elif choice == 3:
        amount2 = int(input("Enter amount to withdraw: "))
        if amount2 > Balance:
            print("!!!Insufficient Balance!!!")
        elif amount2 <= Balance:
            print("Withdraw successful")
            Balance -= amount2
            print(f"Updated balance: ${Balance}")
        else:
            print("!!!Error!!!")
    elif choice == 4:
        print("---Thanks for using---")
        exit()
    else:
        print("!!!Error!!!")