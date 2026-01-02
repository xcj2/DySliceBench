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

    (x, ) = [int(e) for e in lines[0].split(' ')]

    return (x, )


def solve(x):
    
    # 切り捨てが必要
    m = (math.log10(x) - 2) / math.log10(1.01)
    n = math.ceil(m) 

    tmp = 100
    n = 0 
    for i in range(1, 3761):
        tmp = math.floor(tmp * 1.01)
        if tmp >= x:
            n = i
            break


    return n
    


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