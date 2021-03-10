import sys, string


def getBuildingBlocks(path2bbFile): 
#The function gets the building block files and return the required datastructures 
    digits = 3
    aminoMAsses = {}
    standardMasses = set()
    mass2name = {}
    protonMass = 1.00728
    with open(path2bbFile) as bbFile:
        for line in bbFile:
                linesplit = line.strip().split()
                aminoMAsses[linesplit[0]] = round(float(linesplit[3]),digits)
                standardMasses.add(round(float(linesplit[3]),digits))
                mass2name[round(float(linesplit[3]),digits)] = linesplit[0]
    return standardMasses


def writeOriginalSpectra(lines,outputMGF):
    for line in lines:
        outputMGF.write(line)


def findRealPepMass(massGiven,charge):
    protonMass = 1.00728
    realPepMass = massGiven * charge - protonMass
    return realPepMass


