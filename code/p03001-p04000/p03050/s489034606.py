# -*- coding: utf-8 -*-
"""
D - DivRem Number
https://atcoder.jp/contests/diverta2019/tasks/diverta2019_d

"""
import sys


def solve(N):
    def divisor(N):
        divisors = set()
        for i in range(1, int(N**0.5)+1):
            if N % i == 0:
                divisors.add(i)
                divisors.add(N // i)
        return divisors

    ans = 0
    for q in divisor(N):
        if q == 1:
            continue
        a, b = divmod(N, q-1)
        if a == b:
            ans += (q-1)
    return ans


def main(args):
    N = int(input())
    ans = solve(N)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
