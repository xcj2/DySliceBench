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
        (n, k) = [int(e) for e in lines[0].split(' ')]
        for i in range(2*k):
            lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        (n, k) = [int(e) for e in lines[0].split(' ')]

    d = [] 
    a = []
    for i in range(1, 2*k+1):
        if i % 2 == 1:
           d.append(int(lines[i]))
        else:
           a.append([int(e) for e in lines[i].split(' ')])

    return (n, k, d, a)


def solve(n, k, d, a):


    candy_a = set() 
    for i in range(k):
        for e in a[i]:
            candy_a.add(e)

    result = n - len(candy_a)

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