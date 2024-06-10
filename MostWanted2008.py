#author: Alvin Vasquez
# version: MostWanted2008.py
msg = """
This program predicts which cars are the most wanted
by using a histogram.
"""
print(msg)
import random
## Main program ==============================================
#creating a list for cars
carNames = ["Toyota","Jeep","Mclaren","Ford","Audi","Honda","Mazda","Jaguar","BMW","Dodge"]
#creating score list as crime rate
score = []
#Establishing a for loop to display the crime rate
print("Crime Rate")
for i in range(0,9):
    #appending crime rate in random into the score list
    score.append(random.randint(0,10))
#crime rate results
for i in range(0,9):
    print(carNames[i]+"\t",score[i])
#displaying title for a histogram
print("Histogram")
#displaying index for the histogram
for f in range(0,11):
    print(f,end="\t")
    #setting variable for counting
    count = 0
    #establishing a for loop to count the crime rate using if statement
    for j in range(0,9):
        if (f == score[j]):
            count = count + 1
    #displaying astorisk in a for loop through the range of the count variable
    for k in range(count):
        print("*",end="")
    print()
        
