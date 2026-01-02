# -*- coding: utf-8 -*-

import sys

debug = False

def log(text):
    if debug:
        print(text)

def parse_input(lines_as_string = None):

    global debug
    lines = []
    if lines_as_string is None:
        debug = False
#        for line in sys.stdin:
#            lines.append(line)
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    n = [int(e) for e in lines[0].split(" ")][0]

    return (n,)


def solve(n,):


    a = 0
    b = 0
    c = int(pow(n, 0.5))
    if debug:
        log("c=%s" % c)
    for i in range(c, 0, -1):   

        if n % i == 0:
            a = i
            b = n // i
            if debug:
                log("a=%s" % a)
                log("b=%s" % b)
            break


    return  a - 1 + b - 1


def main():
    # 出力
    result = solve(*parse_input())
    if isinstance(result, list):
        for r in result:
            print("%s" % r, end=' ')
    else:
        print("%s" % result)

if __name__ == '__main__':

    main()
	