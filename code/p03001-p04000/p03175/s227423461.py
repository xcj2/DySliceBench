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
URL: https://atcoder.jp/contests/dp/tasks/dp_p

P - Independent Set / 
実行時間制限: 2 sec / メモリ制限: 1024 MB

配点 : 
100 点

問題文
N 頂点の木があります。 
頂点には 1,2,…,N と番号が振られています。
各 i (1≤i≤N−1) について、i 番目の辺は頂点 xi と yi を結んでいます。

太郎君は、各頂点を白または黒で塗ることにしました。 ただし、隣り合う頂点どうしをともに黒で塗ってはいけません。

頂点の色の組合せは何通りでしょうか？ 
10**9+7 で割った余りを求めてください。

制約
入力はすべて整数である。
1≤N≤10**5
1≤xi,yi≤N
与えられるグラフは木である。

"""

#solve
def solve():
    n = II()
    edg = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y = LI_()
        edg[x].append(y)
        edg[y].append(x)
    black = [1] * n
    white = [1] * n
    rank = [-1] * n
    rank[0] = [0, None]
    q = deque()
    q.append([0, -1])
    while q:
        node, pre = q.pop()
        for nex in edg[node]:
            if nex == pre:
                continue
            rank[nex] = [rank[node][0] + 1, node]
            q.appendleft((nex, node))

    ans = []
    for i in range(n):
        ans.append((-rank[i][0], rank[i][1], i))
    ans.sort()
    for _, i, j in ans[:-1]:
        black[i] *= white[j]
        white[i] *= white[j] + black[j]
        black[i] %= mod
        white[i] %= mod
    print((white[0] + black[0]) % mod)
    return


#main
if __name__ == '__main__':
    solve()
