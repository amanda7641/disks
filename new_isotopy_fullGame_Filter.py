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
        overlapData.append([((i%p,j%q),'l'),(((i)%p,(j-1)%q),'r'),(((i+1)%p,(j)%q),'r')])
        overlapData.append([((i%p,j%q),'r'),(((i-1)%p,(j)%q),'l'),(((i)%p,(j+1)%q),'l')])

#Generate all possible choices of disks
diskNumbers = []
for i in range(p):
    for j in range(q):
        diskNumbers.append((i,j))
diskNumbers.pop(0)
diskOptions = list(itertools.combinations(diskNumbers, (disks-1)))
diskChoices = []
for z in range(len(diskOptions)):
    diskChoices.append(list(diskOptions[z]))
    diskChoices[z].insert(0,(0,0))

numberOfDiskChoices = len(diskChoices)

orientationConfigurations = list(itertools.product([0,1], repeat=disks))
#In the above configurations: 1 is positive, 0 is negative

filename = str(p)+","+str(q)+"_xyResults_New_Isotopy_FullGame_Filtered"
file = open(filename,"w+")

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

count = 0
configurationsCount = 0
disksThatWork = []
for diskChoice in diskChoices:
    #check that the diskChoice wasn't already added in a transformed version
    alreadyCounted = False
    for i in range(p):
        for j in range(q):
            if i==0 and j==0:
                continue
            else:
                tempList = []
                for m in range(disks):
                    temp1 = (diskChoice[m][0]+i)%(p)
                    temp2 = (diskChoice[m][1])+j)%(q)
                    tempList.append((temp1,temp2))
                tempList = sorted(tempList)
                if disksThatWork.count(tempList) > 0:
                    alreadyCounted = True
                    break
        if alreadyCounted:
            break
    if alreadyCounted:
        break
    #loop through each orientation configuration
    prunedOverlapData = prune(overlapData, diskChoice)
    configurationsList = []
    for configuration in orientationConfigurations:
        #play the xygame
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
            #check if the constraints make the orientation config fail
            thisDoesNotWork = False
            matrixForm = [[0 for col in range(q)]for row in range(p)]
            configurationCounter = 0 #Use to track which index in configuration we should be using
            #While placing a 1 (negative) or 2 (positive) into the matrix, check whether any surrounding places in the matrix cause a problem
            for disk in diskChoice:
                newValue = matrixForm[disk[0]][disk[1]] + configuration[configurationCounter] + 1
                matrixForm[disk[0]][disk[1]] = newValue
                if newValue == 2 and (matrixForm[disk[0]][(disk[1]+1)%q]==1 or matrixForm[(disk[0]-1)%p][disk[1]]==1 or matrixForm[(disk[0]-1)%p][(disk[1]-1)%q]==2 or matrixForm[(disk[0]+1)%p][(disk[1]+1)%q]==2):
                    thisDoesNotWork = True
                    break
                if newValue == 1 and (matrixForm[disk[0]][(disk[1]-1)%q]==2 or matrixForm[(disk[0]+1)%p][disk[1]]==2 or matrixForm[(disk[0]-1)%p][(disk[1]-1)%q]==1 or matrixForm[(disk[0]+1)%p][(disk[1]+1)%q]==1):
                    thisDoesNotWork = True
                    break
                configurationCounter = configurationCounter + 1
            #If no problems arise above, check to be sure there are no rows of all 1 (negative) or columns of all 2 (positive)
            if not thisDoesNotWork:
                for j in range(q):
                    positive = False
                    if matrixForm[0][j] == 2:
                        positive = True
                        for i in range(p):
                            if matrixForm[i][j]==1 or matrixForm[i][j]==0:
                                positive = False
                                break
                    if positive:
                        thisDoesNotWork = True
                        break
                for i in range(p):
                    negative = False
                    if matrixForm[i][0] == 1:
                        negative = True
                        for j in range(q):
                            if matrixForm[i][j]==2 or matrixForm[i][j]==0:
                                negative = False
                                break
                        if negative:
                            thisDoesNotWork = True
                            break
                #If no problems arise above, all this configuration to the list of configurations that work for this diskchoice
                if not thisDoesNotWork:
                    disksThatWork.append(diskChoice)
                    configurationsList.append(configuration)
                    configurationsCount = configurationsCount + 1
    if len(configurationsList) > 0:
        file.write("Disk Choice: " + str(diskChoice)+ "\n")
        for workingConfiguration in configurationsList:
            file.write(str(workingConfiguration)+ "\n")
        count = count + 1
        file.write("\n")
file.write("There are " + str(count)+ " disk choices that produce " + str(configurationsCount) + " possible configurations.")
file.close()

print("Runtime: " + str(datetime.now()-startTime))