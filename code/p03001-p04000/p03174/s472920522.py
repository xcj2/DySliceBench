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
URL: https://atcoder.jp/contests/dp/tasks/dp_o
O - Matching / 
実行時間制限: 2 sec / メモリ制限: 1024 MB

配点 : 
100 点

問題文
N 人の男性たちと N 人の女性たちがいます。 
男性たちには 1,2,…,N と番号が振られています。 
同様に、女性たちには 1,2,…,N と番号が振られています。

各 i,j (1≤i,j≤N) について、男性 i と女性 j の相性の良し悪しが
    整数 ai,j によって与えられます。 
ai,j=1 ならば男性 i と女性 j は相性が良く、
    ai,j=0 ならば相性が悪いです。

太郎君は、相性が良い男女どうしのペアを N 組作ろうとしています。 
このとき、各男性および各女性は
    ちょうど 1 つのペアに属さなければなりません。

N 組のペアを作る方法は何通りでしょうか？ 
109+7 で割った余りを求めてください。

制約
入力はすべて整数である。
1≤N≤21
ai,j は0 または 1 である。

解法
配るDP
こういう時は事前にいくつの値が何個bit立ってるかを計算しておくのが良い

知見
    ================================================
    |bit_length = [0]                              |
    |for i in range(n):                            |
    |    bit_length += [x + 1 for x in bit_length] |
    |で2**n-1までのbitの立っている数を前計算できる     |
    ================================================
"""

#solve
def solve():
    n = II()
    a = LIR(n)
    n1 = 1 << n
    dp = [0] * n1
    dp[0] = 1
    b = [0]
    for i in range(n):
        b += [x + 1 for x in b]

    c = [1 << i for i in range(n)]
    for i in range(n1-1):
        p = b[i]
        ap = a[p]
        for j in range(n):
            if ap[j]:
                j1 = c[j]
                if i & j1:
                    continue
                dp[i|j1] += dp[i]


    print(dp[-1] % mod)


    return


#main
if __name__ == '__main__':
    solve()
