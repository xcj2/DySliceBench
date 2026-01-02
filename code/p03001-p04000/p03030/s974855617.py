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
        n = int(lines[0])
        for i in range(n):
            lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        n = int(lines[0])

    sp = []
    for i in range(1, n+1):
        token = lines[i].split()
        s = token[0]
        p = int(token[1])
        sp.append((s, p, i))

    return (n, sp)


def solve(n, sp):

    sp2 = [(e[0], -e[1], e[2]) for e in sp]
    sp2.sort()
    for e in sp2:
        print(e[2])


def main():
    # 出力

#    print("%s" % solve(*parse_input()))

    solve(*parse_input())

if __name__ == '__main__':

    main()
