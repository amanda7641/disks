import xygame
import overlapData
import itertools

from datetime import datetime
startTime = datetime.now()

p = input("What is your P value: ")
q = input("What is your Q value: ")
p = int(p)
q = int(q)

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
disks = int(input("How many disks will you use? "))
while disks > p*q:
    disks = int(input("How many disks will you use? "))
diskNumbers = []
for i in range(int(disks)):
    m = int(input("Next disk number!: "))
    while m < 1 or m > p*q or diskNumbers.count(m) > 0:
        if m < 1 or m > p*q:
            m = int(input("There are a maximum of " + str(p*q) + " disks. Choose a new one: "))
        if diskNumbers.count(m) > 0:
            m = int(input("You have already added that disk, choose a new one: "))
    diskNumbers.append(int(m))
# diskNumbers = [1,2,3,12,9,10,11,13,15,17,19]
sortedDiskNumbers = sorted(diskNumbers)
for disk in sortedDiskNumbers:
    if disk == p*q:
        sortedDiskNumbers.remove(disk)
        sortedDiskNumbers.insert(0,0)
print(sortedDiskNumbers)


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
                

orientationConfigurations = list(itertools.product([0,1], repeat=disks))
#1 is positive, 0 is negative

#overlapData = overlapData.OverlapData("allOverlap.dat", sortedDiskNumbers)
#overlapDataForDiskChoices = overlapData.findOverlapDataForDiskChoices()

game = xygame.XYGame(p,q,overlapDataPrunedAgain, len(sortedDiskNumbers), sortedDiskNumbers, orientationConfigurations)
game.play()


print("Runtime: " + str(datetime.now()-startTime))



                