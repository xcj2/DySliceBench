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
        # for line in sys.stdin:
        #     lines.append(line)
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

   
    (a, b, c, k) = [int(e) for e in lines[0].split(' ')]

    return (a, b, c, k)


def solve(a, b, c, k):
    
    result = None
    if a >= k:
        result = 1 * k
    elif a + b >= k:
        result = 1 * a
    elif a + b + c >= k:
        result = 1 * a + 0 * b - 1 * (k - (a + b))
    else:
        result = 1 * a + 0 * b - 1 * c

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