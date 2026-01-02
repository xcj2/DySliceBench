# coding:utf-8

import sys


input = sys.stdin.readline
INF = float('inf')


def inpl(): return list(map(int, input().split()))


# 整数(x, y)最大公約数を求める
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        x, y = y, x % y
        return gcd(x, y)


# 整数(x, y)最小公倍数を求める
def lcm(x, y):
    return x * y // gcd(x, y)


def solve(N, M, S, T):
    L = lcm(N, M)
    ln, lm = L // N, L // M

    # 文字列Xのk * lcm(L/N, L/M) (k = 0 ~ gcd(N, M) - 1)番目の文字は
    # S[k * lcm(L/N, L/M) / (L/N)]と
    # T[k * lcm(L/N, L/M) / (L/M)]で使われる
    D = lcm(ln, lm)
    A = D // ln
    B = D // lm
    for i in range(gcd(N, M)):
        if S[A * i] != T[B * i]:
            break
    else:
        return L
    return -1


N, M = inpl()
S = input()
T = input()
print(solve(N, M, S, T))
