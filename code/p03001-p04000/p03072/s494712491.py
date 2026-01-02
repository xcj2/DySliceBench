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

    if debug:
        log("n=%s" % n)
        log("h=%s" % h)
    
    result = 1
    for i in range(1, n):
        count = 0
        for j in range(i):
            if h[j] <= h[i]:
                count = count + 1
            else:
                break
        if count == i:
            result = result + 1
        

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
