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

def Dijkstra(num, start, vedge):
    """ vedge は DAG の 重みとして vedge[from] = (to, value)　としておくこと """
    """ DAGでない場合は vedge[from] と vedge[to] の両方を作ること """
    """ dist[i] は start から i までの最短距離 """

    dist = [float("inf") for i in range(num)]
    dist[start] = 0
    q = [[dist[start], start]]
    while q:
        du, u = heappop(q)
        for j, k in vedge[u]:
            if dist[j] > du + k:
                dist[j] = du + k
                heappush(q, [dist[j], j])
    return dist



#solve
def solve():
    n, m, s, t = LI()
    s -= 1
    t -= 1
    uva = defaultdict(list)
    uvb = defaultdict(list)
    for _ in range(m):
        u, v, a, b = LI_()
        a += 1
        b += 1
        uva[u].append((v, a))
        uva[v].append((u, a))
        uvb[u].append((v, b))
        uvb[v].append((u, b))
    dista = Dijkstra(n, s, uva)
    distb = Dijkstra(n, t, uvb)
    a = [None] * n
    for i in range(n):
        a[i] = dista[i] + distb[i]
    a = a[::-1]
    for i in range(1,n):
        a[i] = min(a[i], a[i - 1])
    a = a[::-1]
    for i in range(n):
        print(10**15-a[i])
    return


#main
if __name__ == '__main__':
    solve()
