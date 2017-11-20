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
        self.complexes = list(new_complexes)

    def addSelector(self, AttributeName, NegativeValue):
        selector = (AttributeName, NegativeValue)
        if selector not in self.complexes:
            self.complexes.append(selector)

    def SimplifyWith(self, MAXSTAR):
        if len(self.complexes) > MAXSTAR:
            print "Reducing Complex Number with MaxStar"
            self.complexes = self.complexes[:MAXSTAR]

    def Combine(self, S, mybool = True):
        for Complex in S.complexes:
            self.complexes.append(Complex)
