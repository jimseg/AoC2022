#!/usr/bin/env python3

""" du utiity """

import re
import sys

#from collections import defaultdict

# if any cli args, assume there's a fie test.txt (used ith the example inputs

if len(sys.argv) == 1:
    inname = "input%s.txt" % (re.sub(r'\D*(\d+).*', r'\1', sys.argv[0]))
else:
    inname = "test.txt"

Dir_map = {}
cwd = ''
cur_dir = None
num_dirs = 0

class Dir:
    """ track directories and their sizes """
    def __init__(self, name, depth):
        self.name =  name
        self.files = 0
        self.subdirs = set()
        self.done = False
        self.depth = depth
        Dir_map[self.name] = self
    def clear(self):
        """# in case ls is done on a directory we've already done """
        self.files = 0
        self.subdirs = set()
        self.done = False
    def display(self, indent = ""):
        """ for debugging """
        print(indent, self.name, "total: ", self.files, "depth:", self.depth)

def main():
    """ go exploring """
    global cwd, Dir_map, cur_dir, num_dirs
    cwd = ""
    lno = 0
    depth = 0
    cur_dir = Dir('', 0)
    for l in open(inname, 'r').readlines():
        lno += 1
        l = l.strip()
        #print(cwd,cur_dir.name, l)
        if l.startswith('$ ls'):
            if cur_dir is None:
                print("Can't list a directory when we don't know where we are on", lno)
                sys.exit(1)
            # in case we've already done a '$ ls'  of this one
            cur_dir.clear()
            continue
        r = re.match(r'\$ cd (.*)', l)
        if r is not None:
            tgt = r.groups()[0]
            if tgt == '..':
                depth -= 1
                cwd = re.sub(r'[^/]*/$', '', cwd)
                # for those who try to cd .. from /
                if cwd == '':
                    cwd = '/'
                    depth = 0
                cur_dir = Dir_map[cwd]
                if cur_dir is None:
                    print("cd'ed off the edge of the universe")
                    sys.exit(1)
                continue
            # cd to a target dir
            depth += 1
            cwd += '%s/' % tgt
            if cwd == '//':
                cwd = '/'
            if Dir_map.get(cwd, None) is None:
                cur_dir = Dir(cwd, depth)
                num_dirs += 1
            continue
        # ls output line
        r = re.match(r'(\S+)\s+(.*)', l)
        left, right = r.groups()
        if left == 'dir':
            tgt = cwd + "%s/" % right
            cur_dir.subdirs.add(tgt)
        else:
            cur_dir.files += int(left)

    ordering = [ (Dir_map[d], Dir_map[d].depth, Dir_map[d].done, Dir_map[d].name)
                    for d in Dir_map.keys()]
    #print()
    #print("Dir_map:")
    #for d in Dir_map:
    #    Dir_map[d].display()
    #print()
    #print("\nOrdering pre-sort")
    #print(ordering)
    ordering = sorted(ordering , key = lambda x: x[1], reverse=True)
    #print("\nOrdering post-sort")
    #print(ordering)
    #print()
    
    for tpl in ordering:
        d = tpl[0]
        #d.display()
        for sd in d.subdirs:
            subd = Dir_map[sd]
            #subd.display("   ")
            if not subd.done:
                print(sd.name, "never resolved")
                sys.exit(1)
            d.files += subd.files
        d.done = True
    small = 0    
    for k in Dir_map:
        d = Dir_map[k]
        if d.name == '':
            continue
        if d.files <= 100000:
            small += d.files
            d.display('==>  ')
        else:
            d.display('     ')
    print("Part 1:", small)
    # sort directories by size, ascending
    ordering = [(Dir_map[d], Dir_map[d].files) for d in Dir_map.keys()]
    ordering = sorted(ordering, key = lambda x: x[1])
    empty = 70000000
    need  = 30000000
    
    must_free = need - (empty - Dir_map['/'].files )
    print("must free:", must_free)
    for tpl in ordering:
        if tpl[1] >= must_free:
            d = tpl[0]
            print(tpl[1], tpl[0].name)
            
            
main()
