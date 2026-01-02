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
    ws = [int(w) for w in lines[1].split(" ")]

    return (n, ws)


def solve(n, ws):

    result = None
    for i in range(1, n):
        a = sum(ws[:i])
        b = sum(ws[i:])
        diff = abs(a - b)
        if result:
            result = min(result, diff)
        else:
            result = diff

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))

#    solve(*parse_input())

if __name__ == '__main__':

    main()
