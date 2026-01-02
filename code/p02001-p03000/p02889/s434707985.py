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
inf = float('INF')

#A
def A():
    return

#B
def B():
    return

#C
def C():
    return

#D
def D():
    return

#E
def E():
    n, m, l = LI()
    dist = [[inf] * n for i in range(n)]

    for _ in range(m):
        a, b, c = LI_()
        c += 1
        if c > l:
            continue
        dist[a][b] = c
        dist[b][a] = c

    supply = [[n] * n for i in range(n)]
    for k in range(n):
        distk = dist[k]
        for i in range(n):
            if i == k:
                continue
            disti = dist[i]
            distik = dist[i][k]
            for j in range(i + 1, n):
                if distik + distk[j] < disti[j]:
                    disti[j] = distik + distk[j]
                    dist[j][i] = disti[j]

    lis = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if dist[i][j] <= l:
                supply[i][j] = 0
                supply[j][i] = 0
                lis[i].append(j)
                lis[j].append(i)

    for i in range(n):
        q = []
        for k in lis[i]:
            heappush(q, (0, k))
        supplyi = supply[i]

        while q:
            time, p = heappop(q)
            for k in lis[p]:
                if supplyi[k] > time + 1:
                    supplyi[k] = time + 1
                    heappush(q, (time + 1, k))

    q = II()
    for _ in range(q):
        s, t = LI_()
        if dist[s][t] == inf:
            print(-1)
            continue
        else:
            print(supply[s][t])
    return


#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    E()
