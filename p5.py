#!/usr/bin/env python3

""" Towers of Hanoi? """

import re
import sys

#from collections import defaultdict

# if any cli args, assume there's a fie test.txt (used ith the example inputs

if len(sys.argv) == 1:
    inname = "input%s.txt" % (re.sub(r'\D*(\d+).*', r'\1', sys.argv[0]))
else:
    inname = "test.txt"

piles = []    
    
def restack_p1(n, s, d, lno):
    """ move n creates from source s to destination d """
    if len(piles[s]) < n:
        print("Move is too large for line", lno)
        sys.exit(1)
    chunk = piles[s][:n]
    piles[s] = piles[s][n:]
    chunk.reverse()
    piles[d] = chunk + piles[d]

def restack_p2(n, s, d, lno):
    """ move n creates from source s to destination d """
    if len(piles[s]) < n:
        print("Move is too large for line", lno)
        sys.exit(1)
    chunk = piles[s][:n]
    piles[s] = piles[s][n:]
    #chunk.reverse()
    piles[d] = chunk + piles[d]

def print_piles(piles):
    """ show ur workings """
    for p, pile in enumerate(piles):
        print("%2d: " %(p + 1), end='')
        tmp = pile[:]
        tmp.reverse()
        for c in tmp:
            print(c, end='')
        print()
    print()
            
def doit_p1():
    """ uing p1 restack """
    lno = 0
    f = open(inname, 'r')
    while True:
        l = f.readline()
        lno += 1
        l = l[:-1]
        if l.startswith(' 1'):
            break
        while len(l) % 4 != 0:
            l += ' '
        while len(piles) < len(l) // 4:
            piles.append([])
        for p in range(len(l) // 4):
            if l[4 * p + 1] != ' ':
                piles[p].append(l[4 * p + 1])
    print_piles(piles)
    f.readline()
    lno += 1
    while True:
        l = f.readline()
        if l == '':
            break
        lno += 1
        l = l[:-1]
        r = re.match(r'^move (\d+) from (\d+) to (\d+)', l)
        if r is None:
            print("Parse error for", l, "at", lno)
            sys.exit(1)
        (n, s, d) = r.groups()
        #print(l)
        restack_p1(int(n), int(s) - 1, int(d) -1, lno)
    print_piles(piles)
    print("Part 1: ", end='')
    for p in range(len(piles)):
        print(piles[p][0], end='')
    print()
        
def doit_p2():
    """ uing p1 restack """
    global piles
    piles = []
    lno = 0
    f = open(inname, 'r')
    while True:
        l = f.readline()
        lno += 1
        l = l[:-1]
        if l.startswith(' 1'):
            break
        while len(l) % 4 != 0:
            l += ' '
        while len(piles) < len(l) // 4:
            piles.append([])
        for p in range(len(l) // 4):
            if l[4 * p + 1] != ' ':
                piles[p].append(l[4 * p + 1])
    print_piles(piles)
    f.readline()
    lno += 1
    while True:
        l = f.readline()
        if l == '':
            break
        lno += 1
        l = l[:-1]
        r = re.match(r'^move (\d+) from (\d+) to (\d+)', l)
        if r is None:
            print("Parse error for", l, "at", lno)
            sys.exit(1)
        (n, s, d) = r.groups()
        #print(l)
        restack_p2(int(n), int(s) - 1, int(d) -1, lno)
        #
        print_piles(piles)
    print("Part 2: ", end='')
    for p in range(len(piles)):
        print(piles[p][0], end='')
    print()

def main():
    """doit 1 and doit 2 """
    doit_p1()
    doit_p2()
    
main()
