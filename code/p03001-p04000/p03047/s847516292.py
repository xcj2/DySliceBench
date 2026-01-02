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
    k = int(token[1])

    return (n, k)


def solve(n, k):


    return n - k + 1


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
	