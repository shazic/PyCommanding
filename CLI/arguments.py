class Arguments():

    def __init__(self, argumentsClassList):
        self.setArgDetails(argumentsClassList)

    def setArgDetails(self, argumentsClassList):
        self.options = []

        for argumentClass  in argumentsClassList:
            for baseOption in argumentClass().options:
                self.options.append(baseOption)

    def getArgDetails(self):
        return self.options

