#!/usr/bin/env python3

""" p1 find max total """

import re
import sys

from collections import defaultdict

rations = defaultdict(lambda: 0)

elf = 1

if len(sys.argv) == 1:
    inname = "input%s.txt" % (re.sub(r'\D*(\d+).*', r'1', sys.argv[0]))
else:
    inname = "test.txt"
    
                          
for l in open(inname, 'r').readlines():
    l = l.strip()
    if l == "":
        elf += 1
        continue
    rations[elf] += int(l)

#orted(x.items(), key=lambda item: item[1])
arr = sorted(rations.items(), key=lambda item: item[1])
print('Part 1:', arr[-1][1])

print("Part 2:", arr[-1][1] + arr[-2][1] + arr[-3][1])
