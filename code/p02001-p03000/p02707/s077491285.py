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
        lines.append(input())
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
    
    (n, ) = [int(e) for e in lines[0].split(" ")]
    a = [int(e) for e in lines[1].split(" ")]

    return (n, a)


def solve(n, a):

    result = dict([(i, 0) for i in range(1, n+1)])

    for i in range(n-1):
        result[a[i]] = result[a[i]] + 1

    return  list(result.values())


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