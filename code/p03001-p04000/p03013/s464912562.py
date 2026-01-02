# -*- coding: utf-8 -*-
import sys

sys.setrecursionlimit(100000)
# input = sys.stdin.readline


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


class Mod:
    def __init__(self, m):
        self.m = m

    def add(self, a, b):
        return (a + b) % self.m


def slv(N, M, A):
    m = Mod(10**9 + 7)
    dp = [0] * (N+10)
    b = [False] * (N+10)
    for a in A:
        b[a] = True

    dp[0] = 1
    for i in range(N):
        if not b[i+1]:
            dp[i+1] = m.add(dp[i+1], dp[i])
        if not b[i+2]:
            dp[i+2] = m.add(dp[i+2], dp[i])
    return dp[N]


def main():
    N, M = read_int_n()
    A = [read_int() for _ in range(M)]
    print(slv(N, M, A))


if __name__ == '__main__':
    main()
