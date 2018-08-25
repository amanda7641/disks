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
    



#Can get more info from user to let them decide how many disks to try
    #disks = int(input("How many disks will you use? "))

orientationConfigurations = list(itertools.product([0,1], repeat=disks))
#In the above configurations: 1 is positive, 0 is negative

#Generate all possible choices of disks
myNumbers = range(p*q)
myList = list(itertools.combinations(myNumbers, disks))

#Loop through all disk choices to play xygame for each choice
hasConfiguration = []
for sortedDiskNumbers in myList:
    #Prune overlapData rows based on sortedDiskNumbers and pairs from each row with a number that is not in sortedDiskNumbers
    itemCount = 0
    while itemCount < len(overlapData):
        if sortedDiskNumbers.count(overlapData[itemCount][0][0]) <= 0:
            overlapData.remove(overlapData[itemCount])
            itemCount = itemCount - 1
        else:
            pairCount = 0
            while pairCount < len(overlapData[itemCount]):
                if sortedDiskNumbers.count(overlapData[itemCount][pairCount][0]) <= 0:
                    overlapData[itemCount].remove(overlapData[itemCount][pairCount])
                    pairCount = pairCount - 1
                pairCount = pairCount + 1
        itemCount = itemCount + 1
                
    game = xygame.XYGame(p,q,overlapData,len(sortedDiskNumbers),sortedDiskNumbers, orientationConfigurations)
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



