# -*- coding: utf-8 -*-

"""
参考：https://atcoder.jp/contests/abc047/submissions/4077573
"""

import sys
def input(): return sys.stdin.readline().strip()
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N, T = MAP()
aN = LIST()

mx = -INF
l = aN[0]
cnt = 0
for i in range(1,N):
    # 最低値更新なら始点を動かす
    if aN[i] < l:
        l = aN[i]
    else:
        # 最高値更新ならその場所が操作対象になる
        if aN[i] - l > mx:
            mx = aN[i] - l
            cnt = 1
        # 同率最高値なら操作対象が1つ増える
        elif aN[i] - l == mx:
            cnt += 1
print(cnt)
