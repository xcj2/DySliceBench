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
        for line in sys.stdin:
            lines.append(line.strip())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
    

    n = int(lines[0])
    a = [int(e) for e in lines[1].split(' ')]

    return (n, a)


def solve(n, a):

    b = []
    for i in range(1, n):
        b.append(a[i] - a[i-1])
    
    current_money = 1000
    current_stock = 0
    for i in range(0, n):
        if i < n - 1 and b[i] >= 0:
            if current_stock == 0:
                current_stock = current_money // a[i]
                current_money = current_money - current_stock * a[i]
        else:
            if current_stock > 0:
                current_money = current_money + current_stock * a[i]
                current_stock = 0

        if debug:
            log("i=%d, current_money=%d, current_stock=%d" % (i, current_money, current_stock))

    if current_stock > 0:
        current_money = current_money + current_stock * a[n-1]


    return current_money

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
