# Sean Beckford
import sys
import re

for line in sys.stdin:
    mres = re.search(r'<b>(([A-Z]*[a-z]*[ ]*)*)</b>', line)

    if mres:
        print(mres[1])