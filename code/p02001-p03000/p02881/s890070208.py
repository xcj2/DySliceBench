# -*- coding: utf-8 -*-
"""
C - Walk on Multiplication Table
https://atcoder.jp/contests/abc144/tasks/abc144_c

"""
import sys


def divisor(n):
    divisors = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors


def solve(N):
    ans = float('inf')
    for d in divisor(N):
        q = N // d
        ans = min(ans, d-1 + q-1)
    return ans


def main(args):
    N = int(input())
    ans = solve(N)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
