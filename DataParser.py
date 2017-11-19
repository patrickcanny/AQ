#@Author: Patrick Canny
#@File DataParser.py
# Data parsing tool for AQ algorithm.

from DataSet import DataSet

#@Class DataParser
class DataParser(object):
    def __init__(self, MyFile):
        super(DataParser, self).__init__()
        #File name that the parser will parse
        self.File = MyFile

        #A Dataset affiliated with the parser, which is returned to AQ
        self.data = DataSet()

    #@function ParseData
    # Main Parser function, returns the dataset to AQ
    def ParseData(self, File):
        print "Parsing Data..."
        for line in File:
            row = line
            a, b, c = line.partition('!')
            if a == "" or a.isspace():
                row = c
            else:
                row = a
                if row[0] == '<':
                    continue
                elif row[0] == '[':
                    self.DefineAttributes(row)
                else:
                    self.AddCase(row)
        return self.data

    #@function DefineAttributes
    # Helper function for DataParser
    # Sets a variety of attributes in the dataset object affiliated with the class
    def DefineAttributes(self, row):
        #Temporary data table
        AttributesAndDecision = [[],[]]
        attribute = row.split()
        indicies = 0, -1
        attributes = [i for j, i in enumerate(attribute) if j not in indicies]
        del attributes[-1]
        decision = attributes[len(attributes)-1]
        del attributes[-1]

        setattr(self.data, 'AttributeNames', attributes)
        setattr(self.data, 'DecisionName', decision)
        setattr(self.data, 'dataTable', AttributesAndDecision)

    #@function AddCase
    # Appends decision and case rows to the dataset
    # Pretty Standard file splitting function
    def AddCase(self, row):
        case = row.split()
        decisionval = case[-1]
        AllCases = [[],[]]
        AllCases[1].append(decisionval)
        del case[-1]
        for i in range(len(case)):
            try:
                case[i] = float(case[i])
                setattr(self.data, 'IsNumerical', True)
            except ValueError:
                continue

        AllCases[0] = case
        self.data.addNewCaseToDataset(case)
        AllCases[1] = decisionval
        self.data.addNewDecision(decisionval)


    #@function Read
    # Main driver for the dataparser class.
    def Read(self):
        self.File = open(self.File, 'r')
        return self.ParseData(self.File)
