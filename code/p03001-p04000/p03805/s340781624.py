from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n,m = inpl()
g = [[] for i in range(n)]
for i in range(m):
    a,b = inpl()
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
res = 0
seen = [False] * n
def dfs(node,seen):
    global res
    seen[node] = True
    if sum(seen) == n:
        res += 1
    for now in g[node]:
        if not seen[now]:
          dfs(now,seen)  
    seen[node] = False
dfs(0,seen)
print(res)