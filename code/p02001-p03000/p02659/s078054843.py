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

    tokens = lines[0].split(' ')
    a = tokens[0]
    b = tokens[1]

    return (a, b)


def solve(a0, b0):

    a = int(a0)    
    b = float(b0)
#    c =  math.floor(a * (b * 1000) // 1000)

#    b2 = int(math.floor(b * 100))
#    c = math.floor((a * b2) // 100)

    a =  Decimal(a0)
    b =  Decimal(b0)
    
    ab = a * b
    c = int(ab.quantize(Decimal('1.'), rounding=ROUND_DOWN))
    
    if debug:
        print(c)

    return c
    


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
	