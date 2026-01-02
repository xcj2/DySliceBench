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

    (x, k, d) = [int(e) for e in lines[0].split(' ')]


    return (x, k, d)


def solve(x, k, d):

    y = abs(x)
    m =  y // d 

    if debug:
        log("x=%d, k=%d, d=%d, y=abs(x)=%d, m=%d" % (x, k, d, y, m))
    
    result = None
    if k <= m:
        result = y - k * d
    else:
        n = k - m
        if n % 2 == 0:
            result = y - m * d
        else:
            result = abs(y - m * d - d)
             

    return result
    


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
	
