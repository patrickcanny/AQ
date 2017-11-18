from DataSet import DataSet

class DataParser(object):
    def __init__(self, MyFile):
        super(DataParser, self).__init__()
        self.File = MyFile
        self.data = DataSet()

    # def __getattr__(self, name):
    #     return self.name


    def ParseData(self, File):
        print "Parsing Data..."
        for line in File:
            print "Got Line!"
            row = line
            print row
            head, sep, tail = line.partition('!')
            if head == "" or head.isspace():
                row = tail
            else:
                row = head
                if row[0] == '<':
                    # print "Irrelevant Row"
                    continue
                elif row[0] == '[':
                    print "This is the row that has the attributes and decision"
                    self.DefineAttributes(row)
                else:
                    # print "Adding a case to the DataSet"
                    self.AddCase(row)
        return self.data

    def DefineAttributes(self, row):
        AttributesAndDecision = [[],[]]
        attribute = row.split()
        indicies = 0, -1
        attribute = [i for j, i in enumerate(attribute) if j not in indicies]

        AttributesAndDecision[1].append(attribute[len(attribute)-1])
        del attribute[-1]
        AttributesAndDecision[0] = attribute

        self.data.setattr('dataTable', AttributesAndDecision)

    def AddCase(self, row):
        case = row.split()

        AllCases = [[],[]]
        AllCases.append(case[len(case)-1])
        del case[-1]
        for i in range(len(case)):
            try:
                case[i] = float(case[i])
                self.data.setattr('IsNumerical', True)
            except ValueError:
                continue

        AllCases[0] = case
        self.data.addNewCaseToDataset(case)

    #Finds the unique concepts for a specific data table.
    # def FindConcepts(self):
    #     for case in len(data.getattr('dataTable')[1])

    def Read(self):
        self.File = open(self.File, 'r')
        self.ParseData(self.File)
