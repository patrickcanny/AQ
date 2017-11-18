from DataParser import DataParser
from DataSet import DataSet
from Star import Star

class AQ(object):

    def __init__(self, DataSet):
        super(AQ, self).__init__()
        self.DataSet = DataSet
        self.IsConsistent = True
        if self.ConsistencyCalculator():
            pass
            # DataSet.Discretize()
        self.ConceptStars = []

    # Calculates if a given complex covers a Star.
    # This Method Used Intermediately to Calculate Coverings of Partial Stars.
    def IsCovered(self, IndexOfCase, myStar):
        for i in range(0, len(myStar.complexes)):
            coveredByComplex = True
            if coveredByComplex:
                for j in range(0, len(getattr(self.DataSet, 'NumberOfAttributes'))):
                    for k in len(myStar.complexes[i]):

                        if myStar.complexes[i][k].attrName == getattr(self.DataSet, 'AttributeNames')[j] and myStar.complexes[i][k].negValue == getattr(self.DataSet, 'dataTable')[IndexOfCase][j]:
                            coveredByComplex = False

            if coveredByComplex:
                return True

        return False

    # Finds The Value of a Partial Star
    def CalculatePartialStar(self, PositiveCase, NegativeCases):

        PartialStar = Star

        for i in range (0, len(NegativeCases)):
            if i == 0 or IsCovered(NegativeCases[i], PartialStar):
                TheStarOfThisCase = Star()

                for j in range(0, len(getattr(self.DataSet, 'NumberOfAttributes'))):
                    if getattr(self.DataSet, 'dataTable')[PositiveCase][j] is not getattr(self.DataSet, 'dataTable')[NegativeCases[i]][j]:
                        TheStarOfThisCase.gainsSelector(getattr(self.DataSet, 'AttributeNames')[j], getattr(self.DataSet, 'dataTable')[NegativeCases[i]][j])

                PartialStar = Star(PartialStar, TheStarOfThisCase, False)
            #Debug Statement Could Go Here
        return PartialStar


    def ConsistencyCalculator(self):
        Table = getattr(self.DataSet, 'dataTable')
        Attributes = getattr(self.DataSet, 'AttributeNames')
        for i in range(0, len(Table)):
            for j in range (0, i):
                TheAttributesAreIdentical = True
                if TheAttributesAreIdentical:
                    for k in range(0, len(Attributes)):
                        if Table[i][k] is not Table[j][k]:
                            TheAttributesAreIdentical = False
                if TheAttributesAreIdentical and Table[i][len(Attributes)] is not Table[j][len(Attributes)]:
                    return False
        return True

    def runAQ(self, MAXSTAR):
        if not self.IsConsistent:
            return

        self.DataSet.PrintProcessedData()
        # Concepts = self.DataSet.getattr('ConceptNames')
        # PositiveCases = self.DataSet.getattr('ConceptCases')

        Concepts = getattr(self.DataSet, 'ConceptNames')
        PositiveCases = getattr(self.DataSet, 'ConceptCases')

        print Concepts
        print PositiveCases

        for Case in Concepts:
            ConceptStar = Star()
            NegativeCases = []
            for j in getattr(self.DataSet, 'dataTable'):
                isNeg = True
                for k in PositiveCases:
                    if j is k:
                        isNeg = False
                        break
                if isNeg:
                    NegativeCases.append(j)
        for PositiveCase in PositiveCases:
            if not self.IsCovered(PositiveCase, ConceptStar):
                PartialStar = self.CalculatePartialStar(PositiveCase, NegativeCases)
                PartialStar.SimplifyWith(MAXSTAR)
                ConceptStar.Combine(PartialStar, False)
        self.ConceptStars.append(ConceptStar)

    # def WriteRulesWithNegation(self):
    #     #TODO: Figure Out File Extension Stuff
    #     fileName = "test.wth.negation.rul"
    #     with open(filename, 'w') as output:
    #         for concept in range(0, len(ConceptNames)):
    #             for Star in ConceptStars[concept].len(complexes):
    #                 for Selector in
