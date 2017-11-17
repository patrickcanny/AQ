#@author: Patrick Canny
#@topic: EECS690 Project
#@file: LERSReader.py
#@brief: Reads File Data in LERS Format and Processes
import data

class LERSReader:
    def __init__(self, MyFile):
        self.MyFile = MyFile
        self.data = data()

    def Prompt():
        self.MyFile = ""
        while self.MyFile == "":
            MyFile = input('Enter a Filename: ')

    #@Brief: Parses data, adding to dataset appropriately
    #@Pre: File
    #@Post: Parsed dataset
    #@Return: none
    def ParseData(self, File):
        for line in File:
            row = line
            head, sep, tail = line.partition('!')
                if head == "" or head.isspace():
                    row = tail
                else:
                    row = head
                    if row[0] == '<':
                        continue
                    elif row[0] == '[':
                        DefineAttributes(row)
                    else:
                        AddCase(row)

    #@Brief: Defines the attributes for data
    #@Pre: The row of data that is the attribute/decision row
    #@Post: Definition for the attributes and decision in data
    #@Return: none
    def DefineAttributes(row):
        AttributesAndDecision = [[],[]]
        attribute = row.split()
        indicies = 0, -1
        attribute = [i for j, i in enumerate(attribute) if j not in indicies]

        AttributesAndDecision[1].append(attribute[len(attribute)-1])
        del attribute[-1]
        AttributesAndDecision[0] = attribute

        self.data.setattr('ListOfAttributtes') = AttributesAndDecision

    #@Brief: adds a case to the dataset
    #@Pre: a row of data (a given case from file)
    #@Post: adds that case to the dataset
    #@Return: none
    def AddCase(row):
        case = row.split()

        AllCases = [[],[]]
        AllCases.append(case[len(case)-1])
        del case[-1]
        for i in range(len(case)):
            try:
                case[i] = float(case[i])
                self.data.setattr(IsNumerical) = True
            except ValueError:
                continue

        AllCases[0] = case
        self.data.addNewCaseToDataset(case)

    #@Brief: Reads a file give a name fot that file
    #@Pre: File name
    #@Post: Parsed Data
    #@Return: none
    def Read(self):
        self.File = open(self.MyFile, 'r')
        ParseData(self.File)

    #getter
    def __getattr__(self):
        return data
