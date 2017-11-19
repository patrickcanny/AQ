#@Author: Patrick Canny
#@File: DataSet.py
#@Purpose: DataSet object for AQ Program.

#Class DataSet
class DataSet(object):
    """docstring for DataSet."""
    def __init__(self):
        super(DataSet, self).__init__()

        #Name Affiliated with the Decision (i.e. Flu, D)
        self.DecisionName = ""

        #A List Containing the number of attributes in the dataset
        self.NumberOfAttributes = []
        #A list containing the names of each attribute affiliated with the dataset
        self.AttributeNames = []

        #Consistency/Numerical Flags
        self.IsConsistent = True
        self.IsNumerical = False

        #Primary Data Table.
        #   First Index: List of Tuples, each representing the attributes affiliated with a case
        #   Second Index: Each Decision affiliated with a corresponding case.
        #                           The index of decsion will be identical to index of corresponding case
        self.dataTable = [[],[]]
        self.attributeValues = [[],[]]

        #List of the names of each concept
        self.ConceptNames = []

        #List of Lists containing the values affiliated with each concept.
        #The index of the concept cases affiliated with a concept is the same index as that concept in ConceptNames
        self.ConceptCases = []

    #Setter for all Attributes (Python Style *_*)
    def __setattr__(self, name, value):
            super(DataSet, self).__setattr__(name, value)

    #@function addNewCaseToDataset
    # Appends a Case of values to the dataTable
    def addNewCaseToDataset(self, case):
        self.dataTable[0].append(case)

    #@function addNewDecision
    # Appends a decision value to the dataTable
    def addNewDecision(self, Decision):
        self.dataTable[1].append(Decision)

    #@function ChangeConceptNames
    # Essentially a setter for ConceptNames attribute
    def ChangeConceptNames(self):
        self.ConceptNames = list(set(self.dataTable[1]))

    #@function  ChangeConceptCases
    # Essentially a setter for ConceptCases attribute
    def ChangeConceptCases(self):
        for concept in self.ConceptNames:
            DecisionsAffliated = [i for i, x in enumerate(self.dataTable[1]) if x == concept]
            self.ConceptCases.append(DecisionsAffliated)

    #@function Dsicretize
    # If dataset is numerical, this function will convert it to a discretized version
    def Discretize(self):
        for case in self.dataTable[0]:
            for attribute in case:
                DiscretizeAttribute(attribute)

    def DiscretizeAttribute(self, AttributeIndex):
        PossibleAttributes = set(self.dataTable[0][AttributeIndex])





    #@function PrintProcessedData
    # Debugging tool that prints the attributes affiliated with a dataset object
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
