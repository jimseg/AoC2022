#!/usr/bin/env python3

""" p3 find common letters in strings """

import re
import sys

#from collections import defaultdict

# if any cli args, assume there's a fie test.txt (used ith the example inputs

if len(sys.argv) == 1:
    inname = "input%s.txt" % (re.sub(r'\D*(\d+).*', r'\1', sys.argv[0]))
else:
    inname = "test.txt"
    
def common(s1, lno, score):
    """ totalise common letters in string halves """
    sl = set(list(s1[:len(s1)//2]))
    sr = set(list(s1[len(s1)//2:]))
    com = sl.intersection(sr)
    if len(com) != 1:
        print("Error on line %d: %d elements in common %s %s", lno, len(com), sl, sr)
        return 0
    v = ord(com.pop())
    if v in range(ord('a'), ord('z') + 1):
        score += v + 1 - ord('a')
    else:
        score += v + 27 - ord('A')
    #print("    %c %d" %( v, score))
    return score

score = 0
lno   = 0                        
for l in open(inname, 'r').readlines():
    lno += 1
    l = l.strip()
    score = common(l, lno, score)
    
print("Part 1: ", score)


def com3(a, b, c, lno, score):
    """ totaiise common letters in string triples """
    sa = set(list(a))    
    sb = set(list(b))    
    sc = set(list(c))
    com = sa.intersection(sb.intersection(sc))
    if len(com) != 1:
        print(sb, sc, sb.intersection(sc))
        print(sa, sb.intersection(sc), sa.intersection(sb.intersection(sc)))
        print("Found", len(com), " common chars at", lno - 3)
        sys.exit(1)
    v = ord(com.pop())
    if v in range(ord('a'), ord('z') + 1):
        score += v + 1 - ord('a')
    else:
        score += v + 27 - ord('A')
    #print("    %c %d" %( v, score))
    return score
                                            
f =  open(inname, 'r')
score = 0
lno   = 0

while True:
    a = f.readline().strip()
    lno += 1
    if a == "":
        break
    b = f.readline().strip()
    lno += 1
    if b == "":
        print("Ran out of input on line", lno)
        sys.exit(1)
    c = f.readline().strip()
    lno += 1
    if c == "":
        print("Ran out of input on line", lno)
        sys.exit(1)
    score = com3(a, b, c, lno, score)
print("Part2:", score)

    
