#!/usr/bin/python3

#######################################################################
# PROGRAM: This program reads input and prints "MATCH!" for each line #
# containing "b0b" or "b1b", and "NO MATCH!" for each line that       #
# doesn't.  When a match is found, the program also tells you what    #
# the bit in between the b's was.                                     #
#######################################################################

import sys             # "sys" module means "system"
import re

# Loop over each line of input
for line in sys.stdin: # loops over each line of input
    mres = re.search(r'b(0|1)b',line) # use r'...' strings for regexs

    if mres:
        print(f"MATCH! Bit was {mres[1]}")
    else:
        print(f"NO MATCH!")