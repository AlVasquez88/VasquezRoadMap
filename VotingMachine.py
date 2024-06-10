#Author: Alvin Vasquez, 000857238
#Version: votingMachine.py

msg = """
This program is a ballot voting machine.
"""

print(msg)

###Program Function ============================

#defining function for spoiled votes
def spoilVote(collectVotes):
    maxVotes = max(collectVotes.count(p) for p in collectVotes)
    minVotes = min(collectVotes.count(u) for u in collectVotes)
    #processing maxVote and minVote to be the same amount of votes using if statement
    if (maxVotes == minVotes):
        
        return maxVotes and minVotes
    
    
    
    
## Main Program ================================

#Creating variable list for canidateList
canidateList = []

#Inputting the amount of canidates using variable numCanidate 
numCanidates = int(input("How many canidates are running (e.g. 3) > "))

#establishing up a infinite loop if the user inputs a lower number other than 2 by using if statements.
while True:
    if numCanidates <= 1:
        numCanidates = int(input("Please enter two canidates or higher: "))
    else:
        break;
#Appending the number of numCanidates into canidateList using a for loop.
for i in range(1, numCanidates + 1):
    canidate = input(f"Enter lastname of canidate #{i}: ")
    canidateList.append(canidate)

#Outputting the list of canidates
print()
print("List of Canidates")
print("-1 for a spoiled ballot")

#establishing a for loop to display the list of canidates from the canidateList variable
for n in canidateList:
    print(f"{n}\t", canidateList.index(n))
print("press 999 to quit")

                   
#Creating a variable list for collectVotes
collectVotes = []

#Displaying directions for the user to commence voting
print("Enter a vote using the index number beside each canidate.")

#inputting variable integer pickVote to collect the votes with the infinite loop to continue until the user breaks the loop with 999
while True:
    pickVote = int(input("Enter a vote (e.g. 0 or 999 to quit) > "))
    #Establishing a sentinel using an if statement
    if pickVote == 999:
        #Displaying Election results
        print("Election Results -------------------------")
        #Displaying the results using for loop
        for index, x in enumerate(canidateList):
            print(f"{x} {collectVotes.count(index)}")
        
        break;
    else:
        collectVotes.append(pickVote)
        continue;
#Displaying numbers spoiled if any. It will answer none if there is no spoiled ballot. I was unable to find a way to change the none to 0.
print("number spoiled: ", spoilVote(collectVotes))


#Displaying the total valid votes to cast
print("Total valid votes cast: ", len(collectVotes))

#Setting variable tieVotes as input for spoilVote function
tieVotes = spoilVote(collectVotes)

#Displaying results that is either a tie or the winner using if elif statements
if tieVotes == True:
    print("There was a tie.")
    for index, m in enumerate(canidateList):
        print(f"\t\t{m} with {collectVotes.count(index)} votes.")
elif tieVotes != True:
    for max, q in enumerate(canidateList):
        print(f"The winner is {q} with {collectVotes.count(max)} votes.")

# I couldn't figure out a way to display only the winner and hide the losers from the loop.
