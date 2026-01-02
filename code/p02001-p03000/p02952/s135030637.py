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
    n = int(token[0])

    return (n, )


def solve(n):

    count = 0
    for i in range(1, n+1):

        if 1 <= i and i <= 9:
            count = count + 1

        if 100 <= i and i <= 999:
            count = count + 1

        if 10000 <= i and i <= 99999:
            count = count + 1

    return count


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
	