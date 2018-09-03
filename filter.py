import itertools

from datetime import datetime
startTime = datetime.now()

#Read file
def readxyFile(filename):
        text_file = open(filename, "r")
        lineData = text_file.read().splitlines()
        lines = lineData[:len(lineData)-1]
        text_file.close()
        allDiskChoices = []
        for line in lines:
            fullLine = eval(line)
            allDiskChoices.append(fullLine[0])
        return allDiskChoices

p = input("What is your P value: ")
q = input("What is your Q value: ")
p = int(p)
q = int(q)
disks = p*q - (p+q)

#Use the method above to read the file
fileName = "" + str(p)+","+str(q)+"_xyResults_New_Isotopy_After_Constraints"
diskChoices = readxyFile(fileName)

print("Original # of diskChoices: " + str(len(diskChoices)))

#Create a new file to store the new xyResults
newFilename = str(p)+","+str(q)+"_xyResults_New_Isotopy_After_Constraints_and_Filtered"
file = open(newFilename,"w+")

disksThatWork = []
for diskChoice in diskChoices:
    alreadyCounted = False
    for i in range(p):
        for j in range(q):
            if i==0 and j==0:
                continue
            else:
                tempList = []
                for m in range(disks):
                    temp1 = (int(diskChoice[m][0])+i)%(p)
                    temp2 = (int(diskChoice[m][1])+j)%(q)
                    tempList.append((temp1,temp2))
                tempList = sorted(tempList)
                if disksThatWork.count(tempList) > 0:
                    alreadyCounted = True
                    break
    if alreadyCounted:
        break
    else:
        disksThatWork.append(diskChoice)

for item in disksThatWork:
    file.write(str(item)+ "\n")
file.write("New # of diskChoices: " + str(len(disksThatWork)))
file.close()
print("New # of diskChoices: " + str(len(disksThatWork)))

print("Runtime: " + str(datetime.now()-startTime))