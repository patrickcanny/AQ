from DataParser import DataParser

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
    def IsCovered(self, IndexOfCase, Star myStar):
        for i in len(myStar.complexes):
            coveredByComplex = True
            for j in len(DataParser.getattr('NumberOfAttributes')) and coveredByComplex:
                for k in enumerate(len(myStar.complexes[i]):

                    if myStar.complexes[i][k].attrName == DataParser.getattr('AttributeNames')[j] and myStar.complexes[i][k].negValue == DataParser.getattr('dataTable')[IndexOfCase][j]:
                        coveredByComplex = False

            if coveredByComplex:
                return True

        return False

    # Finds The Value of a Partial Star
    def CalculatePartialStar(self, PositiveCase, NegativeCases):
        # TODO: Need to Figure out how to declare class instance in Python!!!!!
        Star PartialStar

        for i in len(NegativeCases):
            if i == 0 or IsCovered(NegativeCases[i], PartialStar):
                Star TheStarOfThisCase #TODO: CLASS DECLARATION Python

                for j in len(DataParser.getattr('NumberOfAttributes')):
                    if DataParser.getattr('dataTable')[PositiveCase][j] not DataParser.getattr('dataTable')[NegativeCases[i]][j]:
                        TheStarOfThisCase.gainsSelector(DataParser.getattr('AttributeNames')[j], DataParser.getattr('dataTable')[NegativeCases[i]][j])

                PartialStar = Star(PartialStar, TheStarOfThisCase, False)
            #Debug Statement Could Go Here
        return PartialStar


    def ConsistencyCalculator(self):
        Table = DataParser.getattr('dataTable')
        Attributes = DataParser.getattr('NumberOfAttributes')
        for i in len(Table):
            for j in i:
                TheAttributesAreIdentical = True
                for k in Attributes and TheAttributesAreIdentical:
                    if Table[i][k] not Table[j][k]:
                        TheAttributesAreIdentical = False
                if TheAttributesAreIdentical and Table[i][Attributes] is not Table[j][Attributes]:
                    return False
        return True

    def runAQ(self, MAXSTAR):
        if not self.getattr('IsConsistent'):
            return

        Concepts = DataParser.getattr('ConceptNames')

        for Case in len(Concepts):
            #PYTHON CLASS DECLARATION AHHH
            Star ConceptStar
            PositiveCases = DataParser.getattr('ConceptCases')
            NegativeCases = []
