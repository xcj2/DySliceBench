#!/usr/bin/python3

import math
import sys


DEBUG = False


def inp():
    return sys.stdin.readline().rstrip()


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def solve(N, A):
    d = {}
    for a in A:
        if a not in d:
            d[a] = 0
        d[a] += 1

    if N % 3 == 0:
        if len(d) > 3:
            return False

        if len(d) == 3:
            a, b, c = d
            if d[a] != d[b] or d[b] != d[c]:
                return False
            arr = [a, b, c]
        elif len(d) == 2:
            a, b = d
            if d[a] * 2 == d[b]:
                arr = [a, b, b]
            elif d[b] * 2 == d[a]:
                arr = [a, a, b]
            else:
                return False
        else:
            (a,) = d
            arr = [a, a, a]

        a, b, c = arr
        if a ^ b == c or a ^ c == b or b ^ c == a:
            return True
        return False

    if len(d) > 1:
        return False

    (a,) = d
    if a != 0:
        return False
    return True


def main():
    N = int(inp())
    A = [int(e) for e in inp().split()]

    print('Yes' if solve(N, A) else 'No')


if __name__ == '__main__':
    main()
