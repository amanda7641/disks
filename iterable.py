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

#Builds general overlapData for all annular disks with these p and q values
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
overlapDataTuple = tuple(overlapData)



#Can get more info from user to let them decide how many disks to try
    #disks = int(input("How many disks will you use? "))

orientationConfigurations = list(itertools.product([0,1], repeat=disks))
#In the above configurations: 1 is positive, 0 is negative

#Generate all possible choices of disks
myNumbers = range(p*q)
myList = list(itertools.combinations(myNumbers, disks))

#Prune overlapData rows based on sortedDiskNumbers and pairs from each row with a number that is not in sortedDiskNumbers
def prune(myOverlapData, diskChoice):
    prunedOverlapData = []
    for overlapDataItem in myOverlapData:
        if diskChoice.count(overlapDataItem[0][0]) > 0:
            prunedOverlapDataItem = []
            for pair in overlapDataItem:
                if diskChoice.count(pair[0]) > 0:
                    prunedOverlapDataItem.append(pair)
            prunedOverlapData.append(prunedOverlapDataItem)
    return prunedOverlapData

#Loop through all disk choices to play xygame for each choice
hasConfiguration = []
for sortedDiskNumbers in myList:
    prunedOverlapData = prune(overlapData, sortedDiskNumbers)
    print(str(sortedDiskNumbers) + ", overlap: " + str(prunedOverlapData))
    game = xygame.XYGame(p,q,prunedOverlapData,len(sortedDiskNumbers),sortedDiskNumbers, orientationConfigurations)
    xyList = game.getXYList()
    if xyList:
        configs = []
        for config in xyList:
            configs.append(config[0])
        hasConfiguration.append((sortedDiskNumbers, configs))
for configuration in hasConfiguration:
    print(configuration)
print("Number of configurations that work: " + str(len(hasConfiguration)))
print("Runtime: " + str(datetime.now()-startTime))
