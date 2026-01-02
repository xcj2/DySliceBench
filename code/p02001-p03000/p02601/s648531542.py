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
        for line in sys.stdin:
            lines.append(line.strip())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    (a, b, c) = [int(e) for e in lines[0].split(" ")]
    k = int(lines[1])

    return (a, b, c, k)


def solve(a, b, c, k):

    a2 = a
    b2 = b
    c2 = c
    tmp = k
    while tmp > 0 and b2 <= a2:
        tmp = tmp - 1
        b2 = 2 * b2

    while tmp > 0 and c2 <= b2:
        tmp = tmp - 1
        c2 = 2 * c2

    if c2 > b2 and b2 > a2:
        result = 'Yes'
    else:
        result = 'No'
    
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
	