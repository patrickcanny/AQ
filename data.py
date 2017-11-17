#@author: Patrick Canny
#@topic: EECS690 Project
#@file: data.py
#@brief: defined a dataset as an object in order ot handle stuff easier.
class data:
    def __init__(self):
        #The list of attricubes affiliated with a given dataset.
        self.ListOfAttributtes = []
        self.AttributeRange = []

        #The list of all the cases
        self.AllCases = []

        #Data can be either numerical or symbolic in our case
        self.IsNumerical = False
        #ASTAR and DSTAR are used to calculate if the dataset is consistent or not.
        self.ASTAR = None
        self.DSTAR = None
        self.IsConsistent = True

        #MAXSTAR is a parameter that regualtes the number of rules generated through seed selection
        self.MAXSTAR = None

    def __getattr__(self, name):
        return self.name

    def __setattr__(self, name, value):
        self.name = value

    def addNewCaseToDataset(self, case):
        self.AllCases.append(case)
