#!/usr/bin/python3

import sys             # "sys" module means "system"

count = 0
for line in sys.stdin: # loops over each line of input
    if line.strip() == "":
        count += 1
print(f"There were {count} blank lines!")