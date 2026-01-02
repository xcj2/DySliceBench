#!/usr/bin/env python3
from functools import lru_cache
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
URL: https://atcoder.jp/contests/dp/tasks/dp_j
J - Sushi / 
実行時間制限: 2 sec / メモリ制限: 1024 MB

配点 : 
100 点

問題文
N 枚の皿があります。 皿には 1,2,…,N と番号が振られています。 
最初、各 i (1≤i≤N) について、皿 i には ai (1≤ai≤3) 個の
    寿司が置かれています。
すべての寿司が無くなるまで、太郎君は次の操作を繰り返し行います。
1,2,…,N の目が等確率で出るサイコロを振り、出目を i とする。 
皿 i に寿司がある場合、皿 i の寿司を 1 個食べる。 
皿 i に寿司が無い場合、何も行わない。
すべての寿司が無くなるまでの操作回数の期待値を求めてください。

解説 :
「皿1に寿司が2個、皿2に寿司が1個」という状態と 
    「皿1に寿司が1個、皿2に寿司が2個」という状態だと、
        操作回数の期待値は同じ。
よく考えると、「どの皿に何個あるか」という
    ところまでわかる必要はなくて、
        「1個の皿がいくつ(c1)、2個の皿がいくつ(c2)、
            3個の皿がいくつ(c3)」だけで期待値は決まることがわかる。
すると結局

dp[c3][c2][c1] = 1 + 
    dp[c3][c2][c1 - 1] * (1の皿が選ばれる確率) + 
        dp[c3][c2 - 1][c1 + 1] * (2の皿が選ばれる確率) + 
            dp[c3 - 1][c2 + 1][c1] * (1の皿が選ばれる確率) + 
                dp[c3][c2][c1] * (0の皿が選ばれる確率) 

この確率漸化式になる
あとはdp[c3][c2][c1]を左辺に移行してごにょごにょして
dp[c3][c2][c1] = (n + 
    dp[c3][c2][c1 - 1] * c1 + 
        dp[c3][c2 - 1][c1 + 1] * c2 + 
            dp[c3 - 1][c2 + 1][c1] * c3) / (c1 + c2 + c3)
という遷移式を完成
メモ化再帰でもできるという噂があるがPythonはカスなので 
    いろいろと工夫する必要があります。
知見的には 
    ====================================
    | 期待値 = Σ ワンステップ前の期待値 * |
    |    そのステップになるための確率)    |
    ====================================
です。
"""
#solve
def solve():
    n = II()
    c = LI()
    c1, c2, c3 = [c.count(i) for i in range(1, 4)]
    d = [[[0] * (n + 2) for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(c3 + 1):
        di = d[i]
        dim1 = d[i - 1]
        for j in range(c3 + c2 + 1 - i):
            dim1jp1 = dim1[j + 1]
            dijm1 = di[j - 1]
            dij = di[j]
            for k in range(c3 + c2 + c1 - i - j + 1):
                l = i + j + k
                if l == 0: continue
                res = n
                if i: res += i * dim1jp1[k]
                if j: res += j * dijm1[k + 1]
                if k: res += k * dij[k-1]
                dij[k] = res / l
    print(d[c3][c2][c1])
    return


#main
if __name__ == '__main__':
    solve()
