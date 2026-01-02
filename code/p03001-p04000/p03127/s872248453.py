# -*- coding: utf-8 -*-

import sys

def gcd(a, b):

    c = min(a, b)
    d = max(a, b)
    r = 0    
    while True:
        r = d % c
        if r == 0:
            break
        d = c
        c = r

    return c

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

    rows = []
    for i in range(1, 2):
        rows.append([int(e) for e in lines[i].split(" ")])

    return (n, rows[0])

def solve(n, monsters):

    g = monsters[0]
    for i in range(1, n):
        g = gcd(g, monsters[i])


    return g

def main():

    print("%d" % solve(*parse_input()))

if __name__ == '__main__':

    main()
