# To Do List apllication

import sys

print("-----TO DO LIST APPLICATION-----\n")

print("To Do List Menu:\n1. View Task\n2. Add Task\n3. Remove Task\n4.exit")

task = ["SAMPLE DATA"]

def user_choice():
    x = input("Enter Your Choice: ")
    return x

def view_task():
    for item in task:
         print(item)

def exit():
    input("Press Enter To Exit...")
    sys.exit()

def add_task():
    while True:
        user_input = input("Enter New Task: ")
        task.append(user_input)
        choice = input("Add Another Task (y/n): ")
        if choice.lower() == "n":
            view_task()
            break

def remove_task():
    while True:
        view_task()
        user_input = input("Enter Task To Remove: ").upper()
        task.remove(user_input)
        choice = input("Remove Another Task (y/n): ")
        if choice.lower() == "n":
            view_task()
            break

def functionality():
    while True:
        choice = user_choice()
        if choice == "1":
            view_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            exit()


functionality()


    
