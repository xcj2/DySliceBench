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

    (h, w) = [int(e) for e in lines[0].split(" ")]

    return (h, w)


def solve(h, w):

    if h == 1 or w == 1:
        return 1

    cell = h * w
    tmp = cell // 2
    result = None
    if cell % 2 == 0:
        result = tmp
    else:
        result = tmp + 1
        

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