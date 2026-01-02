# -*- coding: utf-8 -*-

##
## C - Vacation
## https://atcoder.jp/contests/dp/tasks/dp_c
##

import sys

def solve(N, tuples):
    xa, xb, xc = 0, 0, 0
    for a, b, c in tuples:
        ya = max(xb, xc) + a
        yb = max(xc, xa) + b
        yc = max(xa, xb) + c
        xa, xb, xc = ya, yb, yc
    return max(xa, xb, xc)

def load(input):
    line = input.readline()
    N = int(line.strip())
    tuples = [ tuple( int(s) for s in line.split() )
                   for line in input ]
    return N, tuples

def main():
    N, tuples = load(sys.stdin)
    result = solve(N, tuples)
    print(result)

main()
