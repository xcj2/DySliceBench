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
edges = []
res = [defaultdict(int) for i in range(n)]
for i in range(n-1):
    a,b = inpl()
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
    edges.append([a,b])
def dfs(e,prev_edge=-1,prev_color=-1):
    cnt = 1
    for ne in g[e]:
        if res[e][ne] or ne == prev_edge:
            continue
        if cnt == prev_color:
            cnt += 1
        res[e][ne] = cnt
        res[ne][e] = cnt
        dfs(ne,e,cnt)
        cnt += 1
dfs(0)
m = 0
for eee in g:
    m = max(m, len(eee))
print(m)
for a,b in edges:
    print(res[a][b])
