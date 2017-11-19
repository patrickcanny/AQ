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
        # print "Calculating Partial Star..."
        PartialStar = Star()

        for NegativeCase in NegativeCases:
            TheStarOfThisCase = Star()
            NegValues = getattr(self.DataSet, 'dataTable')[0][NegativeCase]
            # print "Selector:"+ str(NegativeCase) + str(NegValues)

            dif = set(NegValues).difference(set(PositiveCase))
            # print "Differences in Seed and Case: " + str(dif)
            for value in dif:
                position = NegValues.index(value)
                attribute = getattr(self.DataSet, 'AttributeNames')[position]
                TheStarOfThisCase.addSelector(attribute, "!"+str(value))
                NewComplexes = set(TheStarOfThisCase.complexes).union(set(PartialStar.complexes))
                PartialStar.complexes = list(NewComplexes)
        # print "Case Star Complexes"
        # print TheStarOfThisCase.complexes
        # print "PartialStar Complexes: "
        # print PartialStar.complexes
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

            #Debugging Tool
            # print "Positive Cases"
            # print PositiveCases[i]
            # print "Negative Case:"
            # print NegativeCase

            for PositiveCase in PositiveCases[i]:
                #Debugging Tool
                # print "Seed: " + str(PositiveCase) + str(getattr(self.DataSet, 'dataTable')[0][PositiveCase])

                caseValues = getattr(self.DataSet, 'dataTable')[0][PositiveCase]
                if not self.IsCovered(PositiveCase, ConceptStar):

                    PartialStar = self.CalculatePartialStar(caseValues, NegativeCase)

                    PartialStar.SimplifyWith(MAXSTAR)

                    ConceptStar.Combine(PartialStar, False)

                    self.ConceptStars.append(ConceptStar)

                else:
                    print "Case already covered!"
            i+=1
        print self.ConceptStars[0].complexes
        print self.ConceptStars[1].complexes


    def WriteRulesWithNegation(self):
        #TODO: Figure Out File Extension Stuff
        fileName = "datasets/test.wth.negation.rul"
        with open(fileName, 'w') as output:
            for i in xrange(0, len(self.DataSet.ConceptNames)):
                for _complex in self.ConceptStars[i].complexes:
                    print str(_complex)
                    decisionTuple = (getattr(self.DataSet,'DecisionName'), getattr(self.DataSet, 'ConceptNames')[i])
                    print str(_complex)+ " ----> " + str(decisionTuple)
                    output.write(str(_complex)+ " ----> " + str(decisionTuple)+"\n")
        return
