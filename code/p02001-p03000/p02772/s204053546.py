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

    n = int(lines[0])
    a = [int(e) for e in lines[1].split(" ")]

    return (n, a)


def solve(n, a):

    even = [e for e in a if e % 2 == 0]    

    result = 'APPROVED'
    for i in range(len(even)):
        e = even[i]
        if e % 3 == 0:
            pass 
        elif e % 5 == 0:
            pass
        else:
            result = 'DENIED'
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