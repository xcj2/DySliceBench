# -*- coding: utf-8 -*-

import sys

def parse_input(lines_as_string = None):


    lines = []
    if lines_as_string is None:
        lines.append(input())
        tokens = lines[0].split(" ")
        n = tokens[0]
        lines.append(input())
    else:
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        tokens = lines[0].split(" ")
        n = tokens[0]

    s = lines[1]


    return (n, s)


def solve(n, s):



    sum_r = len([1 for c in s if c == "R"])

    result = "No"
    if sum_r > int(n) - sum_r:
        result = "Yes"

    return result

def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
