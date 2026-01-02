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
inf = float("inf")

"""
URL: https://atcoder.jp/contests/dp/tasks/dp_n
N - Slimes / 
実行時間制限: 2 sec / メモリ制限: 1024 MB

配点 : 
100 点

問題文
N 匹のスライムが横一列に並んでいます。 
最初、左から i 番目のスライムの大きさは ai です。

太郎君は、すべてのスライムを合体させて 1 匹のスライムにしようとしています。 
スライムが 1 匹になるまで、太郎君は次の操作を繰り返し行います。

左右に隣り合う 2 匹のスライムを選び、それらを合体させて新しい 1 匹のスライムにする。 
合体前の 2 匹のスライムの大きさを x および y とすると、
    合体後のスライムの大きさは x+y となる。 
このとき、太郎君は x+y のコストを支払う。 
なお、合体の前後でスライムたちの位置関係は変わらない。
太郎君が支払うコストの総和の最小値を求めてください。
"""
#solve
def solve():
    n = II()
    a = LI()
    dp = [[0] * (n + 1) for i in range(n)]
    acc = [0] + list(itertools.accumulate(a))
    c = [[0] * (n + 1) for i in range(n)]
    def f(l, r):
        tmp = inf
        if c[l][r]: return dp[l][r]
        c[l][r] = 1
        # print(dp, l, r)
        if l + 1 == r: return 0
        
        
        for i in range(l + 1, r):
            tmp = min(tmp, f(l, i) + f(i, r) + acc[r] - acc[l])
        # print(l,r)
        dp[l][r] = tmp
        return tmp
    print(f(0, n))
    # print(dp)
    return


#main
if __name__ == '__main__':
    solve()
