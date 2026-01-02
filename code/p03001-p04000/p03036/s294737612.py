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

    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    token = lines[0].split()
    r = int(token[0])
    d = int(token[1])
    x = int(token[2])

    return (r, d, x)


def solve(r, d, x):

    y = x
    result = 0
    for i in range(10):
        y = r*y - d
        print(y)

    return result


def main():
    # 出力

#    print("%s" % solve(*parse_input()))

    solve(*parse_input())

if __name__ == '__main__':

    main()
