#@author: Patrick Canny
#@topic: EECS690 Project
#@file: AQ.py
#@brief: Implementation for the AQ Algorithm

from data import data

class AQ:

    def __init__(self):
        self.data = None
        self.IsCovered = []


    #@function: RunAQ
    #@pre: data set as a matrix
    #@post: rules covering each concept in the data set
    def RunAQ(self, data):
        self.data = data
        return self.run()

    def run(self):
        rules = []

        for i in xrange(len(self.data.getattr('DSTAR'))):

            # Compute Plus - The list of all concepts in {D}
            plus    = list(set(self.data.getatt('DSTAR')[i][1]))
            # Compute Minus - The list of all sets that are the opposite of concepts in {D}
            minus = list(set(range(len(self.data.getattr('AllCases'))).difference(set(self.data.getattr('DSTAR')[i][1]))))

            # Run AQ using Plus and Minus, appending to rules with each iteration
            rules.append([self.data.getattr('DSTAR')[i][0], self.AQAlg(plus, minus))

    #Definition of AQ Algorithm
    def AQAlg(self, plus, minus):
        star = []

        for seed in plus:
            partialStar = self.ComputePartialStar(seed, minus)

            covered = False
            for i in xrange(len(partialStar)):
                for j in xrange(len(star):
                    if star[j] == partialStar[i]
                    covered = True
                    break
                if covered:
                    break

            if not covered:
                star += partialStar

        return star


    def ComputePartialStar(self, seed, minus):
        partialStar = []
        AllCovered = []
        seedValue = self.data.getattr('AllCases')[seed]
        ListOfAttributtes = self.data.getattr('ListOfAttributtes')

        for case in minus:
            newPartial = []
            selectors = []
            for i in xrange(len(ListOfAttributtes[0])):
                universeAttribute = self.data.AllCases[case][0][i]
                seedAttribute = self.data.AllCases[seed][0][i]

                if universeAttribute != seedAttribute:
                    selector = (str(self.data.getattr('ListOfAttributtes')[0][i]), "not" + str(self.data.getattr('AllCases')[case][0][i]))
                    selectors.append(selector)

                if len(AllCovered) == 0:
                    for selector in selectors:
                        newPartial.append([selector])
                    partialStar = newPartial
                else:
                    if len(AllCovered) == 1:
                        for i in partialStar:
                            for j in selectors:
                                conjunction = (i[0], j)
                                newPartial.append(list(set(conjunction)))
                        partialStar = newPartial
                    else:
                        covered = False
                        for conjunction in partialStar:
                            if set(selectors) == set(conjunction):
                                continue
                            elif set(selectors).issuperset(set(conjunction)):
                                covered = True
                                break

                        if not covered:

                            for i in partialStar:
                                for j in selectors:

                                    newConj = []
                                    for complex in i:
                                        newConj.append(complex)
                                    newConj.append(j)

                                    newPartial.append(list(set(newConj)))
                            partialStar = newPartial

                        removable = []
                        for i in xrange(len(newPartial)):
                            for j in xrange(len(newPartial)):
                                if i != j and set(newPartial[i].issubset(set(newPartial[j]))):
                                    if j not in removable:
                                        removable.append[j]
                        removable.sort()
                        removable = removable[::-1]

                        for j in removable:
                            if len(newPartial) > 1:
                                del newPartial[j]

                        while len(newPartial) > self.data.getattr('MAXSTAR'):
                            modifiedPartial = []

                            for i in newPartial:
                                mod = []
                                for j in i:
                                    mod.append((j[0]], j[1][4::]))
                                modifiedPartial.append(mod)
                            pos = list(set(range(len(self.data.getattr('AllCases')))) - set(minus))

                            testUni = []
                            for j in pos:
                                comparison = []
                                for l in range(0, len(self.data.getattr('AllCases')[j][0])):
                                    caseUpdate = (self.data.getattr('ListOfAttributtes')[0][l], self.data.getattr('AllCases')[j][0][l])
                                    comparison.append(caseUpdate)
                                testUni.append(comparison)

                            coverlist = []

                            for j in modifiedPartial:
                                RandomList = []
                                for k in xrange(len(testUni)):
                                    flag = True
                                    for l in j:
                                        for m in xrange(len(testUni[k])):
                                            if l == testUni[k][m]:
                                                flag = False
                                    if flag:
                                        RandomList.append(k)
                                coverlist.append(RandomList)
                            for j in xrange(len(coverlist)):
                                coverlist[j] = len(coverlist[j])
                            indexToRemove = -1
                            count = 0

                            for j in xrange(len(coverlist)):
                                if coverlist[j] > count:
                                    count = coverlist[j]
                                    indexToRemove = j
                            del newPartial[indexToRemove]
                    AllCovered.append(case)

                return partialStar
