class Star(object):
    def __init__(self, PartialStar=None, OtherStar=None , _bool=None):
        super(Star, self).__init__()
        self.complexes = []


    # Simplification stuff
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
        newlist = []
        for entry in PartialStar.complexes:

            for otherentry in self.complexes:
                for thingToAppend in otherentry:
                    templist = []
                    templist.append(entry)
                    if thingToAppend != entry:
                        templist.append(thingToAppend)
                    else:
                        pass
                    newlist.append(templist)
        self.complexes = newlist
        # print "Combined, new Star Complex List: " + str(self.complexes)
