# This is code anonymise the sub domains of ip addresses 
# Author: Andrew Beatty

import re

regex = "\d{1,3}\.\d{1,3} " # note the space at the end
replacementText="XXX.XXX " # note the space at the end to match above
filename = "./smallerAccess.log"
outputFileName = "anonymisedIPs.txt"

with open(filename) as inputFile:
    with open(outputFileName, 'w') as outputFile:
        for line in inputFile:
            # for debugging
            #foundText = re.search(regex, line).group()
            #print(foundText)
            newLine = re.sub(regex, replacementText, line)
            print(newLine)
            outputFile.write(newLine)
            