class DataSet(object):
    """docstring for DataSet."""
    def __init__(self):
        super(DataSet, self).__init__()

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
        if name=="device":
            print "device test"
        else:
            super(DataSet, self).__setattr__(name, value)

    def __getattr__(self, name):
        return self.name

    def addNewCaseToDataset(self, case):
        self.dataTable[0].append(case)

    def PrintProcessedData(self):
        print "Printing your Data"
        print self.NumberOfAttributes
        print self.AttributeNames
        print self.IsConsistent
