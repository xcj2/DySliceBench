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

    (a, b, c) = [int(e) for e in lines[0].split(' ')]

    return (a, b, c)


def solve(a, b, c):
    
    result = 'No'
    if a == b and a != c:
        result = 'Yes'
    if b == c and b != a:
        result = 'Yes'
    if c == a and c != b:
        result = 'Yes'
        
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
	