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

    n = int(lines[0])
    h = [int(e) for e in lines[1].split(" ")]

    return (n, h)


def solve(n, h):

    if n == 1:
        return 0

    count = 0
    count_max = 0
    for i in range(n-1, 0, -1):
        
        if h[i-1] >= h[i]:
            count = count + 1
        else:
            count = 0

        count_max = max(count_max, count)
        if debug:
            log("i=%d, count=%d" % (i, count))


    return count_max


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
	
