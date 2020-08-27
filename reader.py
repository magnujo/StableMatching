import os
import sys
from Person import Person

n = 0
setUpNames = True
isMale = True

males = []
females = []

def parse():
    for line in sys.stdin:
        if line.startswith("#"):
            continue
        elif (line.startswith("n=")):
            n = int(line[2:len(line) - 1])
        elif not line.strip():
            setUpNames = not setUpNames
        elif setUpNames:
            data = line.split(" ")
            name = data[1]
            index = data[0]
            p = Person(name, index, [])
            
            if (isMale):
                males.append(p)
            else:
                females.append(p)

            isMale = not isMale

        elif not setUpNames:
            index = int(line[0])
            prefs = line[line.index(":") + 1:].strip().split(" ")
            if index % 2 == 0:
                females[int((index/2) - 1)].prefrences = prefs
            else:
                males[int(index/2)].preferences = prefs