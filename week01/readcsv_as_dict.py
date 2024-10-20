# readcsv.py
# A program to read a csv file and output each line as a list
# Author: David O'Connell

import csv
FILENAME = "data.csv"
DATADIR = ""  # it's in this directory, so relative path is blank

with open(DATADIR+FILENAME, "rt") as fp:
    #reader = csv.reader(fp, delimiter=",")
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    avg = 0
    for line in reader:
        if not linecount:  # header row
            print (f"\n{line}\n---------------------")  # each line is printed as a list
        else:  # all subsequent rows
            print (line)
            #avg += int(line[1])
            avg += line[1]
        linecount += 1
    avg = avg/(linecount-1)
    print ("average is ", avg)