# -*- coding: utf-8 -*-

import sys
import math

def parse_input(lines_as_string = None):

    lines = []
    if lines_as_string is None:
        for line in sys.stdin:
            lines.append(line)
    else:
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    # 出力
    nm = lines[0].split(" ")
    n = int(nm[0])
    m = int(nm[1])

    rows = []
    for i in range(1, n+1):
        rows.append([int(e) for e in lines[i].split(" ")])

    return (n, m, rows)

def solve(n, m, rows):

    result = []
    for k in range(1, m + 1):
        tmp = []
        for i in range(0, n):
#            print(rows[i])
            r = rows[i]
#            print(r[1:r[0] + 1])
            if k in r[1:r[0]+1]:
               tmp.append(i+1)
        if len(tmp) == n:
            result.append(k)

    return len(result)

def main():

    print("%d" % solve(*parse_input()))

if __name__ == '__main__':

    main()
