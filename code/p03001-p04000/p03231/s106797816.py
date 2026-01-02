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

    # 文字列Xのk * D + 1(k = 0 ~ L // D)番目の文字は
    # Sのk * D // ln + 1(k = 0 ~ D // lm)文字目と、
    # Tのk * D // lm + 1(k = 0 ~ D // ln)文字目の
    # 両方で使われる
    D = lcm(ln, lm)

    li_S = []
    for i in range(0, N, D // ln):
        li_S.append(S[i])

    li_T = []
    for i in range(0, M, D // lm):
        li_T.append(T[i])

    # print(li_S, li_T)
    # S, Tの両方で使われる文字が一致しているか判定
    if li_S == li_T:
        return L
    else:
        return -1


N, M = inpl()
S = input()
T = input()
print(solve(N, M, S, T))
