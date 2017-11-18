from DataParser import DataParser
from DataSet import DataSet

class AQ(object):

    def __init__(self, filename):
        super(AQ, self).__init__()
        self.DataParser = DataParser(filename)
        self.DataSet = DataParser.buildTable()
        self.IsConsistent = self.ConsistencyCalculator()
        if IsConsistent:
            DataSet.Discretize()
        self.ConceptStars = []

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
            for j in range(len(DataSet.getattr('dataTable'))):
                isNeg = True
                for k in PositiveCases:
                    if j is k:
                        isNeg = False
                        break
                if isNeg:
                    NegativeCases.append[j]
        for PositiveCase in PositiveCases:
            if not isCovered(PositiveCase, ConceptStar):
                PartialStar = CalculatePartialStar(PositiveCase, NegativeCases)
                PartialStar.SimplifyWith(MAXSTAR)
                ConceptStar.Combine(PartialStar, False)
        self.ConceptStars.append(ConceptStar)

    def WriteRulesWithNegation(self):
        #TODO: Figure Out File Extension Stuff
        fileName = "test.wth.negation.rul"
        with open(filename, 'w') as output:
            for concept in range(0, len(ConceptNames)):
                for Star in ConceptStars[concept].len(complexes):
                    for Selector in 
