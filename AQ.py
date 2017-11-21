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

        self.negatedRules = []
        self.nonNegatedRules = []

    # @function IsCovered
    # Calculates if a given complex covers a Star.
    # This Method Used Intermediately to Calculate Coverings of Partial Stars.
    def IsCovered(self, Index, myStar):
        #TODO:Figure this thing out...for some reason it's not returning accurate coverings on multiple case complexes
        # print "Checking Coverage of Case " + str(Index) + " by " + str(myStar.complexes)
        masterboolList = []
        boolList = []
        for _complex in myStar.complexes:
            for i in range (0, 3):
                pass
                # print ""
            # print "Starting New Complex"
            # print _complex
            # print Index

            for thing in _complex:
                # print "Thing: " + str( thing)
                indexOfThingBeingChecked = self.DataSet.AttributeNames.index(thing[0])
                # print "DEBUGGING"
                # print str(self.DataSet.dataTable[0][Index][indexOfThingBeingChecked])
                # print thing[1].replace("!", "")
                if str(self.DataSet.dataTable[0][Index][indexOfThingBeingChecked] ) != str( thing[1].replace("!", "")):
                    # print str(self.DataSet.dataTable[0][Index]) + thing[1].replace("!", "") + " caused the cover to return true"
                    boolList.append(True)
                    # print boolList
                else:
                    boolList.append(False)
                    # print boolList
            # print "Congrats! " + str(thing) + " covers seed " + str(Index)
            # print boolList
            if False not in boolList:
                print str(Index) + " appears to be covered by the current conceptstar"
                masterboolList.append(True)
                return True

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
    def CalculatePartialStar(self, seed, NegativeCase):
        print ""
        print "Calculating Partial Star..."

        PartialStar = Star()
        NegValues = getattr(self.DataSet, 'dataTable')[0][NegativeCase]
        print "Selector: "+ str(NegativeCase)

        dif = self.findDifferences(seed, NegValues)
        PartialStar = self.StarForACase(dif)

        print "PartialStar for seed " +str(seed) +" is: " + str(PartialStar.complexes)
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
        indexofcconcept = 0

        for Concept in Concepts:
            self.ConceptStars.append([])
            for h in range (0, 5):
                print ""
            print "Starting New Concept " + str(Concept)
            # ConceptStar = Star()
            PositiveCases = []
            NegativeCases = []
            ConceptCover = []

            for i in xrange(0, len(self.DataSet.dataTable[1])):
                if self.DataSet.dataTable[1][i] == Concept:
                    NegativeCases.append(i)
                else:
                    PositiveCases.append(i)
            #
            # PositiveCases = getattr(self.DataSet, 'ConceptCases')
            # joined = list(itertools.chain.from_iterable(PositiveCases))
            #
            # NegativeCaseSet = set(joined).difference(set(PositiveCases[i]))
            # NegativeCases = list(NegativeCaseSet)
            #
            # #Debugging Tool
            # temp = PositiveCases[i]
            # PositiveCases[i] = NegativeCases
            # NegativeCases = temp
            print "Positive Cases"
            print PositiveCases
            print "Negative Cases"
            print NegativeCases

            MasterCasesCoveredList =[]
            for PositiveCase in PositiveCases:
                for j in range(0,5):
                    print ""

                print "Looking at Positive Case: " + str(PositiveCase)
                ConceptStar = Star()
                #Debugging Tool
                # print "Seed: " + str(PositiveCase) + str(getattr(self.DataSet, 'dataTable')[0][PositiveCase])

                seed = getattr(self.DataSet, 'dataTable')[0][PositiveCase]
                print "Row Affiliated with that Positive Case: " + str(seed)
                for NegativeCase in NegativeCases:
                    PartialStar = self.CalculatePartialStar(seed, NegativeCase)
                    PartialStar.SimplifyWith(MAXSTAR)

                    if len(ConceptStar.complexes) == 0:
                        print "Current Cover is Empty, adding the Partial Star"
                        ConceptStar.complexes.append(PartialStar.complexes)

                    else:
                        print "This is Where Combination of Stars Occurs"
                        ConceptStar.Combine(PartialStar)
                        ConceptStar.simplify()
                        print "Current ConceptStar: " + str(ConceptStar.complexes)
                        CasesCovered = []
                        for i in PositiveCases:
                            # print i
                            if self.IsCovered(i, ConceptStar):
                                # print "adding from positive cases"
                                CasesCovered.append(i)

                        for j in NegativeCases:
                            if j != NegativeCase:
                                if self.IsCovered(j, ConceptStar):
                                    # print "adding from negative cases"
                                    CasesCovered.append(j)

                        print "Cases Covered: " + str(CasesCovered)


                        if self.NegativeCasesRemain(CasesCovered, NegativeCases):
                            pass
                        else:
                            for i in CasesCovered:
                                MasterCasesCoveredList.append(i)
                            print set(MasterCasesCoveredList)

                if set(MasterCasesCoveredList) == set(PositiveCases):
                    print "Great Scott! All the Positive Cases Are Covered!"
                    print "Complexes being added to cover: " + str(ConceptStar.complexes)
                    ConceptCover.append(ConceptStar)
                    print "Here is the current concept cover: " + str(ConceptCover)
                    print "Adding The Final Cover for concept " + str(Concept) + " to The ConceptStars List"
                    print indexofcconcept
                    for star in ConceptCover:
                        self.ConceptStars[indexofcconcept].append(star)
                    break
                elif set(MasterCasesCoveredList) != set(PositiveCases):
                    print "This ConceptStar is being added to the Cover: " + str(ConceptStar.complexes)
                    ConceptCover.append(ConceptStar)
                    print "Here is the current concept cover: " + str(ConceptCover)
            indexofcconcept += 1
        for entry in self.ConceptStars:
                print str(entry)


    def NegativeCasesRemain(self, List, NegativeCases):
        for entry in List:
            if entry in NegativeCases:
                print "Negative Cases Still Remain Covered! We Must Continue."
                return True
        return False

    def SimplifyRuleSet(self):
        print "Simplifying..."
        for Concept in self.ConceptStars:
            for star in Concept:
                for item in star.complexes:
                    for otherItem in star.complexes:
                        if len(item) > len(otherItem):
                            for condition in item:
                                for othercondition in otherItem:
                                    if condition == othercondition:
                                        try:
                                            star.complexes.remove(item)
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
            for i in xrange(0, len(self.DataSet.ConceptNames)):
                for star in self.ConceptStars[i]:
                    for _complex in star.complexes:
                        decisionTuple = (str(getattr(self.DataSet,'DecisionName')), str(getattr(self.DataSet, 'ConceptNames')[i]))
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
                                    if RULE not in self.nonNegatedRules:
                                        print RULE
                                        self.nonNegatedRules.append(RULE)
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
                for star in self.ConceptStars[i]:
                        for _complex in star.complexes:
                            decisionTuple = (getattr(self.DataSet,'DecisionName'), getattr(self.DataSet, 'ConceptNames')[i])
                            rulestring = self.PrintComplexAsRuleNegated(_complex) + " -> " + str(decisionTuple)
                            if rulestring not in self.negatedRules:
                                self.negatedRules.append(rulestring)
                                print rulestring
                                output.write(rulestring + "\n")
        print "Negated Rules Complete!"
        return
