# Python program capable of greeting you

import time

name = input("What's Your Name? ")

# Here "strftime" is a method used to format date and time objects into strings
t = time.strftime("%H:%M:%S")  
hour = int(time.strftime("%H"))
   
if 0 <= hour < 12:
    print(f"Good Morning {name}!")
elif 12 <= hour < 17:
    print(f"Good Afternoon {name}!")
else:
    print(f"Good Evening {name}!")