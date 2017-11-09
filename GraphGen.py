import sys
import math

"""
    To use this script, write in a shell:
    python3 GraphGen.py genGraph graphName.frog
"""

graph = """
    \"graph\": {
        \"_id\": \"cj9dzz33p00013h6t32a00000\",
        \"name\": \"auto-inducSet(3 types)\",
        \"createdAt\": \"2017-10-30T09:44:02.677Z\",
        \"duration\": 120,
        \"broken\": false
    },"""

properties = """
                \"properties\": [
                    \"at least one is not filled\",
                    \"at most one is filled\",
                    \"they all have the same shape\",
                    \"they all have the same color\",
                    \"they all have different shapes\",
                    \"they all have different colors\",
                    \"exactly 2 have the same shape\",
                    \"exactly 2 have the same color\"
                ],"""


def genOneExample(a,b,c):
    tmp = range(3,6)
    incorrect = 'true'
    respected = ''

    if a%3 == b%3 == c%3:
        respected += '2,'
    elif (a%3 == b%3) | (a%3 == c%3) | (b%3 == c%3):
        respected += '6,'
    else:
        respected += '4,'

    if math.floor(a/3) == math.floor(b/3) == math.floor(c/3):
        respected += '3,'
    elif (math.floor(a/3) == math.floor(b/3)) | (math.floor(a/3) == math.floor(c/3)) | (math.floor(b/3) == math.floor(c/3)):
        respected += '7,'
    else:
        respected += '5,'

    if (a not in tmp) | (b not in tmp) | (c not in tmp):
        respected += '0,'
    if ((a not in tmp) & (b not in tmp) & (c not in tmp)) | ((a in tmp) & (b not in tmp) & (c not in tmp)) | ((a not in tmp) & (b not in tmp) & (c in tmp)) | ((a not in tmp) & (b in tmp) & (c not in tmp)):
        respected += '1,'
    respected = respected[:-1]
    tmp = respected.split(',')
    if ('2' in tmp) & (('3' in tmp) | ('5' in tmp)):
            incorrect = 'false'
    if ('4' in tmp) & (('3' in tmp) | ('5' in tmp)):
            incorrect = 'false'

    text = """
                    {
                        \"url\": \"https://raw.githubusercontent.com/romainAA/imagesSetSP/master/ImagesTest/img""" + str(a) + str(b) + str(c) + """.png\",
                        \"isIncorrect\": """ + incorrect + """,
                        \"respectedProperties\": \"""" + respected + """\"
                    },"""
    return text

def genExamples():
    expls = ''
    for a in range(9):
        for b in range(9):
            for c in range(9):
                if(a == b == c == 8):
                    expls += genOneExample(a,b,c)[:-1]
                else:
                    expls += genOneExample(a,b,c)
    return expls

examples = """
                "examples": [""" + genExamples() +"""
                ]"""

data = """
            \"data\": {
                \"title\": \"a set\",
                \"hasExamples\": true,
                \"nbExamples\": 6,
                \"hasTestWithFeedback\": true,
                \"nbTestFeedback\": 4,
                \"hasDefinition\": true,
                \"definition\": \"A set is correct only in the case that if 2 objects of the set share a property, the third object should also have this property\",
                \"hasTest\": true,
                \"nbTest\": 6,""" + properties + """
                \"suffisantSets\": \"{2,3},{2,5},{3,4},{5,4}\",
                \"contradictoryProperties\": \"6,7\",
                \"unnecessaryProperties\": \"0,1,2,3,4,5\",""" + examples + """
            }"""

activities = """
    \"activities\": [
        {
            \"_id\": \"cj9dzz33r00023h6tb64ligbc\",
            \"title\": \"Unnamed\",
            \"startTime\": 0,
            \"length\": 5,
            \"plane\": 1,
            \"activityType\": \"ac-induction\",""" + data + """
        }
    ],"""

operators = """
    \"operators\": [],"""

connections = """
    \"connections\": []"""

def genGraph(x):
    f = open(x, 'w')
    f.write('{')
    f.write(graph)
    f.write(activities)
    f.write(operators)
    f.write(connections)
    f.write('\n}')
    f.close()

if __name__ == "__main__":
    function = getattr(sys.modules[__name__], sys.argv[1])
    filename = sys.argv[2]
    function(filename)
