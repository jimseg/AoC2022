#!/usr/bin/env python3

""" marker sequences """

import re
import sys

#from collections import defaultdict

# if any cli args, assume there's a fie test.txt (used ith the example inputs

if len(sys.argv) == 1:
    inname = "input%s.txt" % (re.sub(r'\D*(\d+).*', r'\1', sys.argv[0]))
else:
    inname = "test.txt"


def main():
    """ ust look and match """
    for l in open(inname, 'r').readlines():
        a = list(l)
        for i in range(len(a) - 4):
            if a[i] == a[i + 1] or      \
                a[i] == a[i + 2] or     \
                a[i] == a[i + 3] or     \
                a[i + 1] == a[i + 2] or \
                a[i + 1] == a[i + 3] or \
                a[i + 2] == a[i + 3]:
                continue
            break
        print("offset:", i + 4, a[i: i + 4])
    for l in open(inname, 'r').readlines():
        a = list(l)
        i = 0
        while i < (len(a) - 14):
            arr = a[i: i + 14]
            s   = set(arr)
            if len(s) == 14:
                print(i + 14, len(arr), len(s),arr, s)
                break
            i += 1
main()
