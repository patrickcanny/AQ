from DataParser import DataParser
from DataSet import DataSet

class AQ(object):

    def __init__(self, filename):
        super(AQ, self).__init__()
        self.DataParser = DataParser(filename)
        self.DataSet = DataParser.buildTable()
        self.IsConsistent = ConsistencyCalculator()
        if IsConsistent:
            DataParser.Discretize()

    def StripFileName(self, inputString):
        Dot = False
        for i in len(inputString):
            if inputString[i] == '.':
                Dot = True
                break
            if Dot :
                return s.substr(0,i)
            else:
                return s

    # Calculates if a given complex covers a Star.
    # This Method Used Intermediately to Calculate Coverings of Partial Stars.
    def IsCovered(self, IndexOfCase, myStar):
        for i in len(myStar.complexes):
            coveredByComplex = True
            for j in len(DataSet.getattr('NumberOfAttributes')) and coveredByComplex:
                for k in len(myStar.complexes[i]):

                    if myStar.complexes[i][k].attrName == DataSet.getattr('AttributeNames')[j] and myStar.complexes[i][k].negValue == DataSet.getattr('dataTable')[IndexOfCase][j]:
                        coveredByComplex = False

            if coveredByComplex:
                return True

        return False

    # Finds The Value of a Partial Star
    def CalculatePartialStar(self, PositiveCase, NegativeCases):

        PartialStar = Star

        for i in len(NegativeCases):
            if i == 0 or IsCovered(NegativeCases[i], PartialStar):
                TheStarOfThisCase = Star()

                for j in len(DataSet.getattr('NumberOfAttributes')):
                    if DataSet.getattr('dataTable')[PositiveCase][j] is not DataSet.getattr('dataTable')[NegativeCases[i]][j]:
                        TheStarOfThisCase.gainsSelector(DataSet.getattr('AttributeNames')[j], DataSet.getattr('dataTable')[NegativeCases[i]][j])

                PartialStar = Star(PartialStar, TheStarOfThisCase, False)
            #Debug Statement Could Go Here
        return PartialStar


    def ConsistencyCalculator(self):
        Table = DataSet.getattr('dataTable')
        Attributes = DataSet.getattr('NumberOfAttributes')
        for i in len(Table):
            for j in i:
                TheAttributesAreIdentical = True
                for k in Attributes and TheAttributesAreIdentical:
                    if Table[i][k] is not Table[j][k]:
                        TheAttributesAreIdentical = False
                if TheAttributesAreIdentical and Table[i][Attributes] is not Table[j][Attributes]:
                    return False
        return True

    def runAQ(self, MAXSTAR):
        if not self.getattr('IsConsistent'):
            return

        Concepts = DataSet.getattr('ConceptNames')

        for Case in len(Concepts):
            ConceptStar = Star()
            PositiveCases = DataSet.getattr('ConceptCases')
            NegativeCases = []
