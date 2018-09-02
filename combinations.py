import itertools

from datetime import datetime
startTime = datetime.now()

p = input("What is your P value: ")
q = input("What is your Q value: ")
p = int(p)
q = int(q)
disks = p*q - (p+q)

diskOptions = range(p*q)

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

# diskChoices = combinations(diskOptions,disks)
# for i in diskChoices:
#     print(i)

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
    whereWShouldStart = count+1
    for l in range(1, len(diskNumbers)):
        tempList = []
        for m in range(disks):
            temp = (diskChoices[count][m]+l)%(p*q)
            tempList.append(temp)
        tempList = sorted(tempList)
        n = whereWShouldStart
        if n >= len(diskChoices):
            n = count+1
        for s in range((len(diskChoices)-count)):
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
                whereWShouldStart=n#
                break
            n = n+1
            if n >= len(diskChoices):
                n = count+1
    count = count+1

# count = 0
# while count < len(diskChoices)-(p*q)+2:
#     for l in range(1, len(diskNumbers)):
#         tempList = []
#         for m in range(disks):
#             temp = (diskChoices[count][m]+l)%(p*q)
#             tempList.append(temp)
#         tempList = sorted(tempList)
#         n=count+1
#         while n < len(diskChoices):
#             match = True
#             r=0
#             while r < len(tempList):
#                 if diskChoices[n][r] == tempList[r]:
#                     r = r+1
#                     continue
#                 else:
#                     match = False
#                 r = r+1
#             if match:    
#                 diskChoices.pop(n)
#                 break
#             n = n+1
#     count = count+1



for a in range(len(diskChoices)):
    tempList = []
    for b in range(disks):
        tempPair = diskNumbers[diskChoices[a][b]]
        tempList.append(tempPair)
    diskChoices[a]=tempList
    


# for item in diskChoices:
#     print(item)
print("New # of diskChoices: " + str(len(diskChoices)))

print("Runtime: " + str(datetime.now()-startTime))