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

    (n, ) = [int(e) for e in lines[0].split(' ')]
    a = [int(e) for e in lines[1].split(' ')]

    return (n, a)


def solve(n, a):
    
    m = int(10 ** 18)
    a.sort()
    result = 1
    for i in range(n):
        result = result * a[i]
        if result > m:
            result = -1
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
	