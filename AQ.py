#@Author: Patrick Canny
#@File: AQ.py
# AQ Algorithm Implementation

from DataParser import DataParser
from DataSet import DataSet
from Star import Star
import itertools

#@Class AQ
class AQ(object):

    def __init__(self, DataSet):
        super(AQ, self).__init__()
        #DataSet used in the AQ algorithm
        self.DataSet = DataSet

        self.MAXSTAR = 0

        #Flag for Consistency of the DataSet
        self.IsConsistent = True
        #Discretizes the data if the data is Consistent
        if self.ConsistencyCalculator():
            self.DataSet.Discretize()

        #List of stars which cover a given concept.
        #Essentially a List of the covers
        self.ConceptStars = []

    # @function IsCovered
    # Calculates if a given complex covers a Star.
    # This Method Used Intermediately to Calculate Coverings of Partial Stars.
    def IsCovered(self, IndexOfComplex, myStar):
        # print "checking coverage of "+ str(myStar.complexes) + " by index "+str(IndexOfComplex)
        for _complex in myStar.complexes:
            coveredByComplex = True;
            for j in xrange(0, len(self.DataSet.AttributeNames)):
                for k in xrange(0, len(_complex)):
                    # print _complex[k]
                    if _complex[k][0] == self.DataSet.AttributeNames[j] and _complex[k][1] == "!"+str(self.DataSet.AttributeNames[j]):
                        coveredByComplex = False
            if coveredByComplex:
                # print "Index " + str(IndexOfComplex)+ " is covered!"
                return True
            print "No Coverage, appending case"
            return False

    def findDifferences(self, seed, NegValues):
        dif = []
        for i in xrange(0, len(seed)):
            if seed[i] != NegValues[i]:
                dif.append(NegValues[i])
            else:
                dif.append(" ")
        return dif

    def StarForACase(self, dif):
        TheStarOfThisCase = Star()
        for i in xrange(0, len(dif)):
            position = i
            attribute = getattr(self.DataSet, 'AttributeNames')[position]
            if dif[i] != " ":
                TheStarOfThisCase.addSelector(attribute, "!"+str(dif[i]))
            else:
                continue
                # print str(getattr(self.DataSet, 'AttributeNames')[position] ) + " value is shared between cases"
        return TheStarOfThisCase

    # @function CalculatePartialStar
    # Finds The Value of a Partial Star, and returns that star as a Star object
    def CalculatePartialStar(self, seed, NegativeCases):
        # print ""
        # print "Calculating Partial Star..."
        PartialStar = Star()

        i = 0
        for NegativeCase in NegativeCases:
            if i ==0 or (self.IsCovered(NegativeCase, PartialStar) == True):
                TheStarOfThisCase = Star()
                NegValues = getattr(self.DataSet, 'dataTable')[0][NegativeCase]
                # print "Selector:"+ str(NegativeCase) + str(NegValues)

                dif = self.findDifferences(seed, NegValues)
                TheStarOfThisCase = self.StarForACase(dif)

                # print "Selector" + str(i)
                # print TheStarOfThisCase.complexes
                PartialStar.complexes.append(TheStarOfThisCase.complexes)
                # print "Updated Partial Star"
                PartialStar.simplify()
                PartialStar.SimplifyWith(self.MAXSTAR)
                # print PartialStar.complexes
            else:
                continue
                # print "Case " + str(NegativeCase) + " is already covered!"
        return PartialStar


    #@function ConsistencyCalculator
    # Caclulates whether or not a dataset is consistent
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

    #@function runAQ
    # The main driver of the whiole program is the AQ Algorithm
    # For every concept, the algorithm will generate a cover, appending that cover to ConceptStars
    # This is done through generation and comparison of partial stars.
    def runAQ(self, MAXSTAR):
        self.MAXSTAR = MAXSTAR
        if not self.IsConsistent:
            return

        Concepts = getattr(self.DataSet, 'ConceptNames')
        i = 0

        for Concept in Concepts:
            # print ""
            # print""
            # print "Starting New Concept..."
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

                seed = getattr(self.DataSet, 'dataTable')[0][PositiveCase]
                if not self.IsCovered(PositiveCase, ConceptStar):

                    PartialStar = self.CalculatePartialStar(seed, NegativeCase)
                    # PartialStar.SimplifyWith(MAXSTAR)
                    ConceptStar.Combine(PartialStar, False)
                    self.ConceptStars.append(ConceptStar)

                else:
                    pass
                    # print "Case already covered!"
            i+=1
        # DEBUG
        print self.ConceptStars[0].complexes
        print self.ConceptStars[1].complexes


    def SimplifyRuleSet(self):
        print "Simplifying..."
        for Concept in self.ConceptStars:
            for item in Concept.complexes:
                for otherItem in Concept.complexes:
                    if len(item) > len(otherItem):
                        for condition in item:
                            for othercondition in otherItem:
                                if condition == othercondition:
                                    try:
                                        Concept.complexes.remove(item)
                                    except:
                                        continue



    def PrintComplexAsRuleNegated(self, _complex):
        rule = ""
        ConditionsInRule = 0

        for entry in _complex:
            for condition in entry:
                NotCondition = entry[1].replace("!", "")
            rule +=  "(" + str(entry[0]) + ", not "  + str(NotCondition) +  ")"
            ConditionsInRule += 1
            if len(_complex) != ConditionsInRule:
                rule += " & "
        return rule

    #Takes a Complex
    #Inverts the Rules affiliated with that complex
    def PrintComplexAsRuleNotNegated(self, _complex):
        rule = ""
        NumConditionsInRule = 0
        ConditionsInRule = []

        for entry in _complex:
            NegSet = list(set(entry).difference(set(self.DataSet.AttributeNames)))
            NewSet = []
            for condition in NegSet:
                condition = condition.replace("!", "")
                NewSet.append(condition)
            NegSet = NewSet

            for AV in self.DataSet.attributeValues:
                if AV[0] == entry[0]:
                    ReversedCondition = list(set(AV[1]).difference(set(NegSet)))
                    ReversedCondition.insert(0, entry[0])
                    ConditionsInRule.append(ReversedCondition)
        return ConditionsInRule



    def WriteRulesWithoutNegation(self):
        fileName = "datasets/my-data.without.negation.rul"
        with open(fileName, 'w') as output:
            for i in xrange(len(self.DataSet.ConceptNames)):
                decisionTuple = (getattr(self.DataSet,'DecisionName'), getattr(self.DataSet, 'ConceptNames')[i])
                for _complex in self.ConceptStars[i].complexes:

                    ruleList = self.PrintComplexAsRuleNotNegated(_complex)
                    ComboList = []
                    for i in xrange(0, len(ruleList)):
                        for j in xrange(0, len(ruleList[i])):
                            if j != 0:
                                newTuple = (ruleList[i][0], ruleList[i][j])
                                ComboList.append(newTuple)

                    for entry in ComboList:
                        for OtherEntry in ComboList:
                            if (entry[0] != OtherEntry[0]):
                                RULE = str(entry) + " & "+ str(OtherEntry) + " -> " + str(decisionTuple)
                                print RULE
                                output.write(RULE + "\n")
                        ComboList.remove(entry)

        print "Non-Negated Rules Complete!"
        return

    # @function WriteRulesWithNegation
    # Writes the rules to a file in negated format
    # working on figuring out how to transform this to non-negated format
    def WriteRulesWithNegation(self):
        #TODO: Figure Out File Extension Stuff
        fileName = "datasets/my-data.with.negation.rul"
        with open(fileName, 'w') as output:
            for i in xrange(0, len(self.DataSet.ConceptNames)):
                decisionTuple = (getattr(self.DataSet,'DecisionName'), getattr(self.DataSet, 'ConceptNames')[i])
                for _complex in self.ConceptStars[i].complexes:

                    print self.PrintComplexAsRuleNegated(_complex) + " -> " + str(decisionTuple)
                    output.write(self.PrintComplexAsRuleNegated(_complex)+ " -> " + str(decisionTuple)+"\n")
        print "Negated Rules Complete!"
        return
