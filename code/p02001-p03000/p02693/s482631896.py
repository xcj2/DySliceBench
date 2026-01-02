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

    (k, ) = [int(e) for e in lines[0].split(' ')]
    (a, b) = [int(e) for e in lines[1].split(' ')]

    return (k, a, b)


def solve(k, a, b):

    result = 'NG'
    for i in range (1, 1001):
        if a <= k * i and k * i <= b:
            result = 'OK'
            break
    
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
	