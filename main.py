#@Author: Patrick Canny
#@File: main.py
#Controller/interface for the program
import os
from AQ import AQ
from DataParser import DataParser
from DataSet import DataSet

#setup a checker bool
checkTheFile = False

#clear screen for readability's sake
for i in range(0,100):
    print " "

#Welcome User!
print "Welcome to Patrick Canny's AQ Rule Inductor!"

#While the bool from above is not true, continually prompt for a filename
while not checkTheFile:
    MyFile = raw_input('Please Enter a Filename (i.e. "datasets/simpledata.txt"): ')
    #Make sure the file is valid by testing it out and catching the IOexception
    try:
        tester = open(MyFile, 'r')
        print "Great file choice! Let's get down to business."
        checkTheFile = True
        break
    except IOError:
        print "Sorry, that's not a good file name :("

#Declaration of DataParser Object
Parser = DataParser(MyFile)

#Actually Get the Data
myData = Parser.Read()
myData.ChangeConceptNames()
myData.ChangeConceptCases()
myData.ChangeAttributeValues()
print "Initializing AQ..."

#Initializing AQ...
myAQ = AQ(myData)
myAQ.DataSet.PrintProcessedData()

#Get MAXSTAR from the user
checker = False
while not checker:
    MaxStar = raw_input("Please Enter a MaxStar Value: ")
    try:
        ms = int(MaxStar)
        if ms > 0:
            checker = True
        else:
            print "MaxStar Must be greater than 0"
    except:
        print "Sorry, but MaxStar must be and integer greater than 0!"

#Actually run AQ...it's that easy.
myAQ.runAQ(MaxStar)
print "Ran AQ!"

#Simplify your potentially messed up rules
myAQ.SimplifyRuleSet()

#Write all the rules from AQ to the required files
myAQ.WriteRulesWithNegation()
myAQ.WriteRulesWithoutNegation()

print "Thanks!"
