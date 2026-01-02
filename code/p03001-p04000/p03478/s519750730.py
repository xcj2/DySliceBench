# -*- coding: utf-8 -*-
"""
https://beta.atcoder.jp/contests/abc083/tasks/abc083_b

"""
import sys
from sys import stdin
input = stdin.readline


def digits_sum(N):
    ans = 0
    while N:
        ans += (N % 10)
        N //= 10
    return ans


def solve(N, A, B):
    ans = []
    for i in range(1, N+1):
        d_sum = digits_sum(i)
        if A <= d_sum <= B:
            ans.append(i)
    return sum(ans)


def main(args):
    N, A, B = map(int, input().split())
    ans = solve(N, A, B)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
