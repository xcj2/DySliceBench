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

    n = int(lines[0])
    aa = [int(e) for e in lines[1].split(' ')]

    return (n, aa)


def solve(n, aa):

    cnt = 0
    for i in range(1, n+1):
        if i % 2 == 1 and aa[i-1] % 2 == 1:
            cnt = cnt + 1
            
    
    return cnt


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
	