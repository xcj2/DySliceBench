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

    (x, y) = [int(e) for e in lines[0].split(' ')]

    return (x, y)


def solve(x, y):
    
    result = 'No'
    for c in range(0, 101):
        for t in range(0, 101):
            if c + t == x and 2 * c + 4 * t == y:
                result = 'Yes'
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
	