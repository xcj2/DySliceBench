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
        lines.append(input())
        lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    n = int(lines[0])
    b = [int(e) for e in lines[1].split(" ")]

    return (n, b)


def solve(n, b):

    a = []
    a.append(b[0])
    for i in range(1, n-1):
        a.append(min(b[i-1], b[i]))

    a.append(b[n-2])

    return sum(a)


def main():
    # 出力
    result = solve(*parse_input())
    if isinstance(result, list):
        for r in result:
            print("%s" % r)
    else:
        print("%s" % result)


if __name__ == '__main__':

    main()
	
