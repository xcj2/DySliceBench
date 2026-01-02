# -*- coding: utf-8 -*-

import sys
import math
from decimal import Decimal, ROUND_DOWN


debug = False

def log(text):
    if debug:
        print(text)

def parse_input(lines_as_string = None):

    global debug
    lines = []
    if lines_as_string is None:
        debug = False
        # for line in sys.stdin:
        #     lines.append(line)
        lines.append(input())
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    (x, n) = [int(e) for e in lines[0].split(' ')]
    if n >= 1:
        p = [int(e) for e in lines[1].split(' ')]
    else:
        p = []

    return (x, n, p)


def solve(x, n, p):
    
    pp = set(p)
    result = None
    for i in range(0, 99):
        xa = x - i
        xb = x + i

        if xa in pp:
            pass
        else:
            result = xa
            break

        if xb in pp:
            pass
        else:
            result = xb
            break


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
	