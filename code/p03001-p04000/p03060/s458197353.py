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
        lines.append(input())

    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    n = int(lines[0])
    v = [int(e) for e in lines[1].split(" ")]
    c = [int(e) for e in lines[2].split(" ")]

    return (n, v, c)


def solve(n, v, c):

    result = 0
    for i in range(n):
        d = v[i] - c[i]
        if d > 0:
            result = result + d

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
