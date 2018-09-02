from datetime import datetime
startTime = datetime.now()

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

xyResults = readxyFile("3,4_xyResults.dat")
for xyResult in xyResults:
    print(xyResult)

print("Runtime: " + str(datetime.now()-startTime))
