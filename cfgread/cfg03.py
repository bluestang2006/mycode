#!/usr/bin/env python3

## create file object in "r"ead mode
file = input("Enter the filename of the cfg file to read: ")
with open(file, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
lines = 0
for x in configlist:
    lines += 1
    print(x.strip())
print("Total number of lines =", lines)

