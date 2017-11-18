from DataSet import DataSet

class DataParser(object):
    def __init__(self, MyFile):
        super(DataParser, self).__init__()
        self.File = MyFile
        self.data = DataSet()

    def ParseData(self, File):
        print "Parsing Data..."
        for line in File:
            row = line
            head, sep, tail = line.partition('!')
            if head == "" or head.isspace():
                row = tail
            else:
                row = head
                if row[0] == '<':
                    continue
                elif row[0] == '[':
                    self.DefineAttributes(row)
                else:
                    self.AddCase(row)
        return self.data

    def DefineAttributes(self, row):
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

    #Finds the unique concepts for a specific data table.
    # def FindConcepts(self):
    #     for case in len(data.getattr('dataTable')[1])

    def Read(self):
        self.File = open(self.File, 'r')
        return self.ParseData(self.File)
