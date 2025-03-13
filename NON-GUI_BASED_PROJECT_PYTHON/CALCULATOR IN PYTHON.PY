import sys

def addition():
    num =list(map(float, input("Enter the numbers seprated by space: ").split()))
    return sum(num)

def subtraction():
    num1=float(input("Enter Num1: "))
    num2=float(input("Enter Num2: "))
    sub = (num1 - num2)
    return sub

def division():
    num1=float(input("Enter Num1: "))
    num2=float(input("Enter Num2: "))
    if num2 != 0:
        div = (num1 / num2)
        return div
    elif num2 == 0:
        print("---INVALID INPUT---")

def multiplication():
    value = list(map(float, input("Enter the numbers seprated by space: ").split()))
    Result= 1
    for i in value:
        Result *= i # Can also be "Result = Result*num".
    return Result
    
def averagelist():
    num = list(map(float, input("Enter the numbers seprated by space: ").split()))
    sumoflist = sum(num)
    lengthoflist = len(num)
    averageoflist = (sumoflist / lengthoflist)
    return averageoflist

def factorial():
    num = int(input("Enter the number: "))
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

def user_input():
    uit = input("1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Average\n6) Factorial\nEnter from the given operation(1/2/3/4/5/6): ")
    if uit == "1":
            print(addition())
    elif uit == "2":
            print(subtraction())
    elif uit == "3":
            print(multiplication())
    elif uit == "4":
            print(division())
    elif uit == "5":
            print(averagelist())
    elif uit == "6":
            print(factorial())

def exit():
    input("Press Enter TO Exit....")
    sys.exit()

user_input()
exit()