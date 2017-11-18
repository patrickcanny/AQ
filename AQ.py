from DataParser import DataParser
from DataSet import DataSet
from Star import Star
import itertools

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
        for Complex in myStar.complexes:
            coveredByComplex = True
            if coveredByComplex:
                for j in range(0, len(getattr(self.DataSet, 'NumberOfAttributes'))):
                    for k in Complex:

                        if myStar.k.attrName == getattr(self.DataSet, 'AttributeNames')[j] and myStar.k.negValue == getattr(self.DataSet, 'dataTable')[IndexOfCase][j]:
                            coveredByComplex = False

            if coveredByComplex:
                return True
        return False

    # Finds The Value of a Partial Star
    def CalculatePartialStar(self, PositiveCase, NegativeCases):
        print "Calculating Partial Star..."
        PartialStar = Star()

        for NegativeCase in NegativeCases:
            if not NegativeCase or self.IsCovered(NegativeCase, PartialStar):
                TheStarOfThisCase = Star()

                for j in range(0, len(getattr(self.DataSet, 'NumberOfAttributes'))):
                    if getattr(self.DataSet, 'dataTable')[PositiveCase][j] is not getattr(self.DataSet, 'dataTable')[NegativeCases[i]][j]:
                        TheStarOfThisCase.gainsSelector(getattr(self.DataSet, 'AttributeNames')[j], getattr(self.DataSet, 'dataTable')[NegativeCases[i]][j])

                PartialStar = Star(PartialStar, TheStarOfThisCase, False)
        print "PartialStar Complexes: "
        print PartialStar.complexes
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
                    print "Data Not Consistent!"
                    return False
        print "Data is Consistent"
        return True

    def runAQ(self, MAXSTAR):
        if not self.IsConsistent:
            return

        Concepts = getattr(self.DataSet, 'ConceptNames')
        i = 0
        
        for Concept in Concepts:
            print "Starting New Concept..."
            ConceptStar = Star()
            PositiveCases = getattr(self.DataSet, 'ConceptCases')
            joined = list(itertools.chain.from_iterable(PositiveCases))
            NegativeCaseSet = set(joined).difference(set(PositiveCases[i]))
            NegativeCase = list(NegativeCaseSet)
            print "Positive Cases"
            print PositiveCases[i]
            print "Negative Case:"
            print NegativeCase

            for PositiveCase in PositiveCases[i]:
                print "Case in Question: " + str(PositiveCase)
                print "Case Values: " + str(getattr(self.DataSet, 'dataTable')[0][PositiveCase])
                caseValues = getattr(self.DataSet, 'dataTable')[0][PositiveCase]
                if not self.IsCovered(PositiveCase, ConceptStar):
                    PartialStar = self.CalculatePartialStar(caseValues, NegativeCase)
                    PartialStar.SimplifyWith(MAXSTAR)
                    ConceptStar.Combine(PartialStar, False)
                    self.ConceptStars.append(ConceptStar)
                else:
                    print "Case already covered!"
            i+=1


    # def WriteRulesWithNegation(self):
    #     #TODO: Figure Out File Extension Stuff
    #     fileName = "test.wth.negation.rul"
    #     with open(filename, 'w') as output:
    #         for concept in range(0, len(ConceptNames)):
    #             for Star in ConceptStars[concept].len(complexes):
    #                 for Selector in
