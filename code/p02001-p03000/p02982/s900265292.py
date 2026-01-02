# -*- coding: utf-8 -*-

import sys
import math

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
        d = int(tokens[1])
        for i in range(n):
            lines.append(input())
    else:
        debug = True
        lines = [e for e in lines_as_string.split("\n")][1:-1]
        tokens = lines[0].split(" ")
        n = int(tokens[0])
        d = int(tokens[1])

    xs = []
    for i in range(1, n+1):
        tokens = lines[i].split(" ")
        xs.append([int(e) for e in tokens])

    return (n, d, xs)


def solve(n, d, xs):

    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            a = xs[i]
            b = xs[j]
            sum = 0
            for k in range(d):
                sum = sum + (a[k] - b[k])**2
            
            distance = math.sqrt(sum)

            if distance.is_integer():
                count = count + 1

    return count


def main():
    # 出力

    print("%s" % solve(*parse_input()))

#    solve(*parse_input())

if __name__ == '__main__':

    main()
