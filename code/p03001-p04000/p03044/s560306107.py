from collections import Counter,defaultdict
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

def dfs(x):
    for p in g[x]:
        # print(p[0])
        if color[p[0]] != -1:
            continue
        if p[1] % 2: #odd
            if color[x]: #pre=white
                color[p[0]] = 0
            else:
                color[p[0]] = 1
        else:
            if color[x]: #pre=white
                color[p[0]] = 1
            else:
                color[p[0]] = 0
        dfs(p[0])
n = inp()
g = [[] for i in range(n)]
#0:黒 1:白 -1:未訪問
color = [-1] * n

for i in range(n-1):
    u,v,w = inpl()
    g[u-1].append([v-1,w])
    g[v-1].append([u-1,w])
# print(g)
color[0] = 0
dfs(0)
for i in range(1,n):
    if color[i] != -1:
        continue
    dfs(i)
for i in range(n):
    print(color[i])