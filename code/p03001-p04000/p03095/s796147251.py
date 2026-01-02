# -*- coding: utf-8 -*-

import sys

def parse_input(lines_as_string = None):


    lines = []
    if lines_as_string is None:
        lines.append(input())
        lines.append(input())
    else:
        lines = [e for e in lines_as_string.split("\n")][1:-1]
 
    tokens = lines[0].split(" ")
    n = int(tokens[0])
    tokens = lines[1].split(" ")
    s = tokens[0]

    return (n, s)


def solve(n, s):

    d = dict([(c, 0) for c in "abcdefghijklmnopqrstuvwxyz"])

    for c in s:
        d[c] = d[c] + 1

    count = 1
    for v in [v for v in d.values() if v > 0]:
        count = count * (v+1)
    

    return (count - 1) %(10**9+7)

def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
