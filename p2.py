#!/usr/bin/env python3

""" p2 score scissor/paper rock """

import re
import sys

#from collections import defaultdict

if len(sys.argv) == 1:
    inname = "input%s.txt" % (re.sub(r'\D*(\d+).*', r'\1', sys.argv[0]))
else:
    inname = "test.txt"
        
# map col1 to rps
p1vals = {'A': 'r', 'B': 'p', 'C': 's'}

p1res = { 'rr': 1 + 3, 'rp': 1 + 0, 'rs': 1 + 6,
          'pr': 2 + 6, 'pp': 2 + 3, 'ps': 2 + 0,
          'sr': 3 + 0, 'sp': 3 + 6, 'ss': 3 + 3
        }
             
p2res = { 'rr': 1 + 3, 'rp': 2 + 6, 'rs': 3 + 0,
          'pr': 1 + 0, 'pp': 2 + 3, 'ps': 3 + 6,
          'sr': 1 + 6, 'sp': 2 + 0, 'ss': 3 + 3
        }

p2vals =  [ {'X': 'r', 'Y': 'p', 'Z': 's'},
            {'X': 'r', 'Z': 'p', 'Y': 's'},
            {'Y': 'r', 'X': 'p', 'Z': 's'},
            {'Y': 'r', 'Z': 'p', 'X': 's'},
            {'Z': 'r', 'X': 'p', 'Y': 's'},
            {'Z': 'r', 'Y': 'p', 'X': 's'} ]


results = [ [0,0] for i in range (6)]
for l in open(inname, 'r').readlines():
    l = l.strip()
    p1 = p1vals[l.split()[0]]
    l2  = l.split()[1]
    for perm in range(6):
        # or all the mappings or XYZ, ind a letter
        p2 = p2vals[perm][l2]
        play = '%s%s' % (p1, p2)
        results[perm] = [results[perm][0] + p1res[play], results[perm][1] + p2res[play]]

for prm in range(6):
    print(prm, results[prm])

playlist = { 'rX': 's', 'rY': 'r', 'rZ': 'p',
             'pX': 'r', 'pY': 'p', 'pZ': 's',
             'sX': 'p', 'sY': 's', 'sZ': 'r' }

score = 0                          
for l in open(inname, 'r').readlines():
    l = l.strip()
    p1 = p1vals[l.split()[0]]
    l2 = l.split()[1]
    p2 = playlist["%s%s" % (p1, l2)]
    score += p2res["%s%s" % (p1, p2)]
print(score)
    
