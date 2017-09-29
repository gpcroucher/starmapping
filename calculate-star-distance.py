import math, re

def polarToCartesian(ra, dec, dist, name="star"):
    A = math.radians((int(ra[0]) * 15) + (int(ra[1]) * 0.25) + (float(ra[2]) * 0.004166))
    B = math.radians(math.copysign((abs(int(dec[0])) + (int(dec[1]) / 60) + (float(dec[2]) / 3600)), int(dec[0])))
    C = float(dist[0])

    print(A)
    print(B)
    print(C)

    print(math.cos(A))
    print(math.cos(B))

    X = ((C * math.cos(B)) * math.cos(A))
    Y = ((C * math.cos(B)) * math.sin(A))
    Z = C * math.sin(B)

    return [X, Y, Z, name]

name = input("Enter name of first object: ")
raw_ra = input("Enter right ascension: ")
raw_dec = input("Enter declination: ")
raw_dist = input("Enter distance in lightyears: ")

ra = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", raw_ra)
dec = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", raw_dec)
dist = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", raw_dist)

print(ra)
print(dec)
print(dist)

firstobject = polarToCartesian(ra, dec, dist, name)

name = input("Enter name of second object: ")
raw_ra = input("Enter right ascension: ")
raw_dec = input("Enter declination: ")
raw_dist = input("Enter distance in lightyears: ")

ra = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", raw_ra)
dec = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", raw_dec)
dist = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", raw_dist)

print(ra)
print(dec)
print(dist)

secondobject = polarToCartesian(ra, dec, dist, name)

finaldistance = math.sqrt( ((firstobject[0] - secondobject[0])**2) + ((firstobject[1] - secondobject[1])**2) + ((firstobject[2] - secondobject[2])**2) )

print("The distance between ", firstobject[3], "and ", secondobject[3], "is ", finaldistance, "ly")