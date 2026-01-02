from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,pprint,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
g = [[] for i in range(n)]
for i in range(n-1):
    a,b,c = inpl()
    g[a-1].append((b-1,c))
    g[b-1].append((a-1,c))
color = [-1] * n 
color[0] = 0
def dfs(node):
    for v,c in g[node]:
        if color[v] != -1:
            continue
        if (c) % 2:
            color[v] = 0 if color[node] else 1
        else: color[v] = 1 if color[node] else 0
        dfs(v)
dfs(0)

for i in color:
    print(i)