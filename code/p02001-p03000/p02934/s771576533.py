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

    token = lines[0].split(" ")
    n = int(token[0])

    a = [int(e) for e in lines[1].split(" ")]

    return (n, a)


def solve(n, a):

    total = 0
    for i in range(n):
        total = total + (1/a[i])

    result = 1 / total

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
	