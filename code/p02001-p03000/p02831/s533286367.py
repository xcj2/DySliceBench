# -*- coding: utf-8 -*-

import sys
import math
import itertools

debug = False

def log(text):
    if debug:
        print(text)


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

def lcm(a, b):
    g = gcd(a, b)
    return (a * b) // g


def parse_input(lines_as_string = None):

    global debug
    lines = []
    if lines_as_string is None:
        debug = False
        # error?
        # for line in sys.stdin:
        #     lines.append(line)
        lines.append(input())

    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    

    (a, b) = [int(e) for e in lines[0].split(" ")]

    return (a, b)


def solve(a, b):

    
    return lcm(a, b)


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
