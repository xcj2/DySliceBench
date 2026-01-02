# -*- coding: utf-8 -*-

import sys

def parse_input(lines_as_string = None):

    lines = []
    if lines_as_string is None:
        for line in sys.stdin:
            lines.append(line)
    else:
        lines = [e for e in lines_as_string.split("\n")][1:-1]

    params = lines[0].split(" ")
    a = int(params[0])
    b = int(params[1])

    return (a, b)


def solve(a, b):

    result = 0
    if b % a == 0:
        result = a + b
    else:
        result = b - a

    return result

def main():
    # 出力

    a, b = parse_input()
    print("%d" % solve(a, b))

if __name__ == '__main__':

    main()
