#!/usr/bin/env python3

""" crt """

import re
import sys

#from collections import defaultdict

# if any cli args, assume there's a fie test.txt (used ith the example inputs

if len(sys.argv) == 1:
    inname = "input%s.txt" % (re.sub(r'\D*(\d+).*', r'\1', sys.argv[0]))
else:
    inname = "test%s.txt" %  (re.sub(r'\D*(\d+).*', r'\1', sys.argv[0]))

cycle   = 0
xreg  = 1
checks = [20, 60, 100, 140, 180, 220 ]
sums   = 0

xvals = []

def do_addx(n):
    """incremetor"""
    global cycle,  xreg, checks, sums
    #print("%4d %8d %8d" % (cycle, xreg, xreg * (cycle + 1)))
    #print("%4d %8d %8d" % (cycle + 1, xreg, xreg * (cycle + 2)))
    if cycle + 1 in checks:
        sums += xreg * (cycle + 1)
    xvals.append(xreg)
    if cycle + 2 in checks:
        sums += xreg * (cycle + 2)
    xvals.append(xreg)   
    cycle += 2
    xreg += n

def noop():
    """time killer"""
    global cycle,  xreg, checks, sums
    #print("%4d %8d %8d" % (cycle, xreg, xreg * cycle))
    if cycle + 1 in checks:
        sums += xreg * (cycle + 1)
    xvals.append(xreg)
    cycle += 1    

def main():
    """doit"""
    global sums, xvals
    for l in open(inname, 'r').readlines():
        l = l.strip()
        if l == "noop":
            noop()
        else:
            cmd, val = l.split()
            val = int(val)
            if cmd != 'addx':
                print('WT?', l)
                sys.exit(1)
            do_addx(val)
    print("Part 1:", sums)
    screen = [['.' for col in range(40)] for row in range(6)]
    # split each row off to get xvals
    row_no = len(screen) - 1
    while len(xvals) > 0:
        xrow =  xvals[:40]
        xvals = xvals[40:]
        #print(xrow)
        for col, xval in enumerate(xrow):
            #print((col, xval), end=' ')
            if xval - 1 <= col <= xval+ 1:
                screen[row_no][col] = '#'
            else:
                screen[row_no][col] = ' '
        row_no -= 1
        #print()
    for i in range (len(screen)-1, -1, -1):
        row = screen[i]
        for col in range(40):
            print('%s' % row[col], end = '')
        print()
                
main()
