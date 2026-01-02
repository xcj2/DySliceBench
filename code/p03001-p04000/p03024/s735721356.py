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

    return (s, )


def solve(s, ):

    win = s.count("o")
    lose = s.count("x")
    
    result = "NO"
    if 15 - lose >= 8:
        result = "YES"

    return result

def main():
    # 出力

    print("%s" % solve(*parse_input()))


if __name__ == '__main__':

    main()
