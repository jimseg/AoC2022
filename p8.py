#!/usr/bin/env python3

""" forests """

import re
import sys

#from collections import defaultdict

# if any cli args, assume there's a fie test.txt (used ith the example inputs

if len(sys.argv) == 1:
    inname = "input%s.txt" % (re.sub(r'\D*(\d+).*', r'\1', sys.argv[0]))
else:
    inname = "test%s.txt" % (re.sub(r'\D*(\d+).*', r'\1', sys.argv[0]))

trees = []

def row(l):
    """ fill in l->r and r->l values """
    l = list(l.strip())
    new_row = []
    h = int(l[0])
    new_row.append([h, True])
    max_h = h
    for col in range(1, len(l)):
        h = int(l[col])
        new_row.append([h, h > max_h])
        max_h = max(h, max_h)
    h = int(l[len(l) - 1])
    max_h = h
    new_row[len(l) -1] = [h, True]
    for col in range(len(l) - 2, 0, -1):
        h = int(l[col])
        if h > max_h:
            new_row[col] = [h, True]
        max_h = max(h, max_h)
    trees.append(new_row)

def count():
    """ count no of True entries """
    #for _r, row in enumerate(trees):
    #    print(row)
    visible = 0
    for _r, row in enumerate(trees):
        for _c, arr in enumerate(row):
            if arr[1]:
                visible += 1
    return visible
        
def column(idx):
    """ fill in a column """
    h = trees[0][idx][0]
    max_h = h
    trees[0][idx] = [h, True]
    for r in range(1, len(trees) - 1):
        h = trees[r][idx][0]
        if h > max_h:
            trees[r][idx] = [h, True]
        max_h = max(h, max_h)
    h = trees[len(trees) - 1][idx][0]
    trees[len(trees) - 1][idx] = [h, True]
    max_h = h
    for r in range(len(trees) - 2, 0, -1):
        h = trees[r][idx][0]
        if h > max_h:
            trees[r][idx] = [h, True]
        max_h = max(h, max_h)

hites = []
views = []

def fillr(l):
    """ create array """
    l = list(l.strip())
    r = []
    for _c, h in enumerate(l):
        r.append(int(h))
    hites.append(r)
    
def get_views():
    """ get views """
    max_view = 0
    for i in range(len(hites)):
        views.append([1 for x in range(len(hites[0]))])
        views[i][0] = 0
        views[i][len(views[0]) -1] = 0
        hites[i][0] = 9
        hites[i][len(hites[0]) -1] = 9
    views[0] = [0 for i in range(len(hites[0]))]
    views[len(hites) - 1] = [0 for i in range(len(hites))]
    hites[0] = [9 for i in range(len(hites[0]))]
    hites[len(hites) - 1] = [9 for i in range(len(hites[0]))]
    
    print("\nhites")
    for _n, row in enumerate(hites):
        print(row)
    print("\nviews")
    for _n, row in enumerate(views):
        print(row)
                
    for r, row in enumerate(hites):
        if row in (0, len(hites) - 1):
            continue
        for c, h in enumerate(row):
            if c in (0, len(row) - 1):
                continue
            rl = 0
            for i in range(c - 1, -1, -1):
                rl += 1
                if h <= hites[r][i]:
                    break
            views[r][c] = rl
            lr = 0
            for i in range(c + 1, len(hites[0])):
                lr +=1
                if h <=  hites[r][i]:
                    break
            views[r][c] *= lr
   
    # now do verticals
    for c in range(1, len(hites[0]) - 2):
        for r in range(len(hites)):
            h = hites[r][c]
            tb = 0
            for i in range(r - 1, -1, -1):
                tb += 1
                if h <= hites[i][c]:
                    break
            views[r][c] *= tb
            bt = 0
            for i in range(r + 1, len(hites)):
                bt += 1
                if h <= hites[i][c]:
                    break
            views[r][c] *= bt
            max_view = max(max_view, views[r][c])
        #print("\nafter vertical:", c)
        #for _n, row in enumerate(hites):
        #    print(row)
        #print("\nviews")
        #for _n, row in enumerate(views):
        #    print(row)
                

    print("Part 2:", max_view)
    
def main():
    """ go exploring """
    for l in open(inname, 'r').readlines():
        row(l)
    for col in range(len(trees[0])):
        column(col)
    print("Part 1:", count())

    for l in open(inname, 'r').readlines():
        fillr(l)
    get_views()
    
main()
