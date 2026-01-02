# -*- coding: utf-8 -*-

import sys
import math

debug = False

def log(text):
    if debug:
        print(text)

def parse_input(lines_as_string = None):

    global debug
    lines = []
    if lines_as_string is None:
        debug = False
#        for line in sys.stdin:
#            lines.append(line)
        lines.append(input())
        (h, w) = [int(e) for e in lines[0].split(" ")]
        for i in range(h):
            lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        (h, w) = [int(e) for e in lines[0].split(" ")]
    
    s = []
    for i in range(1, h + 1):
        s.append(lines[i])
        

    return (h, w, s)

def solve(h, w, s):


    result = -1
    for i in range(h):
        for j in range(w):

            if s[i][j] == "#":
                continue
            
            d = 0
            resolved = set() 
            last_resolved = set()
            last_resolved.add((i, j))
            for r in last_resolved:
                resolved.add(r)

            while True:
                neighbors_of_last_resolved = set()
                for (m, n) in last_resolved:

                    for (dm, dn) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

                        if m+dm < 0 or h - 1 < m+dm:
                            continue

                        if n+dn < 0 or w - 1 < n+dn:
                            continue
                        
                        if s[m+dm][n+dn] == "#":
                            continue
                        else:
                            r = (m+dm, n+dn)
                            if not r in resolved:
                                neighbors_of_last_resolved.add(r)
                
                last_resolved = neighbors_of_last_resolved
                for r in last_resolved:
                    resolved.add(r)

                if len(last_resolved) == 0:
                    break
                else:
                    d = d + 1

            if d > result:
                result = d

    return result

def main():
    # 出力
    result = solve(*parse_input())
    if isinstance(result, list):
        for r in result:
            print("%s" % r)
    else:
        print("%s" % result)

if __name__ == '__main__':

    main()
	