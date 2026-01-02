# -*- coding: utf-8 -*-

import sys
import math


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

def parse_input(lines_as_string = None):

    global debug
    lines = []
    if lines_as_string is None:
        debug = False
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
    
    (k, ) = [int(e) for e in lines[0].split(" ")]

    return (k, )


def solve(k):

    result = 0
    mem = dict()
    for a in range(1, k+1):
        for b in range(1, k+1):
            for c in range(1, k+1):
                if (b, c) in mem:
                    d = mem[(b, c)] 
                else:
                    d = gcd(b, c)
                    mem[(b, c)] = d

                if (a, d) in mem:
                    e = mem[(a, d)] 
                else:
                    e = gcd(a, d)
                    mem[(a, d)] = e

                result = result + e
    
     
    return  result


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