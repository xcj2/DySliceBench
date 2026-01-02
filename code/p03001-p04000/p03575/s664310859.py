from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m = inpl()
g = [[] for _ in range(n)]
r = dict()
cnt = 0
for _ in range(m):
    a,b = inpl()
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    r[cnt] = (a-1,b-1)
    cnt += 1
res = 0
def chk(g):
    seen = [False] * n
    seen[0] = True
    q = deque([0])
    while q:
        v = q.popleft()
        for nv in g[v]:
            if seen[nv]:
                continue
            seen[nv] = True
            q.append(nv)
    if sum(seen) == n:
        return True
    return False
for i in range(m):
    gg = [[] for _ in range(n)]
    a,b = r[i]
    for j in range(n):
        for k in g[j]:
            if (j,k) == (a,b) or (j,k) == (b,a):
                continue
            gg[j].append(k)
    if not chk(gg):
        res += 1
print(res)    