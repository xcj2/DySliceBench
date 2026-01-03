#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float("INF")

#A
def A():
    n = S()
    n1 = n[::-1]
    for i in range(len(n)):
        if n1[i] != n[i]:
            print("No")
            return
    print("Yes")
    return

#B
def B():
    a, b, c, d = LI()
    ans = [0 for i in range(101)]
    ans[a] += 1
    ans[b] -= 1
    ans[c] += 1
    ans[d] -= 1
    for i in range(100):
        ans[i+1] += ans[i]
    print(ans.count(2))
#C
def C():
    n = II()
    ans = 1
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    for _ in range(n):
        t = II()
        ans = ans // gcd(ans, t) * t
    print(ans)
    return

#D
def D():
    n = II()
    vedg = defaultdict(list)
    for _ in range(n-1):
        a, b, c = LI()
        vedg[a].append((b, c))
        vedg[b].append((a, c))
    dist = defaultdict(lambda :inf)
    Q, k = LI()
    q = deque([k])
    dist[k] = 0
    while q:
        f = q.pop()
        for t, value in vedg[f]:
            if dist[t] > dist[f] + value:
                dist[t] = dist[f] + value
                q.append(t)
    for _ in range(Q):
        x, y = LI()
        print(dist[x] + dist[y])
    return

#Solve
if __name__ == '__main__':
    D()
