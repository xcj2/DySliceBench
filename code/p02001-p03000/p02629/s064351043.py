# -*- coding: utf-8 -*-

import sys
import math
from decimal import Decimal, ROUND_DOWN


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

    (n, ) = [int(e) for e in lines[0].split(' ')]

    return (n, )


def solve(n):

    def s(n):
        return (int(26 ** n) - 1) * 26 // 25

    d = 0
    for i in range(1, 100): 
        if s(i-1) + 1 <= n and n <= s(i):
            d = i
            break

    m = n - s(d- 1) - 1
    ks = []
    while True:
        k = m // 26
        r = m % 26
        ks.append(r)
        if k == 0:
            break
        m = k

    ks.reverse()

    names = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for k in ks:
        result.append(names[k])

    pad_size = d - len(result)
    result = ["a"] * pad_size + result

    return ''.join(result)
    


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
	