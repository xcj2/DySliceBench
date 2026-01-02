# -*- coding: utf-8 -*-

import sys

def parse_input(lines_as_string = None):

    lines = []
    if lines_as_string is None:
        lines.append(input())
        tokens = lines[0].split(" ")
        n = int(tokens[0])
        m = int(tokens[1])
        for i in range(n):
            lines.append(input())
    else:
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        print("lines=%s" % lines)
        tokens = lines[0].split(" ")
        n = int(tokens[0])
        m = int(tokens[1])

    a = []
    b = []
    for i in range(n):
        tokens = lines[i+1].split(" ")
        a.append(int(tokens[0]))
        b.append(int(tokens[1]))

    return (n, m, a, b)

def solve(n, m, a, b):

    
    s_a = sorted([(i, e) for i, e in enumerate(a)], key=lambda e: e[1])
#    print("s_a=%s" % s_a)

    current = m
    total = 0
    tmp = 0
    for i, e in s_a:
        if current > b[i]:
            tmp = e * b[i]
            current = current - b[i]
        else:
            tmp = e * current
            current = 0

        total = total + tmp

#        print("i=%d, total=%d" % (i, total))
        if current == 0:
            break

    return total

def main():

    print("%d" % solve(*parse_input()))

if __name__ == '__main__':

    main()
