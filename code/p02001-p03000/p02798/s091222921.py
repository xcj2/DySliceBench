#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

"""
URL : https://atcoder.jp/contests/keyence2020/tasks/keyence2020_d
解説AC

きもすぎBit全探索および転倒数
    （転倒数に結びついたら強い
    　隣通しを入れ替えてsortの操作数→バブルソートの操作数→転倒数
    　これの徹底）

AC例1: 最初に考え付いたのはこっち
    maskでどのindexが裏返しになっているかを保持。
    その状況下で生成される表面の数の配列を作成し(これをLとする)ソート。
    iを[0,n)で回して各A[i],B[i]に対して
    maskをもとにAかBが使用されているかを見る。
    Lにおけるその数のindexとiの差の偶奇は奇数B偶数ならA。
    defalutdictかなんかで各Lの数字とそのindexの偶奇の数とそのindexを保持
    indexとiの差の偶奇とdictからLの各indexが元どの番号にいたかを保持。
    あとは元の番号の配列の転倒数を求めればそのmaskにおける操作数が出る

AC例2: 解説はこっち
    maskではどのindexがすでに左側で固定化されたかを保持。
    巡回セールスマンのようにどこを決めて最後に決めたindexは何か
    というDPでいける。（は？）
    というのもmaskだけではそのマスク内の順番はわからないからね。
    欲しいのはその固定化された物の最大の値なので最悪なんかうまくできるかも
    すごすぎ
    こっちを実装します
    700点をACしたいね(2020/3/25/ 20:05)

    Reference: https://atcoder.jp/contests/keyence2020/submissions/9567775 By:yutaka1999
"""

#solve
def solve():
    n = II()
    A = LI()
    B = LI()
    bit_length = [0] 
    for i in range(n):
        bit_length += [x + 1 for x in bit_length]
    dp = [[-1] * n for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = 0
    for mask in range(1 << n):
        dpm = dp[mask]
        c = bit_length[mask]
        for i in range(n):
            if not((1 << i) & mask) or dpm[i] == -1: continue
            w = B[i] if 1 & i == c & 1 else A[i]
            cost = c
            for j in range(n):
                if 1 & (mask >> j):
                    cost -= 1
                else:
                    v = B[j] if 1 & j != c & 1 else A[j]
                    if v >= w:
                        vl = dpm[i] + cost
                        if dp[mask | (1 << j)][j] == -1 or dp[mask | (1 << j)][j] > vl:
                            dp[mask | (1 << j)][j] = vl

    ans = -1
    for i in range(n):
        if dp[-1][i] != -1:
            if ans == -1 or ans > dp[-1][i]:
                ans = dp[-1][i]
    print(ans)

    return


#main
if __name__ == '__main__':
    solve()
