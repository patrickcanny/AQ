class Star(object):
    def __init__(self, PartialStar=None, OtherStar=None , _bool=None):
        super(Star, self).__init__()
        self.complexes = []
        self.MyBool = _bool
        self.PartialStar = PartialStar
        self.OtherStar = OtherStar
        if PartialStar and OtherStar:
            myset = set(PartialStar.complexes).union(set(OtherStar.complexes))
            self.complexes = list(myset)
        if self.MyBool:
            self.simplify()

    def SimplifyWith(self):
        for FirstComplex in complexes[0]:
            for SecondComplex in complexes[1]:
                if set(FirstComplex).issuperset(set(SecondComplex)):
                    pass#Remove Redundant complexes
                elif set(SecondComplex).issuperset(FirstComplex):
                    pass#Remove Redundant

    def addSelector(self, AttributeName, NegativeValue):
        selector = (AttributeName, NegativeValue)
        myComplex = list(selector)
        complexes.append(myComplex)

    def reduce(self, MAXSTAR):
        if len(complexes) > MAXSTAR:
            complexes = complexes[:MAXSTAR]

    def Concatenate(self, S, mybool = True):
        for Complex in S.complexes:
            complexes.append(Complex)
