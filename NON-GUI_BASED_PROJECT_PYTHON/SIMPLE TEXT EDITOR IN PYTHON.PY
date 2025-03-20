import sys

def exit():
    input("Press Enter To Exit...")
    sys.exit()

def read_create():
    x = (input("Enter The Name Of File: ")).upper()
    try:
        with open (f"{x}.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        with open(f"{x}.txt", "x") as file:
            file.write("THIS IS NEW FILE")
            print("This File Doesn't Exist...")
            print(f"{x}, File Is Created")

def write_data():
    x = (input("Enter The Name Of File: ")).upper()
    y = input("Enter Data To Be Written: ")
    with open(f"{x}.txt", "w") as file:
        file.write(f"{y}")
        print("Data Is Written")

def add_data():
    x = (input("Enter The Name Of File: ")).upper()
    y = input("Enter Data To Be added: ")
    with open(f"{x}.txt", "a") as file:
        file.write(f"\n{y}")
        print("Data Is Added")

def main():
    print("---SIMPLE TEXT EDITOR---")
    print("Select Your Choice:\n1. Read/Create File\n2. Write/Overwrite Data\n3. Add Data\n4. Exit")
    while True:
        z = input("Enter Your Choice: ")
        if z == "1":
            read_create()
        elif z == "2":
            write_data()
        elif z == "3":
            add_data()
        elif z == "4":
            exit()

main()