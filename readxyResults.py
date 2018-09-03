from datetime import datetime
startTime = datetime.now()

#Read file and build list of allxyResults where each item is a list with the first item being the diskchoice and the following items are configuration configurations
def readxyFile(filename):
        text_file = open(filename, "r")
        lines = text_file.read().splitlines()
        lines.pop(len(lines)-1)
        text_file.close()
        allxyResults = []
        onexyResult = []
        count = 0
        for line in lines:
            if line == "":
                count = count + 1
                allxyResults.append(onexyResult)
                onexyResult = []
                continue
            else:
                if not onexyResult:
                    onexyResult.append(eval(line[13:]))
                else:
                    onexyResult.append(eval(line))
        return allxyResults

p = input("What is your P value: ")
q = input("What is your Q value: ")
p = int(p)
q = int(q)
disks = p*q - (p+q)

#Use the method above to read the file
filename = "" + str(p)+","+str(q)+"_xyResults_New_Isotopy"
xyResults = readxyFile(filename)

#Create a new file to store the new xyResults
newFilename = str(p)+","+str(q)+"_xyResults_New_Isotopy_After_Constraints"
file = open(newFilename,"w+")


xyResultCount = 0 #Use to track how many diskChoices still have configurations that could work
configurationsCount = 0 #Use to track how many total possible configurations there are
#Loop through each diskchoice and its configurations
for xyResult in xyResults:
    configurationsList = [] #This will keep all configurations that could still work for this disk choice
    for configuration in xyResult[1:]:
        thisDoesNotWork = False
        matrixForm = [[0 for col in range(q)]for row in range(p)]
        configurationCounter = 0 #Use to track which index in configuration we should be using
        #While placing a 1 (negative) or 2 (positive) into the matrix, check whether any surrounding places in the matrix cause a problem
        for disk in xyResult[0]:
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
                configurationsList.append(configuration)
                configurationsCount = configurationsCount + 1
    #If there are configurations that pass all tests for this diskchoice, write to the file the disk choice followed by all possible configurations that are remaining
    if configurationsList:
        file.write(str(xyResult[0]) + "," + str(configurationsList) + "\n")
        xyResultCount = xyResultCount + 1
file.write("There are " + str(xyResultCount) + " disk choices that produce " + str(configurationsCount) + " possible configurations.")
file.close()
print("There are " + str(xyResultCount) + " disk choices that produce " + str(configurationsCount) + " possible configurations.")
print("Runtime: " + str(datetime.now()-startTime))