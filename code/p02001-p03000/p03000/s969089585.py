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

    tokens = lines[0].split(" ")
    n = int(tokens[0])
    x = int(tokens[1])
    ls = [int(l) for l in lines[1].split(" ")]

    return (n, x, ls)


def solve(n, x, ls):

    d = 0
    count = 1
    for i in range(0, n):
        d = d + ls[i]
        if d <= x:
            count = count + 1
        else:
            break


    return count


def main():
    # 出力

    print("%s" % solve(*parse_input()))

#    solve(*parse_input())

if __name__ == '__main__':

    main()
