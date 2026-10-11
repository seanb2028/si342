# Sean Beckford
import sys
import re

for line in sys.stdin:
    mres = re.search(r'([MTWRF]+\d{1,2})', line)

    if mres:
        print(mres[1])