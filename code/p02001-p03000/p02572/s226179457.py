# -*- coding: utf-8 -*-

import sys
import math
from decimal import Decimal, ROUND_DOWN
from collections import deque
from itertools import combinations
import copy

debug = False

def log(text):
    if debug:
        print(text)

def parse_input(lines_as_string = None):

    global debug
    lines = []
    if lines_as_string is None:
        debug = False
        for line in sys.stdin:
            lines.append(line.strip())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    (n, ) = [int(e) for e in lines[0].split(' ')]
    a = [int(e) for e in lines[1].split(' ')]


    return (n, a)


def solve(n, a):

   
    total = 0
    m = int(10**9 + 7)
    s = sum(a)
    s_current = 0
    for i in range(n):
        s_current = s_current + a[i]
        total = (total + a[i] * (s - s_current)) % m

    total = total % m


    return total
    


def main():
    # 出力
    result = solve(*parse_input())
    if isinstance(result, list):
        for r in result:
            print("%s" % r, sep='')
    else:
        print("%s" % result, sep='')

if __name__ == '__main__':

    main()
	
