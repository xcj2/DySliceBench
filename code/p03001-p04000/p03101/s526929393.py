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
    width = int(tokens[0])
    height = int(tokens[1])
    tokens = lines[1].split(" ")
    w = int(tokens[0])
    h = int(tokens[1])

    return (width, height, w, h)


def solve(width, height, w, h):


    return (width - w) * (height - h)

def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
