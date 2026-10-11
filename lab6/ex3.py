#!/usr/bin/python3

#######################################################################
# PROGRAM: This program prints "MATCH!" or "NO MATCH!" dependiing on
# whether or not a line contains a string like "<67B>", i.e. number
# followed by A or B, all in <>'s and without spaces.  When a match is
# found, the numeric and letter values are printed out.
#######################################################################

import sys             # "sys" module means "system"
import re

# Loop over each line of input
for line in sys.stdin: # loops over each line of input
    mres = re.search(r'<([0-9]*)(A|B)>',line) # use r'...' strings for regexs

    if mres:
        print(f"MATCH! Bit was ({mres[1]},{mres[2]})")
    else:
        print(f"NO MATCH!")