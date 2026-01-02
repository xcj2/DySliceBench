#!/usr/bin/env python3

import math

def is_sqrt(n):
    s = int(math.sqrt(n))
    return s*s == n


def d2(d, pi, pj, xss):
    return sum([(xss[pi][i] - xss[pj][i])**2 for i in range(d)])


def solv(n, d, xss):
    count = 0
    for pi in range(n):
        for pj in range(pi):
            dd = d2(d, pi, pj, xss)
            if is_sqrt(dd):
                count += 1
    return count

if __name__ == '__main__':

    n,d = map(int, input().split())

    xss = []

    for _ in range(n):
        xss.append([int(x) for x in input().split()])

    ans = solv(n, d, xss)
    print(ans)
