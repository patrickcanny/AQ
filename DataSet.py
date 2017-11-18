class DataSet(object):
    """docstring for DataSet."""
    def __init__(self):
        super(DataSet, self).__init__()

        self.DecisionName = ""
        self.Attributes_Length = 0
        self.NumberOfAttributes = []
        self.AttributeNames = []

        self.IsConsistent = True
        self.IsNumerical = False

        self.dataTable = [[],[]]
        self.attributeValues = [[],[]]

        self.ConceptNames = []
        self.ConceptCases = [[],[]]

    def __setattr__(self, name, value):
            super(DataSet, self).__setattr__(name, value)

    # def __getattr__(self, name):
    #     super(DataSet, self).__getattr__(name)

    def addNewCaseToDataset(self, case):
        self.dataTable[0].append(case)

    def addNewDecision(self, Decision):
        self.dataTable[1].append(Decision)

    def ChangeConceptNames(self):
        self.ConceptNames = list(set(self.dataTable[1]))

    def ChangeConceptCases(self):
        concept = self.ConceptNames[0]
        iterator = 0
        for decision in self.dataTable[1]:
            if decision == concept:
                self.ConceptCases[0].append(iterator)
            else:
                self.ConceptCases[1].append(iterator)
            iterator += 1

    # def Discretize(self):
    #     for i in dataTable[0]

    def PrintProcessedData(self):
        print "Printing your Data"

        print self.DecisionName
        print self.IsConsistent
        print self.IsNumerical

        print "Attribute Names: "
        print self.AttributeNames

        print "Cases: "
        for row in self.dataTable[0]:
            print row

        print "Decisions For those Cases"
        for row in self.dataTable[1]:
            print row

        print set(self.dataTable[1])
