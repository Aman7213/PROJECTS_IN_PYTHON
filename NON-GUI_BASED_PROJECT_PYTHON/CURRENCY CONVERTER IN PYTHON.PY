# Currency converter program

import sys

def exit():
    input("Press Enter To Exit...")
    sys.exit()

def user_amount():
    amount = float(input("Enter the Amount: "))
    return amount

def user_input_amount():
    source = input("Source Currency (USD/INR/JAP): ").upper()
    return source

def user_output_amount():
    target = input("Target Currency (USD/INR/JAP): ").upper()
    return target

def usd_inr(amount):
    return amount * 87.05

def usd_jap(amount):
    return amount * 147.90

def inr_usd(amount):
    return amount * 0.011

def inr_jap(amount):
    return amount * 1.07

def jap_inr(amount):
    return amount * 0.59

def jap_usd(amount):
    return amount * 0.0068

amount = user_amount()
source = user_input_amount()
target = user_output_amount()

def currency_converter():
    if source == "USD" and target == "USD":
        print(f"{amount} USD is equal to {amount} USD")
    elif source == "USD" and target == "INR":
        print(f"{amount} USD is equal to {usd_inr(amount)} INR")
    elif source == "USD" and target == "JAP":
        print(f"{amount} USD is equal to {usd_jap(amount)} JAP")
    elif source == "INR" and target == "INR":
        print(f"{amount} INR is equal to {amount} INR")
    elif source == "INR" and target == "USD":
        print(f"{amount} INR is equal to {inr_usd(amount)} USD")
    elif source == "INR" and target == "JAP":
        print(f"{amount} INR is equal to {inr_jap(amount)} JAP")
    elif source == "JAP" and target == "JAP":
        print(f"{amount} JAP is equal to {amount} JAP")
    elif source == "JAP" and target == "USD":
        print(f"{amount} JAP is equal to {jap_usd(amount)} USD")
    elif source == "JAP" and target == "INR":
        print(f"{amount} JAP is equal to {jap_inr(amount)} INR")
    else:
        print("---INVALID INPUT---")
        exit()

print("---Currency Converter---")
currency_converter()
exit()
