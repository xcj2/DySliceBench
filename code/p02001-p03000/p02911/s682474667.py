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
        tokens = lines[0].split(" ")
        n = int(tokens[0])
        k = int(tokens[1])
        q = int(tokens[2])
        for i in range(q):
            lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        tokens = lines[0].split(" ")
        n = int(tokens[0])
        k = int(tokens[1])
        q = int(tokens[2])

    a = []
    for i in range(q):
        a.append(int(lines[i+1]))

    return (n, k, q, a)


def solve(n, k, q, a):

    win = []
    for i in range(n):
        win.append(0)

    for i in range(q):
        win[a[i]-1] = win[a[i]-1] + 1

    result = []
    for i in range(n):

        if k - (q - win[i]) > 0:
            result.append("Yes")
        else:
            result.append("No")

    return result


def main():
    # 出力
    result = solve(*parse_input())
    if isinstance(result, list):
        for r in result:
            print("%s" % r)
    else:
        print("%s" % result)


if __name__ == '__main__':

    main()
	
