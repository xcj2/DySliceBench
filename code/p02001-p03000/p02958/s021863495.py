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
        token = lines[0].split()
        n = int(token[0])
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        token = lines[0].split()
        n = int(token[0])

    a = [int(i) for i in lines[1].split(" ")]

    return (n, a)


def solve(n, a):

    b = a.copy()
    b.sort()

    if a == b:
        return "YES"

    result = "NO"
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                c = a.copy()
                c[i], c[j] = c[j], c[i]
                if b == c:
                    result = "YES"
                    break

    return result


def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
	