#@author: Patrick Canny
#@topic: EECS690 Project
#@file: interface.py
#@brief: Controls UI stuff etc

from data import data
from LERSReader import LERSReader
from AQ import AQ

from itertools import izip_longest

class Interface(object):
    def __init__(self):
        self.data = data()
        self.aq = AQ()
        self.results = None

    def RUNME(self):
        MyFile = ""
        while MyFile == "":
            MyFile = input("Enter a File to Test: ")

        MyMAXSTAR = None
        while not MyMAXSTAR:
            MyMAXSTAR = input("Enter a MAXSTAR Value: ")
            if MyMAXSTAR == 0:
                print "MAXSTAR Cannot Be 0!"

        MyLERSReader = LERSReader(MyFile)
        MyLERSReader.Read()

        self.data = MyLERSReader.getattr('data')
        self.data.setattr('MAXSTAR') = MyMAXSTAR

        if self.data.getattr('IsNumerical')
            self.TransformToNumerical()

        self.GetBlocks()
        self.IsConsistent()
        self.FindRangeOfAttributes()

        self.results = self.aq.RunAQ(self.data)

    def GetBlocks(self):

        for 
