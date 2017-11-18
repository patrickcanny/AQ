class DataSet(object):
    """docstring for DataSet."""
    def __init__(self):
        super(DataSet, self).__init__()

        self.DecisionName = ""
        self.n_attributes = 0
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

    def __getattr__(self, name):
        return self.name

    def addNewCaseToDataset(self, case):
        self.dataTable[0].append(case)

    def addNewDecision(self, Decision):
        self.dataTable[1].append(Decision)


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
