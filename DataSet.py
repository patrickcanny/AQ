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

        #Holds possible attribute values for each attribute studied
        self.attributeValues = []

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

    def ChangeAttributeValues(self):
        for i in xrange(0, len(self.AttributeNames)):
            ListOfPossibleAttributeValues = []
            for row in self.dataTable[0]:
                if row[i] not in ListOfPossibleAttributeValues:
                    ListOfPossibleAttributeValues.append(row[i])
            ValueToAppend = (self.AttributeNames[i], ListOfPossibleAttributeValues)
            self.attributeValues.append(ValueToAppend)

    #@function Dsicretize
    # If dataset is numerical, this function will convert it to a discretized version
    def Discretize(self):
        index = 0
        ListOfDescritizableIndexes = []
        for value in self.attributeValues:
            if len(value[1]) > 2:
                for row in self.dataTable[0]:
                    for attribute in row:
                        try:
                            #if the indexed value can be converted to a floating point, do it and add to a list of descritazable attributes
                            float(attribute)
                            ListOfDescritizableIndexes.append(index)

                        except:
                            continue
                    index += 1

                for i in xrange(len(row)):
                    if i in ListOfDescritizableIndexes:
                        DiscreteList = []
                        for row in self.dataTable[0]:
                            #create a list of all the attributes at index i in each case
                            DiscreteList.append(row[i])
                            #created a set in order to remove duplicate values for calculation
                        DiscreteSet = set(DiscreteList)
                        #found maximum and minimum values from that set
                        MaximumAttributeVal = max(DiscreteSet)
                        MinimumAttributeVal = min(DiscreteSet)
                        try:
                            float(MaximumAttributeVal)
                            float(MinimumAttributeVal)
                            MeanVal = (MaximumAttributeVal + MinimumAttributeVal)//2
                        except:
                            continue
                        for row in self.dataTable[0]:
                            if MinimumAttributeVal <= float(row[i]) < MeanVal:
                                row[i] = str(MinimumAttributeVal)+".."+str(MeanVal)
                            elif MeanVal <= float(row[i]) <= MaximumAttributeVal :
                                row[i] = str(MeanVal)+".."+str(MaximumAttributeVal)



    #@function PrintProcessedData
    # Debugging tool that prints the attributes affiliated with a dataset object
    def PrintProcessedData(self):
        print "Printing your Data"

        print self.DecisionName
        print self.IsConsistent
        print self.IsNumerical

        print "Attribute Names: "
        print self.AttributeNames

        print "Attribute Values"
        print self.attributeValues

        print "Cases: "
        for row in self.dataTable[0]:
            print row

        print "Decisions For those Cases"
        for row in self.dataTable[1]:
            print row
