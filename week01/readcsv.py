# readcsv.py
# A program to read a csv file and output each line as a list
# Also calculates the average age by reading numbers as floats rather than strings
# An alternative version (commented out) converts the strings to ints
# Author: David O'Connell

import csv
FILENAME = "data.csv"
DATADIR = ""  # it's in this directory, so relative path is blank

with open(DATADIR+FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        print (line)
        total += line['age']
        linecount += 1
    print ("average is ", total/linecount)