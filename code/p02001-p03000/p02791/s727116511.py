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
    p = [int(e) for e in lines[1].split(' ')]

    return (n, p)


def solve(n, p):


    result = [] 
    current_min = 200000 + 1
    current_min_index = None
    for i in range(n):

        if current_min < p[i]:
            pass
        else:
           current_min = p[i]
           current_min_index = i

        done = False
        for j in range(current_min_index, i+1):
            if p[i] <= p[j]:
                if j == i:
                    done = True
            else:
                break
        if done:
            result.append(i)


    return len(result)


def main():
    # 出力
    result = solve(*parse_input())
    if isinstance(result, list):
        print("%d %d" % (result[0], result[1]))
    else:
        print("%s" % result, sep='')

if __name__ == '__main__':

    main()