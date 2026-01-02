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
    k = int(token[0])
    x = int(token[1])

    return (k, x)


def solve(k, x):


    start = max(-1000000, x - (k-1))
    end = min(1000000, x + (k-1))

    result = " ".join([str(i) for i in range(start, end + 1)])
        

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
	