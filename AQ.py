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
        masterboolList = []
        boolList = []
        for _complex in myStar.complexes:
            for thing in _complex:
                indexOfThingBeingChecked = self.DataSet.AttributeNames.index(thing[0])
                if str(self.DataSet.dataTable[0][Index][indexOfThingBeingChecked] ) != str( thing[1].replace("!", "")):
                    boolList.append(True)
                else:
                    boolList.append(False)
            if False not in boolList:
                masterboolList.append(True)
                return True
        return False

    #Figure out the diferences between two given cases in the data table.
    def findDifferences(self, seed, NegValues):
        dif = []
        for i in xrange(0, len(seed)):
            if seed[i] != NegValues[i]:
                dif.append(NegValues[i])
            else:
                dif.append(" ")
        return dif

    #Helper Method for adding selectors to each partial star.
    def StarForACase(self, dif):
        TheStarOfThisCase = Star()
        for i in xrange(0, len(dif)):
            position = i
            attribute = getattr(self.DataSet, 'AttributeNames')[position]
            if dif[i] != " ":
                TheStarOfThisCase.addSelector(attribute, "!"+str(dif[i]))
            else:
                continue
        return TheStarOfThisCase

    # @function CalculatePartialStar
    # Finds The Value of a Partial Star, and returns that star as a Star object
    def CalculatePartialStar(self, seed, NegativeCase):
        PartialStar = Star()
        NegValues = getattr(self.DataSet, 'dataTable')[0][NegativeCase]
        dif = self.findDifferences(seed, NegValues)
        PartialStar = self.StarForACase(dif)
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


    # The main driver of the whiole program is the AQ Algorithm
    # For every concept, the algorithm will generate a cover, appending that cover to ConceptStars
    # This is done through generation and comparison of partial stars.
    def runAQ(self, MAXSTAR):
        self.MAXSTAR = MAXSTAR
        if not self.IsConsistent:
            return

        #Loop Through Each Concept
        Concepts = getattr(self.DataSet, 'ConceptNames')
        indexofcconcept = 0

        for Concept in Concepts:
            #ConceptStars keeps track of the rules, so we add a new list of rules for each concept
            self.ConceptStars.append([])

            #Debugging/ Sanity Check
            print "Starting New Concept " + str(Concept)
            PositiveCases = []
            NegativeCases = []
            ConceptCover = []

            #Create the Sets of Positive and Negative Cases
            for i in xrange(0, len(self.DataSet.dataTable[1])):
                if self.DataSet.dataTable[1][i] == Concept:
                    PositiveCases.append(i)
                else:
                    NegativeCases.append(i)

            #Sanity Check
            print "Positive Cases"
            print PositiveCases
            print "Negative Cases"
            print NegativeCases

            #Create a Master cases Covered List to keep track of the indexes of cases that are already covered.
            MasterCasesCoveredList =[]
            for PositiveCase in PositiveCases:

                #Create a New star that is the conjunction of all partial stars for this positive case
                ConceptStar = Star()

                seed = getattr(self.DataSet, 'dataTable')[0][PositiveCase]

                # Loop Through all the negative cases using seed as a parameter for partial star generation.
                for NegativeCase in NegativeCases:
                    print ""
                    PartialStar = self.CalculatePartialStar(seed, NegativeCase)
                    PartialStar.SimplifyWith(MAXSTAR)

                    #Set the complexes of the Concept star to the partial star if it's emty initially
                    if len(ConceptStar.complexes) == 0:
                        ConceptStar.complexes.append(PartialStar.complexes)

                    else:
                        #Combine Stars
                        ConceptStar.Combine(PartialStar)
                        ConceptStar.simplify()

                        #Figure out what cases are currently covered by the Star
                        CasesCovered = []
                        for i in PositiveCases:
                            if self.IsCovered(i, ConceptStar):
                                CasesCovered.append(i)

                        for j in NegativeCases:
                            if j != NegativeCase:
                                if self.IsCovered(j, ConceptStar):
                                    CasesCovered.append(j)

                        #If negative cases remain in the CasesCovered List, break
                        if self.NegativeCasesRemain(CasesCovered, NegativeCases):
                            break
                        #Otherwise, make sure to add the cases to the master cases covered list
                        else:
                            for i in CasesCovered:
                                MasterCasesCoveredList.append(i)

                #This is done after every negative case is viewed, as to ensure MasterCasesCoveredList is accurate
                #If the master cover is the same as the positive cases, add the star to the cover for this concept
                if set(MasterCasesCoveredList) == set(PositiveCases):
                    ConceptCover.append(ConceptStar)

                    #For Every star in  the current cover
                    for star in ConceptCover:
                        #output each star to the  conceptstars list (the master cover)
                        self.ConceptStars[indexofcconcept].append(star)
                    break

                #If there are still discrepencies in PositiveCases and MasterCoverList
                elif set(MasterCasesCoveredList) != set(PositiveCases):
                    #We still want to add the concept star to the concept cover, but not add it's entries to the master cover
                    ConceptCover.append(ConceptStar)

            #Increment the concept index
            indexofcconcept += 1

    #Check quickly if negative cases remain
    def NegativeCasesRemain(self, List, NegativeCases):
        for entry in List:
            if entry in NegativeCases:
                return True
        return False


    #Make the ruleset simpler by removing rules that are supersets of other rules
    def SimplifyRuleSet(self):
        print "Simplifying..."
        for Cover in self.ConceptStars:
            for star in Cover:
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

    #Printing Helper for Negated Rules
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
        # print "Non-negating Rule"
        rule = ""
        NumConditionsInRule = 0
        ConditionsInRule = []

        for entry in _complex:
            # print entry
            NegSet = list(set(entry).difference(set(self.DataSet.AttributeNames)))
            NewSet = []
            # print NegSet
            for condition in NegSet:
                condition = condition.replace("!", "")
                NewSet.append(condition)
            NegSet = NewSet
            # print NegSet
            for AV in self.DataSet.attributeValues:
                if AV[0] == entry[0]:
                    ReversedCondition = list(set(AV[1]).difference(set(NegSet)))
                    # print ReversedCondition
                    ReversedCondition.insert(0, entry[0])
                    ConditionsInRule.append(ReversedCondition)
                    # print "Conditions In Rule: " + str(ConditionsInRule)
        return ConditionsInRule


    #Helper for writing non-negated rules
    def WriteRulesWithoutNegation(self):
        fileName = "datasets/my-data.without.negation.rul"
        with open(fileName, 'w') as output:
            for i in xrange(0, len(self.DataSet.ConceptNames)):
                for star in self.ConceptStars[i]:
                    for _complex in star.complexes:
                        decisionTuple = (str(getattr(self.DataSet,'DecisionName')), str(getattr(self.DataSet, 'ConceptNames')[i]))
                        ruleList = []
                        for thing in _complex:
                            myRules = self.PrintComplexAsRuleNotNegated(_complex)
                            if myRules not in ruleList:
                                ruleList.append(myRules)
                        for entry in myRules:
                            pass
                        for entry in ruleList:
                            for sublist in entry:
                                for other in entry:

                                        if len(entry) == 1:
                                            RULE = "(" + str(sublist[0]) + ", " + str(sublist[1])+ ") -> " + str(decisionTuple)
                                            print RULE
                                            self.nonNegatedRules.append(RULE)
                                            output.write(RULE + "\n")

                                        if (sublist[0] != other[0]):
                                            RULE  = "(" + str(sublist[0]) +", " + str(sublist[1]) + ") & ("+ str(other[0]) +", "+str(other[1])+ ") -> " + str(decisionTuple)
                                            if RULE not in self.nonNegatedRules:
                                                print RULE
                                                self.nonNegatedRules.append(RULE)
                                                output.write(RULE + "\n")

        print "Non-Negated Rules Complete!"
        return

    # @function WriteRulesWithNegation
    # Writes the rules to a file in negated format
    # working on figuring out how to transform this to non-negated format
    def WriteRulesWithNegation(self):
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
