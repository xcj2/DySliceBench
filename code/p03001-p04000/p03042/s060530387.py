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

    s = lines[0]

    return (s,)


def solve(s):

    a = int(s[:2])
    b = int(s[2:])

    def mm(x):
        return 1 <= x and x <= 12

    def yy(x):
        return 0 <= x and x <= 99

    result = "NA"
    if mm(a) and mm(b):
        result = "AMBIGUOUS"
    elif mm(a) and yy(b):
        result = "MMYY"
    elif yy(a) and mm(b):
        result = "YYMM"

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
