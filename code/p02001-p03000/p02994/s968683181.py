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

    tokens = lines[0].split(" ")
    n = int(tokens[0])
    l = int(tokens[1])

    return (n, l)


def solve(n, l):

    min_abs = abs(l)
    removed = l
    sum = 0
    for i in range(l, l+n):
        sum = sum + i
        if abs(i) < min_abs:
            min_abs = abs(i)
            removed = i

    return sum - removed


def main():
    # 出力

    print("%s" % solve(*parse_input()))

#    solve(*parse_input())

if __name__ == '__main__':

    main()
