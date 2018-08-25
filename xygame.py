import itertools

class XYGame:

    def __init__(self, p, q, overlapData, numberOfDisks, diskChoices, orientationConfigurations):
        self.p = int(p)
        self.q = int(q)
        self.overlapData = overlapData
        self.numberOfDisks = numberOfDisks
        self.diskChoices = diskChoices
        self.orientationConfigurations = orientationConfigurations
        #list of special disks that do not follow configuration if/else rules
        #then the special rules need to be added to singleConfigurationXY function


    #this will not be used at the moment since a list is being passed in
    #get overlap data from file
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

    #function to test one configuration
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

    #loop through all configurations
    def allConfigurationsXY(self, configurations, overlapData):
        configurationPairingList = []
        for configuration in configurations:
            xyList = self.singleConfigurationXY(configuration, overlapData)
            if xyList == None:
                continue
            else:
                configurationPairingList.append((configuration, xyList))
        return configurationPairingList

    #print the pairings of configurations that work and the xy list
    def printAllConfigurationsXY(self, list):
        for item in list:
            print("Configuration: " + str(item[0]) + ", XYList: " + str(item[1]))

    def play(self):
        #do not need to read overlap file unless we change back to overlap file instead of list
        #overlapData = self.readOverlapFile(self.overlapData)
        overlapData = self.overlapData
        print("Overlap Data: " + str(self.overlapData))
        print()


        print("Configurations that work: ")
        XYList = self.allConfigurationsXY(self.orientationConfigurations, self.overlapData)
        self.printAllConfigurationsXY(XYList)
        print("Number of working configuration: " + str(len(XYList)))

    def getXYList(self):
        overlapData = self.overlapData
        XYList = self.allConfigurationsXY(self.orientationConfigurations, self.overlapData)
        return XYList