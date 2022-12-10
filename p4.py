#!/usr/bin/env python3

""" p4 find overlapping ranges """

import re
import sys

#from collections import defaultdict

# if any cli args, assume there's a fie test.txt (used ith the example inputs

if len(sys.argv) == 1:
    inname = "input%s.txt" % (re.sub(r'\D*(\d+).*', r'\1', sys.argv[0]))
else:
    inname = "test.txt"

pat = re.compile(r'\D*(\d+)-(\d+),(\d+)-(\d+)\D*')
def parse_ranges(s, lno):
    """ return start and end points o two ranges """
    r = re.match(pat, s)
    if r is None:
        print("Failed to match pattern at line ", lno, s)
        sys.exit(1)
    arr = r.groups()
    return(int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3]))

def main():
    """ main """
    enclosed = 0
    overlaps = 0
    seen = [0 for i in range(100)]
    lno = 0
    no_pairs = 0
    non_overlaps = 0
    for l in open(inname, 'r').readlines():
        lno += 1
        a, b,c,d = parse_ranges(l, lno)
        if a <= c and b >= d:
            enclosed += 1
            #print(a, b, c, d)
        elif c <= a and d >= b:
            enclosed += 1
            #print(a, b, c, d)
        if a < min(c, d) and b < min(c,d):
            non_overlaps += 1
        elif c < min (a, b) and d < min(a, b):
            non_overlaps += 1
        else:
             overlaps += 1
            
    print("Part 1:", enclosed)
    print("Part 2:", non_overlaps, overlaps)

main()
