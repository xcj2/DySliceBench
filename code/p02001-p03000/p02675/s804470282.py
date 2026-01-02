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

    m = str(n)
    l = m[-1]
    result = None
    if l in ('2', '4', '5', '7', '9'):
        result = 'hon'
    elif l in ('0', '1', '6', '8'):
        result  = 'pon'
    elif l in ('3'):
        result = 'bon'
    
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
	