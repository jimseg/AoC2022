#!/usr/bin/env python3

""" forests """

import re
import sys

#from collections import defaultdict

# if any cli args, assume there's a fie test.txt (used ith the example inputs

if len(sys.argv) == 1:
    inname = "input%s.txt" % (re.sub(r'\D*(\d+).*', r'\1', sys.argv[0]))
else:
    inname = "test.txt"

#  H..   T..    .H.   .T.   T..   H..   ..T.   ..T   H.T    H..   H..   T..   T..  T.H   ..H  ..H
#  ...   ...    ...   ...   ...   ...   ...    H..   ...    ..T   ...   ...   ..H  ...   T..   ...
#  T..   H..    T..   H..   .H.   .T.   H..    ...   ..     ...   ..T   ..H   ...  ...   ...   T..
#   0     1      2     3     4     5     6      7     8     9    10    11     12    13    14   15
# DX=0  DX=0   DX=1  DX=-1 DX=1  DX=-1 DX=-2  DX=-2 DX=-2 DX=-2 DX=-2  DX=2  DX=2  DX=2  DX=2 DX=2
# DY=2  DY=-2  DY=2  DY=-2 DY=-2 DY=2  DY=-2  DY=-1 DY=0  DY=1  DY=2   DY=-2 DY=-1 DY=0  DY=1 DY=2
# up    dwn    up-R  dwn-L dwn-R up=L  dwn-L  dwn-L left  up-L  up-L   dwn-R dwn-R right up-R up-r

# for every possible head/tail position AFTER a move of the head, identiy rhe reulting
# coniguration based on delta x and delta y. If it's one of the above, make a move of
# the tail 
adjmap = {( 0, 2): 0, ( 0, -2): 1, ( 1, 2): 2, (-1,-2): 3, (1,-2): 4, (-1, 2): 5,
          (-2,-2): 6, (-2, -1): 7, (-2, 0): 8, (-2, 1):9, (-2, 2): 10,
          ( 2, -2): 11, (2,-1): 12, (2, 0): 13, (2, 1): 14, (2, 2): 15}

# for each of the above, what has to be done to the tail position
#           0     1      2      3      4       5      6       7       8      9     10    11     12     13     14   15
#           up   dwn    up-R  dwn-L   dwn-R   up-L   dwn-L   dwn-L   left   up-L   up-L dwn-R   dwn-R  right up-R  up-r
fixups = [(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1),(-1,-1),(-1,-1),(-1,0),(-1,1),(-1,1),(1,-1),(1,-1),(1, 0),(1,1),(1,1)]

# update tuples per_command

cmd_tpls = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

visited = set()
tx = ty = hx = hy = minx = maxx = miny = maxy = 0

def get_adj(tx, ty, hx, hy):
    """identiy which of the 9 possible layouts we are in"""
    tpl = (hx - tx, hy - ty)
    adj = adjmap.get(tpl, None)
    return adj

def p1_rep(tpl, n):
    """repeat command n times part 1, single head and tail"""
    global tx, ty, hx, hy, minx, maxx, miny, maxy
    #print()
    while n > 0:
        n -= 1
        hx += tpl[0]
        hy += tpl[1]
        adj = get_adj(tx, ty, hx, hy)
        if adj is not None:
            dx, dy = fixups[adj]
            tx += dx
            ty += dy
            #print("fixup:", adj,(dx, dy))
        visited.add((tx, ty))
        #print("p1_rep",tx,ty,hx,hy,tpl,n, adj, (hx - tx, hy - ty))
        #print_map()
        
heads = [(0, 0) for i in range(10)]
tails = [(0, 0) for i in range(10)]

def p2_rep(tpl, n):
    """repeat command n times part 1, single head and tail"""
    global maxx, maxy, minx, miny
    while n > 0:
        n -= 1
        (hx, hy) = heads[0]
        (tx, ty) = tails[0]
        hx += tpl[0]
        hy += tpl[1]
        heads[0] = (hx, hy)
        adj = get_adj(tx, ty, hx, hy)
        #print("p2_rep",tx,ty,hx,hy,tpl,n, adj, (hx - tx, hy - ty), len(visited))
        for idx in range(9):
            tx, ty = tails[idx]
            adj = get_adj(tx, ty, hx, hy)
            if adj is None:
                break
            dx, dy = fixups[adj]
            tx += dx
            ty += dy
            tails[idx] = (tx, ty)
            if(idx < 9):
                heads[idx + 1] = (tx, ty)
            #print(idx, (tx, ty))
            hx, hy = tx, ty
            maxx = max(hx, tx, maxx, 0)
            minx = min(hx, tx, minx, 0)
            maxy = max(hy, ty, maxy, 0)
            miny = min(hy, ty, miny, 0)
            visited.add(heads[-1])
                    
def print_map():
    """show working"""
    global tx, ty, hx, hy
    for row in range(6, -1, -1):
        for col in range(6):
            c = '.'
            if row == hy and col == hx:
                c = 'H'
            elif row == ty and col == tx:
                c = 'T'
            elif (col, row) in visited:
                c = '#'
            print("%s" % c, end = '')
        print()
    print()

def print_p2(l):
    """part 2 map"""
    for row in range(20, -1, -1):
        for col in range(26):
            c = '.'
            #if (row, col) == (5, 11   ):
            #    c = 's'
            #elif (col, row) == heads[0]:
            if (col, row) == heads[0]:
                c = 'H'
            else:
                for n, tpl in enumerate(heads):
                    if n == 0:
                        continue
                    if (col, row) == tpl:
                        c = "%d" % n
                        break
            print("%s" %c, end = '')
        print()
    print(l, "\n")

def print_visited(l):
    """part 2 map"""
    global maxx,maxy, minx, miny
    for row in range(maxy, miny -1, -1):
        for col in range(minx, maxx +1):
            c = '.'
            if (col, row) in visited:
                c = '#'
            print("%s" %c, end = '')
        print()
    print(l, "\n")

def main():
    """ go exploring """
    global tx, ty, hx, hy, minx, maxx, miny, maxy
    visited.add((tx, ty))
    for l in open(inname, 'r').readlines():
        cmd, count = l.strip().split()
        count = int(count)
        tpl = cmd_tpls[cmd]
        #print(cmd, tpl, hx, hy, tx, ty, count)
        p1_rep(tpl, count)
        if len(sys.argv) > 1:
            print_map()
    print("Part 1", len(visited))

    fname = inname
    if len(sys.argv) > 1:
        fname = "test9.txt"
    visited.clear()
    for i in range(10):
        heads[i] = (11, 5)
        tails[i] = (11, 5)
    #print_p2("initial")
    for l in open(fname, 'r').readlines():
        cmd, count = l.strip().split()
        count = int(count)
        tpl = cmd_tpls[cmd]
        p2_rep(tpl, count)
        #print("\n",l)
        if len(sys.argv) > 1:
            print_p2(l)
    print("Part 2:", len(visited))
    print_visited('Visited')
        
main()        
