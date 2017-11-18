class Star(object):
    def __init__(self, PartialStar = None, OtherStar = None, _bool):
        super(Star, self).__init__()
        self.complexes = []
        self.MyBool = _bool
        self.PartialStar = PartialStar
        self.OtherStar = OtherStar
        
