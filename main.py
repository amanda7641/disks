import xygame
import overlapData
import itertools

from datetime import datetime
startTime = datetime.now()

p = input("What is your P value: ")
q = input("What is your Q value: ")
p = int(p)
q = int(q)

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
    

#Gets more info from user
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
#You can comment out the above, if you wish to supply the diskNumbers in a list like below
    #diskNumbers = [1,2,3,12,9,10,11,13,15,17,19]
    #disks = len(diskNumbers)

#Sort diskNumbers for easy viewing, replace any p*q with 0 so that indexing is easier in future functions/methods
sortedDiskNumbers = sorted(diskNumbers)
for disk in sortedDiskNumbers:
    if disk == p*q:
        sortedDiskNumbers.remove(disk)
        sortedDiskNumbers.insert(0,0)
print(sortedDiskNumbers)


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

orientationConfigurations = list(itertools.product([0,1], repeat=disks))
#In the above configurations: 1 is positive, 0 is negative

#If we are going to be reading overlapData from a .dat file use the below
    #overlapData = overlapData.OverlapData("allOverlap.dat", sortedDiskNumbers)
    #overlapDataForDiskChoices = overlapData.findOverlapDataForDiskChoices()

game = xygame.XYGame(p,q,overlapData, len(sortedDiskNumbers), sortedDiskNumbers, orientationConfigurations)
game.play()


print("Runtime: " + str(datetime.now()-startTime))



     