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

    n = [int(e) for e in lines[0].split(" ")][0]
    d = [int(e) for e in lines[1].split(" ")]

    return (n, d)


def solve(n, d):

    if d[0] != 0:
        return 0 
     
    d.sort()

    z = [] 
    tmp = d[0]
    count = 0
    for i in range(n):
        if tmp != d[i]:
            z.append((tmp, count))
            tmp = d[i]
            count = 1
        else:
            count = count + 1
    z.append((tmp, count))

    if z[0][0] != 0 or z[0][1] > 1:
        return 0

    result = 1
    m = len(z)
    for i in range(1, m):
        if z[i-1][0] + 1 != z[i][0]:
            result = 0
            break
        else:
            result = result * z[i-1][1] ** z[i][1]
    
    res = result % 998244353

    return res


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