# -*- coding: utf-8 -*-

import sys

def parse_input(lines_as_string = None):


    lines = []
    if lines_as_string is None:
        lines.append(input())
        tokens = lines[0].split(" ")
        n = int(tokens[0])
        m = int(tokens[1])
        c = int(tokens[2])
        lines.append(input())
        for i in range(n):
            lines.append(input())

    else:
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        tokens = lines[0].split(" ")
        n = int(tokens[0])
        m = int(tokens[1])
        c = int(tokens[2])

    b = [int(e) for e in lines[1].split(" ")]
    
    a = []
    for i in range(n):
        a.append([int(e) for e in lines[i+2].split(" ")])

    return (n, m, c, b, a)


def solve(n, m, c, b, a):

    count = 0
    for i in range(n):
        ans = 0
        for j in range(m):
            ans =  ans + a[i][j]*b[j]
        ans = ans + c
        if ans > 0:
            count = count + 1

    return count

def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
