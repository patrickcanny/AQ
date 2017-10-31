#@author: Patrick Canny
#@topic: EECS690 Project
#@file: LERSReader.py
#@brief: Reads File Data in LERS Format and Processes

def Prompt():
    filename = ""
    while filename == "":
        filename = input('Enter a Filename: ')


#@Brief: Reads a file give a name fot that file
#@Pre: File name
#@Post: N/A
#@Return: File-Size Array, where each entry corresponds to each line of the file.
def Read(filename):
    myFile = open(filename, "r")
    lineArray = myFile.read().split('\n')
    return lineArray

#@Brief:
#@Pre:
#@Post:
#@Return:
def FindNumberOfAttributes(Data):
    attributes = 0
    for char in Data:
        if char ! = "d"
        attributes += 1
        else
        continue

#@Brief:
#@Pre:
#@Post:
#@Return:
def ParseData(Data):
    AttributeNo = FindNumberOfAttributes(Data[1])
    noEntries = len(Data)-2
    DATASET = [[0 for x in range(AttributeNo+1)]for y in range(noEntries)]
