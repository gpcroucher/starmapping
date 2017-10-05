import math, re

def polarToCartesian(ra, dec, dist, name="star"):
    A = math.radians((int(ra[0]) * 15) + (int(ra[1]) * 0.25) + (float(ra[2]) * 0.004166))
    B = math.radians(math.copysign((abs(int(dec[0])) + (int(dec[1]) / 60) + (float(dec[2]) / 3600)), int(dec[0])))
    C = float(dist[0])

    X = ((C * math.cos(B)) * math.cos(A))
    Y = ((C * math.cos(B)) * math.sin(A))
    Z = C * math.sin(B)

    return { "name":name, "X":X, "Y":Y, "Z":Z }

def convertInputsToCartesian(star):
    ra = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", star["raw_ra"])
    dec = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", star["raw_dec"])
    dist = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", star["raw_dist"])

    return polarToCartesian(ra, dec, dist, star["name"])

def takeInputs():
    name = input("Enter name of object: ")
    raw_ra = input("Enter right ascension: ")
    raw_dec = input("Enter declination: ")
    raw_dist = input("Enter distance in lightyears: ")

    return { "name":name, "raw_ra":raw_ra, "raw_dec":raw_dec, "raw_dist":raw_dist }

def calculateStarDistance(first, second, output=True):
    finaldistance = math.sqrt( (first["X"] - second["X"])**2 + (first["Y"] - second["Y"])**2 + (first["Z"] - second["Z"])**2 )
    if output:
        print("The distance between", first["name"], "and", second["name"], "is", finaldistance, "ly")
    return finaldistance

first = takeInputs()
second = takeInputs()
calculateStarDistance(convertInputsToCartesian(first), convertInputsToCartesian(second))

#finaldistance = math.sqrt( ((firstobject[0] - secondobject[0])**2) + ((firstobject[1] - secondobject[1])**2) + ((firstobject[2] - secondobject[2])**2) )

#print("The distance between", firstobject[3], "and", secondobject[3], "is", finaldistance, "ly")
