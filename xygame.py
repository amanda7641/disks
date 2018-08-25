import itertools

class XYGame:

    def __init__(self, p, q, overlapData, numberOfDisks, diskChoices, orientationConfigurations):
        self.p = int(p)
        self.q = int(q)
        self.overlapData = overlapData
        self.numberOfDisks = numberOfDisks
        self.diskChoices = diskChoices
        self.orientationConfigurations = orientationConfigurations

    #This function is not currently used since a list is being passed in instead of a .dat file
    #Read overlap data from file
    def readOverlapFile(self, overlapData):
        text_file = open(overlapData, "r")
        lines = text_file.read().splitlines()
        text_file.close()
        overlapData = []
        for line in lines:
            overlapItems = []
            items = line.split(',')
            for i in range(len(items)):
                if i % 2 == 0:
                    overlapItems.append((int(items[i]), str(items[i+1])))
            overlapData.append(overlapItems)
        return overlapData

    #Tests one configuration to see if it works
    def singleConfigurationXY(self, configuration, overlapData):
        xyFullList = []
        tooManyYTest = False
        for overlapDataList in overlapData:
            xyList = []
            for overlapDataItem in overlapDataList:
                #make if for when overlapDataItem[0] % self.p == 0, then the below rules reverse
                if configuration[self.diskChoices.index(overlapDataItem[0])] == 1:
                    if overlapDataItem[1] == "l":
                        xyList.append("x")
                    else:
                        xyList.append("y")
                else:
                    if overlapDataItem[1] == "l":
                        xyList.append("y")
                    else:
                        xyList.append("x")
            if xyList.count("y") >= 2:
                tooManyYTest = True
                break
            xyFullList.append(xyList)
        if tooManyYTest:
            return None
        return xyFullList

    #Loop through all configurations to test using singleConfigurationXY function
    def allConfigurationsXY(self, configurations, overlapData):
        configurationPairingList = []
        for configuration in configurations:
            xyList = self.singleConfigurationXY(configuration, overlapData)
            if xyList == None:
                continue
            else:
                configurationPairingList.append((configuration, xyList))
        return configurationPairingList

    #Print the pairings of configurations that work and the xy list to go with the configuration
    def printAllConfigurationsXY(self, list):
        for item in list:
            print("Configuration: " + str(item[0]) + ", XYList: " + str(item[1]))

    def play(self):
        #A change can be made here if you wish to go back to reading an overlap .dat file
            #overlapData = self.readOverlapFile(self.overlapData)
        overlapData = self.overlapData
        print("Overlap Data: " + str(self.overlapData))
        print()


        print("Configurations that work: ")
        XYList = self.allConfigurationsXY(self.orientationConfigurations, self.overlapData)
        self.printAllConfigurationsXY(XYList)
        print("Number of working configuration: " + str(len(XYList)))

    #Play the XYGame, but instead of printing results return the XYList
    def getXYList(self):
        overlapData = self.overlapData
        XYList = self.allConfigurationsXY(self.orientationConfigurations, self.overlapData)
        return XYList