import xygame
import overlapData
import itertools

from datetime import datetime
startTime = datetime.now()

p = input("What is your P value: ")
q = input("What is your Q value: ")
p = int(p)
q = int(q)
disks = p*q - (p+q)

#builds general overlap for all annular disks with these p and q values
overlapData = []
for i in range(1,p*q+1):
    if i % p == 0:
        overlapData.append([(i%(p*q),'r'),((i+q-1)%(p*q),'l'),((i+q)%(p*q),'r'),((i+1)%(p*q),'l')])
        overlapData.append([(i%(p*q),'l'),((i-1)%(p*q),'r'),((i-q)%(p*q),'l'),((i-q+1)%(p*q),'r')])
    elif i % p == 1:
        overlapData.append([(i%(p*q),'l'),((i-1)%(p*q),'r'),((i+q)%(p*q),'r'),((i+q-1)%(p*q),'r')])
        overlapData.append([(i%(p*q),'r'),((i-q+1)%(p*q),'l'),((i-q)%(p*q),'r'),((i+1)%(p*q),'r')])
    elif i % p == (p-1):
        overlapData.append([(i%(p*q),'l'),((i+q)%(p*q),'l'),((i+q-1)%(p*q),'r')])
        overlapData.append([(i%(p*q),'r'),((i-1)%(p*q),'r'),((i-q)%(p*q),'l'),((i-q+1)%(p*q),'l'),((i+1)%(p*q),'l')])
    else:
        overlapData.append([(i%(p*q),'l'),((i+q)%(p*q),'r'),((i+q-1)%(p*q),'r')])
        overlapData.append([(i%(p*q),'r'),((i-1)%(p*q),'r'),((i-q)%(p*q),'l'),((i-q+1)%(p*q),'l'),((i+1)%(p*q),'r')])
    



#gets more info from user
#can use to decide how many disks to use
#disks = int(input("How many disks will you use? "))

orientationConfigurations = list(itertools.product([0,1], repeat=disks))
#1 is positive, 0 is negative

#generate all possible choices of disks
myNumbers = range(p*q)
myList = list(itertools.combinations(myNumbers, disks))

#loop through all disk choices to play xygame for each choice - disable choosing disks when we do this.
hasConfiguration = []
for sortedDiskNumbers in myList:
    #prune overlapData rows based on sortedDiskNumbers
    overlapDataPruned = []
    for overlapDataItem in overlapData:
        if sortedDiskNumbers.count(overlapDataItem[0][0]) > 0:
            overlapDataPruned.append(overlapDataItem)

    #prune out pairs from each row with a number that is not in sortedDiskNumbers
    overlapDataPrunedAgain = []
    for overlapDataItem in overlapDataPruned:
        overlapDataItemPruned = []
        for pair in overlapDataItem:
            if sortedDiskNumbers.count(pair[0]) > 0:
                overlapDataItemPruned.append(pair)
        overlapDataPrunedAgain.append(overlapDataItemPruned)
                
    game = xygame.XYGame(p,q,overlapDataPrunedAgain,len(sortedDiskNumbers),sortedDiskNumbers, orientationConfigurations)
    xyList = game.getXYList()
    if len(xyList):
        configs = []
        for config in xyList:
            configs.append(config[0])
        hasConfiguration.append((sortedDiskNumbers, configs))
        print((sortedDiskNumbers, configs))
print("Number of configurqations that work: " + str(len(hasConfiguration)))

for configuration in hasConfiguration:
    print(configuration)

print("Runtime: " + str(datetime.now()-startTime))


#overlapData = overlapData.OverlapData("allOverlap.dat", sortedDiskNumbers)
#overlapDataForDiskChoices = overlapData.findOverlapDataForDiskChoices()

