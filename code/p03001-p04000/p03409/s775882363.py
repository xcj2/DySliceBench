#最大二部マッチング
def dfs(v, edges, n, visited, matched):
    for u in edges[v]:
        if u in visited:
            continue
        visited.add(u)
        if matched[u] == -1 or dfs(matched[u], edges, n, visited, matched):
            matched[u] = v
            return True
    return False
def examC():
    N = I()
    ab = [LI() for _ in range(N)]
    cd = [LI() for _ in range(N)]
    xn = N; yn = N
    matched = [-1] * yn
    E = [set() for _ in range(xn)]
    for i in range(xn):
        for j in range(yn):
            if ab[i][0]<cd[j][0] and ab[i][1]<cd[j][1]:
                E[i].add(j)
    ans = 0
    for s in range(xn):
        ans += dfs(s, E, yn, set(), matched)
    print(ans)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC()
