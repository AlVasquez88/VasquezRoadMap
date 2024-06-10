#A1 - pH Analyzer
#Alvin Vasquez, 000857238
#
#This program analyzes pH readings from highly acidic to the most nuetral or strong base levels.
#
#
#PROGRAM FUNCTION===================================

#Establishing function as pH(n)

def pH(n):
    if n == 0:
        return "The pH value of 0 indicates: Strong Acid"
    elif n == 1:
        return "The pH value of 1 indicates: Strong Acid"
    elif n == 2:
        return "The pH value of 2 indicates: Strong Acid"
    elif n == 3:
        return "The pH value of 3 indicates: Weak Acid"
    elif n == 4:
        return "The pH value of 4 indicates: Weak Acid"
    elif n == 5:
        return "The pH value of 5 indicates: Weak Acid"
    elif n == 6:
        return "The pH value of 6 indicates: Weak Acid"
    elif n == 7:
        return "The pH value of 7 indicates: Nuetral"
    elif n == 8:
        return "The pH value of 8 indicates: Weak Base"
    elif n == 9:
        return "The pH value of 9 indicates: Weak Base"
    elif n == 10:
        return "The pH value of 10 indicates: Weak Base"
    elif n == 11:
        return "The pH value of 11 indicates: Weak Base"
    elif n == 12:
        return "The pH value of 12 indicates: Strong Base"
    elif n == 13:
        return "The pH value of 13 indicates: Strong Base"
    elif n == 14:
        return "The pH value of 14 indicates: Strong Base"
    else:
        return "Error: Invalid pH value. Values must be between 0 and 14 Inclusive."






#MAIN PROGRAM ======================================

#Displaying program title:
print("pH Analyzer")

#Inputting variable "n" as the integer value

n = int(input("Enter a pH value (e.g. 7) > "))

#Outputting the variable n using program function pH(n):

print(pH(n))