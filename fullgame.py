import itertools

p = input("What is your P value: ")
q = input("What is your Q value: ")
p = int(p)
q = int(q)
disks = p*q - (p+q)

diskNumbers = []
for i in range(p):
    for j in range(q):
        diskNumbers.append((i,j))
print(diskNumbers)
diskChoices = list(itertools.combinations(range(p*q), disks))
numberOfDiskChoices = len(diskChoices)
print("Original # of diskChoices: " + str(numberOfDiskChoices))

count = 0
while count < len(diskChoices)-(p*q)+2:
    for l in range(1, len(diskNumbers)):
        tempList = []
        for m in range(disks):
            temp = (diskChoices[count][m]+l)%(p*q)
            tempList.append(temp)
        tempList = sorted(tempList)
        n=count+1
        while n < len(diskChoices):
            match = True
            r=0
            while r < len(tempList):
                if diskChoices[n][r] == tempList[r]:
                    r = r+1
                    continue
                else:
                    match = False
                r = r+1
            if match:    
                diskChoices.pop(n)
            n = n+1
    count = count+1



for a in range(len(diskChoices)):
    tempList = []
    for b in range(disks):
        tempPair = diskNumbers[diskChoices[a][b]]
        tempList.append(tempPair)
    diskChoices[a]=tempList
    


# for item in diskChoices:
#     print(item)
print("New # of diskChoices: " + str(len(diskChoices)))