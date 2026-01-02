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

    n = int(lines[0])

    return (n, )


def solve(n):


    x = n / 1.08

    a = int(math.floor(math.floor(x) * 1.08))
    b = int(math.floor(math.ceil(x) * 1.08))

    result = ':('
    if a == n:
        result = str(int(math.floor(x)))

    if b == n:
        result = str(int(math.ceil(x)))


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