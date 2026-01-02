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
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    (s, t) = [e for e in lines[0].split(" ")]
    (a, b) = [int(e) for e in lines[1].split(" ")]
    u = lines[2]

    return (s, t, a, b, u)


def solve(s, t, a, b, u):
    
    a2 = a
    b2 = b
    if s == u:
        a2 = a2 - 1
    elif t == u:
        b2 = b2 - 1
    
    result = ' '.join([str(a2), str(b2)])

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
	