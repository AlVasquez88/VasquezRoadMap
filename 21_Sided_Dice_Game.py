#Author: Alvin Vasquez
#Version: PV18
import random

msg = """
This Program Determines if your number matches the 21-sided dice
"""

print(msg)

### Program Function

#defining program function roll()

def Roll():
    x = random.randint(1,21)
    return x

### Main Program

Predict = int(input("Pick a number between 1 to 21:\n"))

while True:
    if Predict > 1 and Predict < 21:
        print("You selected: ", Predict)
        break;
    else:
        print("Please enter another number.")


print()
print("Rolling the 21-sided dice.....")
print("The dice landed at: ", Roll())