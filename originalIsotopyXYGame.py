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
diskNumbers = []
for i in range(p):
    for j in range(q):
        overlapData.append([((i%p,j%q),'l'),(((i+1)%p,j%q),'r'),((i%p,(j-1)%q),'r')])
        overlapData.append([((i%p,j%q),'r'),(((i-1)%p,(j-1)%q),'r'),(((i-1)%p,j%q),'l'),(((i)%p,(j+1)%q),'l'),(((i+1)%p,(j+1)%q),'r')])

#Gets more info from user
disks = int(input("How many disks will you use? "))
while disks > p*q:
    disks = int(input("How many disks will you use? "))
diskNumbers = []
for i in range(int(disks)):
    m = input("Enter disk number in form 'i,j': ")
    mList = m.split(',')
    iTH = int(mList[0])
    jTH = int(mList[1])
    while iTH < 0 or iTH > p-1 or jTH < 0 or jTH > q-1 or diskNumbers.count((iTH,jTH)) > 0:
        if iTH < 0 or iTH > p-1 or jTH < 0 or jTH > q-1:
            m = input("Error, one of those is not possible. Choose a new disk: ")
            mList = m.split(',')
            iTH = int(mList[0])
            jTH = int(mList[1])
        if diskNumbers.count((iTH,jTH)) > 0:
            m = input("You have already added that disk, choose a new one: ")
            mList = m.split(',')
            iTH = int(mList[0])
            jTH = int(mList[1])
    diskNumbers.append((iTH,jTH))
#You can comment out the above, if you wish to supply the diskNumbers in a list like below
    #diskNumbers = [1,2,3,12,9,10,11,13,15,17,19]
    #disks = len(diskNumbers)

#Sort diskNumbers for easy viewing
sortedDiskNumbers = sorted(diskNumbers)
print(sortedDiskNumbers)

# for i in overlapData:
#     print(i)
#     print("There are: " + str(len(overlapData)))

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

print("Overlap Data: " + str(overlapData))
print()

print("Configurations that work: ")
configurationsList = []
for configuration in orientationConfigurations:

    tooManyYTest = False
    for overlapDataList in overlapData:
        xyList = []
        for overlapDataItem in overlapDataList:
            if configuration[sortedDiskNumbers.index(overlapDataItem[0])] == 1:
                if overlapDataItem[1] == "l":
                    xyList.append("x")
                else:
                    xyList.append("y")
            else:
                if overlapDataItem[1] == "l":
                    xyList.append("y")
                else:
                    xyList.append("x")
        if xyList[0] == "y" and xyList.count("y") >= 2:
            tooManyYTest = True
            break
    if tooManyYTest:
        continue
    else:
        configurationsList.append(configuration)


for workingConfiguration in configurationsList:
    print("Configuration: " + str(workingConfiguration))
print("Number of working configuration: " + str(len(configurationsList)))

print("Runtime: " + str(datetime.now()-startTime))



 