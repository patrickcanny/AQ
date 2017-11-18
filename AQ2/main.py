import os
from AQ import AQ
from DataParser import DataParser
from DataSet import DataSet

checkTheFile = False

for i in range(0,100):
    print " "

print "Welcome to Patrick Canny's AQ Rule Inductor!"

while not checkTheFile:
    MyFile = raw_input('Please Enter a Filename (i.e. "datasets/simpledata.txt"): ')
    try:
        tester = open(MyFile, 'r')
        print "Great file choice! Let's get down to business."
        checkTheFile = True
        break
    except IOError:
        print "Sorry, that's not a good file name :("

Parser = DataParser(MyFile)

myData = Parser.Read()

myData.PrintProcessedData()

print "Initializing AQ..."
myAQ = AQ()

MaxStar = 0
while MaxStar <= 0:
    MaxStar = raw_input("Please Enter a MaxStar Value: ")

myAQ.runAQ(MaxStar)
print "Ran AQ!"

myAQ.WriteRulesWithNegation()
myAQ.WriteRulesWithoutNegation()

print "Thanks!""
