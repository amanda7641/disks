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
for i in range(p):
    for j in range(q):
        overlapData.append([((i%p,j%q),'l'),(((i+1)%p,j%q),'r'),((i%p,(j-1)%q),'r')])
        overlapData.append([((i%p,j%q),'r'),(((i-1)%p,(j-1)%q),'r'),(((i-1)%p,j%q),'l'),(((i)%p,(j+1)%q),'l'),(((i+1)%p,(j+1)%q),'r')])

#Generate all possible choices of disks
diskNumbers = []
for i in range(p):
    for j in range(q):
        diskNumbers.append((i,j))
print(diskNumbers)
diskChoices = list(itertools.combinations(diskNumbers, disks))
numberOfDiskChoices = len(diskChoices)

orientationConfigurations = list(itertools.product([0,1], repeat=disks))
#In the above configurations: 1 is positive, 0 is negative

filename = str(p)+","+str(q)+"_xyResults"
file = open(filename,"w+")

count = 0
for diskChoice in diskChoices:
    prunedOnceOverlapData= []

    #Prune overlapData rows based on sortedDiskNumbers and pairs from each row with a number that is not in sortedDiskNumbers
    # itemCount = 0
    # while itemCount < len(prunedOverlapData):
    #     if diskChoice.count(prunedOverlapData[itemCount][0][0]) <= 0:
    #         prunedOverlapData.remove(prunedOverlapData[itemCount])
    #         itemCount = itemCount - 1
    #     else:
    #         pairCount = 0
    #         while pairCount < len(prunedOverlapData[itemCount]):
    #             if diskChoice.count(prunedOverlapData[itemCount][pairCount][0]) <= 0:
    #                 prunedOverlapData[itemCount].remove(prunedOverlapData[itemCount][pairCount])
    #                 pairCount = pairCount - 1
    #             pairCount = pairCount + 1
    #     itemCount = itemCount + 1

    for overlapDataItem in overlapData:
        if diskChoice.count(overlapDataItem[0][0]) > 0:
            prunedOnceOverlapData.append(overlapDataItem)
    
    prunedOverlapData = []
    for overlapDataItem in prunedOnceOverlapData:
        prunedOverlapDataItem = []
        for pair in overlapDataItem:
            if diskChoice.count(pair[0]) > 0:
                prunedOverlapDataItem.append(pair)
        prunedOverlapData.append(prunedOverlapDataItem)

    print(diskChoice)
    print("Overlap Data: " + str(prunedOverlapData))
    print("Configurations that work: ")
    configurationsList = []
    for configuration in orientationConfigurations:
        tooManyYTest = False
        for overlapDataList in prunedOverlapData:
            xyList = []
            for overlapDataItem in overlapDataList:
                if configuration[diskChoice.index(overlapDataItem[0])] == 1:
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
    if len(configurationsList) > 0:
        file.write("Disk Choice: " + str(diskChoice)+ "\n")
        for workingConfiguration in configurationsList:
            print("Configuration: " + str(workingConfiguration))
            file.write(str(workingConfiguration)+ "\n")
        print("Number of working configuration: " + str(len(configurationsList)))
        count = count + 1
        file.write("\n")
file.write("There are " + str(count)+ " disk choices that have working orientation configurations.")   
file.close()

print("Runtime: " + str(datetime.now()-startTime))
