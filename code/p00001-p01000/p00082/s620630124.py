# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0082

"""
import sys
from sys import stdin
from collections import deque
input = stdin.readline


def calc_remaining(data, carriges):
    # ??????????????£????????°?????????
    total = 0
    for d, c in zip(data, carriges):
        if d > c:
            total += d - c
    return total


def solve(data):
    carriges = deque([1, 4, 1, 4, 1, 2, 1, 2])

    min_remaining = float('inf')
    min_carrige_value = float('inf')

    for i in range(8):
        remaining = calc_remaining(data, carriges)
        if remaining < min_remaining:
            min_remaining = remaining
            min_carrige_value = int(''.join(map(str, carriges)))
        elif remaining == min_remaining:
            carrige_value = int(''.join(map(str, carriges)))
            if carrige_value < min_carrige_value:
                min_carrige_value = carrige_value
        carriges.rotate(1)

    return min_remaining, min_carrige_value


def main(args):
    for line in sys.stdin:
        # data = [2, 3, 1, 4, 0, 1, 0, 1]
        # data = [4, 2, 3, 2, 2, 2, 1, 1]
        data = [int(x) for x in line.split()]
        _, result = solve(data)
        print(' '.join(map(str, list(str(result)))))



if __name__ == '__main__':
    main(sys.argv[1:])
    