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
    
    (a, b) = [int(e) for e in lines[0].split(" ")]

    return (a, b)


def solve(a, b):

   
    x1f = math.floor(a / 0.08)
    x1c = math.ceil(a / 0.08)
    x2f = math.floor(b / 0.1)
    x2c = math.ceil(b / 0.1)

    both = []
    if math.floor(x1f * 0.08) == a and math.floor(x1f * 0.1) == b:
        both.append(x1f)

    if math.floor(x1c * 0.08) == a and math.floor(x1c * 0.1) == b:
        both.append(x1c)

    if math.floor(x2f * 0.08) == a and math.floor(x2f * 0.1) == b:
        both.append(x2f)

    if math.floor(x2c * 0.08) == a and math.floor(x2c * 0.1) == b:
        both.append(x2c)


    result = -1
    if len(both):
        result = min(both)
    

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