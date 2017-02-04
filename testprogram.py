#!/usr/bin/env python

# import our log file class
from clsWriteFile import clsWriteFile

#create our log file object from clsWriteFile
objLogFile = clsWriteFile("Log File.txt", True)

#create our user file object from clsWriteFile
objUserFile = clsWriteFile("User File.txt")

for i in range (0,101):                         # if i is evenly divisible by 25
    if i % 25 == 0:
        # then write the value of i to a log file
        objLogFile.setWriteFile("We are at " + str(i) + "%")

        # if i is greater than 0 & evenly divisible by 100
        if (i > 0) & (i % 100 == 0):
            #then write the value of i to the user file
            objUserFile.setWriteFile("Cycle complete.")
