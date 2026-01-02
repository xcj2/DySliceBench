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
    
    (k, n) = [int(e) for e in lines[0].split(" ")]
    a = [int(e) for e in lines[1].split(" ")]

    return (k, n, a)


def solve(k, n, a):


    result = k+1
    for i in range(n):
        
        if a[i-1] < a[i]:
            right_dist = k - a[i] + a[i-1]
        else:
            right_dist = a[i-1] - a[i]
        
        if debug:
            log("%d, %d, %d" % (i, n, (i+1) % n))
        if a[i] < a[(i+1) % n]:
            left_dist = a[i] + k - a[(i+1) % n]
        else:
            left_dist = a[i] - a[(i+1) % n]
        
        result = min([result, right_dist, left_dist])
    
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