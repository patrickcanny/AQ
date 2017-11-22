class Star(object):
    def __init__(self, PartialStar=None, OtherStar=None , _bool=None):
        super(Star, self).__init__()
        self.complexes = []
        self.covers = []
        self.MyBool = _bool
        self.PartialStar = PartialStar
        self.OtherStar = OtherStar
        # if PartialStar and OtherStar:
        #     PartialSet = set(PartialStar.complexes)
        #     OtherSet = set(OtherStar.complexes)
        #     myset = PartialSet.union(OtherSet)
        #     self.complexes = list(myset)
        # if self.MyBool:
        #     self.simplify()

    def Star(self, PartialStar, OtherStar, boolean):
        PartialSet = set(getattr(PartialStar, 'complexes'))
        OtherSet = set(getattr(OtherStar, 'complexes'))
        PossibleCover = []
        if PartialSet.issubset(OtherSet):
            print "PartialStat is a Subset of OtherStar!"
            return
        else:
            for AV in PartialSet:
                if AV not in PartialSet:
                    PossibleCover.append(AV)


    def simplify(self):
        new_complexes = []
        for elem in self.complexes:
            if elem not in new_complexes:
                new_complexes.append(elem)
        new = []
        for elem in new_complexes:
            for otherelem in new_complexes:
                if set(elem).issubset(set(otherelem)) and elem != otherelem and elem not in new:
                    new.append(elem)

        # print "NEW COMPLEXES??? " + str(new)
        if len(new) > 0:
            self.complexes =  new
        else:
            self.complexes = new_complexes

    #Simple Helper function for adding a selector as a tuple
    def addSelector(self, AttributeName, NegativeValue):
        selector = (AttributeName, NegativeValue)
        if selector not in self.complexes:
            self.complexes.append(selector)

    #Quick way to Trim stuff using MaxStar
    def SimplifyWith(self, MAXSTAR):
        if len(self.complexes) > int(MAXSTAR):
            print "Reducing Complex Number with MaxStar"
            self.complexes = self.complexes[:int(MAXSTAR)]

    def Combine(self, PartialStar):
        # self.complexes.append(PartialStar.complexes)
        newlist = []
        for entry in PartialStar.complexes:
            #  print "entry: " + str(entry)


            for otherentry in self.complexes:
                for thingToAppend in otherentry:
                    templist = []
                    templist.append(entry)
                    # print "This is what is being combined with entry: " + str(thingToAppend)
                    if thingToAppend != entry:
                        templist.append(thingToAppend)
                    else:
                        pass
                    # print "New Rule: " + str(templist)
                    newlist.append(templist)
        # print str(newlist)
        self.complexes = newlist
        print "Combined, new Star Complex List: " + str(self.complexes)
