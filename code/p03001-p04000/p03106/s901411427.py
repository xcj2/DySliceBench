# -*- coding: utf-8 -*-

import sys

def gcd(a, b):

    c = min(a, b)
    d = max(a, b)
    r = 0    
    while True:
        r = d % c
        if r == 0:
            break
        d = c
        c = r

    return c


def parse_input(lines_as_string = None):


    lines = []
    if lines_as_string is None:
        lines.append(input())
    else:
        lines = [e for e in lines_as_string.split("\n")][1:-1]
 
    tokens = lines[0].split(" ")
    a = int(tokens[0])
    b = int(tokens[1])
    k = int(tokens[2])

    return (a, b, k)


def solve(a, b, k):

    tmp = gcd(a, b)

    div = tmp - 1
    order = 1
    current = tmp
    while div > 0:
        if order == k:
            break

        if tmp % div == 0:
           order += 1
           current = div

        div -= 1

    return current

def main():
    # 出力

    print("%s" % solve(*parse_input()))

if __name__ == '__main__':

    main()
