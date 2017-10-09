#import calculate-star-distance.py as calc
import csv

# base = input("Enter name of star: ")

working_list = []
fieldnames = []

with open("hygdata_v3.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if "I" in row["spect"]:
            working_list.append(row)
    fieldnames = reader.fieldnames

#print(working_list)

with open("output.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames)
    writer.writeheader()
    writer.writerows(working_list)

# with open("output.csv"
