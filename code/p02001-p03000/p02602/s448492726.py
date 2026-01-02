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


    (n, k) = [int(e) for e in lines[0].split(" ")]
    a = [int(e) for e in lines[1].split(" ")]

    return (n, k, a)


def solve(n, k, a):

    # previous = 1
    # for i in range(k):
    #     previous = previous * a[i]

    
    result = []
    for i in range(k, n):

        if a[i-k] < a[i]:
            result.append('Yes')
        else:
            result.append('No')


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
	
