# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0114
"""
import sys


def lcm(x, y):
    return x*y//gcd(x, y)


def gcd(x, y):
    if x < y:
        temp = x
        x = y
        y = temp
    while y > 0:
        r = x % y
        x = y
        y = r
    return x


def solve(data):
    a1, m1, a2, m2, a3, m3 = data
    x_cycle = y_cycle = z_cycle = 0
    x = y = z = 1

    while True:
        x = (a1 * x) % m1
        x_cycle += 1
        if x == 1:
            break
    while True:
        y = (a2 * y) % m2
        y_cycle += 1
        if y == 1:
            break
    while True:
        z = (a3 * z) % m3
        z_cycle += 1
        if z == 1:
            break

    return lcm(lcm(x_cycle, y_cycle), z_cycle)


def main(args):
    # data = [2, 5, 3, 7, 6, 13]
    #data = [517, 1024, 746, 6561, 4303, 3125]
    while True:
        data = [int(x) for x in input().split(' ')]
        if data.count(0) == 6:
            break
        result = solve(data)
        print(result)


if __name__ == '__main__':
    main(sys.argv[1:])