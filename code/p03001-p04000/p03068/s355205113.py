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
    s = lines[1]
    k = int(lines[2])

    return (n, s, k)


def solve(n, s, k):


    c = s[k-1]

    result = []
    for d in s:
        if c == d:
            result.append(c)
        else:
            result.append("*")

    return "".join(result)


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
