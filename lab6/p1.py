# Sean Beckford
import sys
import re

for line in sys.stdin:
    mres = re.search(r'SI([0-9][0-9][0-9][A-Z]*)', line)

    if mres:
        print(mres[1])