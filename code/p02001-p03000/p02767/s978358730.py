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
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
    
    n = int(lines[0])
    x = [int(e) for e in lines[1].split(" ")]

    return (n, x)


def solve(n, x):


    result = float('inf')
    for p in range(1, 101):
        tmp = int(sum([(e - p)**2 for e in x]))
        if tmp < result:
            result = tmp

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