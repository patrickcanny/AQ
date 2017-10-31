#@author: Patrick Canny
#@topic: EECS690 Project
#@file: AQ.py
#@brief: Implementation fo the AQ Algorithm

import LERSReader
import PrintProcessedData
import re
import sys
import time

#@function: RunAQ
#@pre: data set as a matrix
#@post: rules covering each concept in the data set
def RunAQ(data):
    if data:
        allCovered = False
        while not allCovered:
            cover =

#@function: Star
#@pre: seed case and negative examples
#@post:
def Star(seed, neg):



#@function: GenerateRule
#@pre: List of Conditions, concept being covered
#@post: Sensical rules
def GenerateRule(parameters, concept):
    rule = ""
    for condition in parameters:
        if rule == "":
            rule += condition
        else:
            rule += " & " + condition
    rule += " ----> "+ concept
    return rule
