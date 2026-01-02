#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-

N = int(input())
a = list(map(int, input().split()))
assert len(a) == N

# 解説を参照
# https://img.atcoder.jp/arc101/editorial.pdf

def mergesort(S, f, t):
    global T

    if t - f <= 1:
        return 0

    mid = (f + t) // 2
    n1 = mergesort(S, f, mid)
    n2 = mergesort(S, mid, t)
    n = n1 + n2
    i = f
    j = mid
    k = f
    while i < mid and j < t:
        if S[i] <= S[j]:
            T[k] = S[i]
            i += 1
            n += t - j
        else:
            T[k] = S[j]
            j += 1
        k += 1

    while i < mid:
        T[k] = S[i]
        i += 1
        k += 1
    assert k == j
    for i in range(f, k):
        S[i] = T[i]
    return n

def inversion(S):
    """リストSの転倒数"""
    global T
    T = [0] * len(S)
    return mergesort(S, 0, len(S))

def n_median_larger_than_or_equal_to(x):
    """aの部分列の中央値のうちx以上のものの個数"""

    # aの要素を -1, 1 に置換したリスト
    b = [-1 if e < x else 1 for e in a]
    # bの累積和
    S = [0]
    for e in b:
        S.append(S[-1] + e)
    # Sの転倒数
    return inversion(S)

# 条件を満たす x の最大値を2分探索で探す
lo = 1
hi = max(a)

ncomb = N * (N + 1) // 2    # 部分列の個数

while lo < hi:
    mid = (lo + hi + 1) // 2
    nm = n_median_larger_than_or_equal_to(mid)
    if nm >= (ncomb + 1) // 2:
        lo = mid
    else:
        hi = mid - 1

print(lo)
