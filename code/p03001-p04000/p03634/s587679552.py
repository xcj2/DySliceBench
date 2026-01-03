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

n = inp()
g = [[] for i in range(n)]
cc = dict()
for i in range(n-1):
    a,b,c = inpl()
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
    cc[(a,b)] = c
    cc[(b,a)] = c
q,k = inpl()
k -= 1
cost = [INF] * n
cost[k] = 0
def dfs(node,c):
    for next in g[node]:
        if cost[next] == INF:
            cost[next] = c + cc[(node,next)]
            dfs(next,cost[next])

dfs(k,0)
res = [0] * q
for i in range(q):
    x,y = inpl()
    x -= 1
    y -= 1
    res[i] = cost[x] + cost[y]
for z in res:
    print(z)
