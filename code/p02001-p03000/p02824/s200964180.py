#!/usr/bin/env python3

import sys
import numpy as np


def check(N, M, V, P, As, i):
    # As = 3 2 2 1 1 0
    border = As[P - 1]
    a = As[i]
    # iはTop Pに入っている
    if a >= border:
        return True
    # iに全票入れてもTop Pに入れない
    if a + M < border:
        return False

    # iがTop Pに入るのを保てる最大の票数を計算
    num = M  # i番目に全票
    num += (P - 1) * M  # Top 1からP-1までには全票いれてよい
    num += (N - i - 1) * M # iよりあとのものにも全票いれてよい
    for j in range(P - 1, i): # Top Pからi-1まで、同票までOK
        num += (a + M - As[j])
    
    return num >= M * V


def solve(N, M, V, P, As):

    As = As[:]
    As.sort(reverse=True)

    # for j in range(N):
    #     print("j, check = ", j, check(N, M, V, P, As, j))

    # 二分探索がなりたたない場合を除外
    if check(N, M, V, P, As, N-1):
        return N

    ok = 0
    ng = N - 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(N, M, V, P, As, mid):
            ok = mid
        else:
            ng = mid

    return ok + 1


def main():
    N, M, V, P = map(int, input().split())
    As = list(map(int, input().split()))
    print(solve(N, M, V, P, As))

main()