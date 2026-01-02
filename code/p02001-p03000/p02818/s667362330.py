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

    (a, b, k) = [int(e) for e in lines[0].split(" ")]

    return (a, b, k)


def solve(a, b, k):

    a2 = a
    b2 = b
    if a >= k:
        a2 = a - k
        b2 = b
    else:
        a2 = 0
        b2 = max([b - (k - a), 0])

    return [a2, b2]


def main():
    # 出力
    result = solve(*parse_input())
    if isinstance(result, list):
        print("%d %d" % (result[0], result[1]))
    else:
        print("%s" % result, sep='')

if __name__ == '__main__':

    main()
	
