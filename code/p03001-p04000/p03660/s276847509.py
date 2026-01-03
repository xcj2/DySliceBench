# 2020-05-28 22:45:55

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
ab = [list(map(int,input().split())) for _ in range (N-1)]

edge = [[] for _ in range(N)]
for u,v in ab:
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)

fromNode = [0] * N
def dfs(v, p):
    for nv in edge[v]:
        if nv==p:continue 
        fromNode[nv] = v
        dfs(nv, v)
    return 

def pathFind(s, g, fromNode):
    path = []
    while s!=g:
        g = fromNode[g]
        if g==s:break
        path.append(g)
    path.reverse()
    return path
dfs(0,-1)
path = pathFind(0,N-1,fromNode)

colors = [-1]*N
colors[0] = 0
colors[N-1] = 1
for i in range(len(path)):
    if i<=(len(path)-1)//2:
        colors[path[i]] = 0
    else:
        colors[path[i]] = 1

def dfs_color(v, p, c):
    for nv in edge[v]:
        if nv==p:continue 
        if colors[nv]==-1:
            colors[nv] = c
            dfs_color(nv, v, c)
    return 

dfs_color(0,-1,0)
dfs_color(N-1, -1, 1)
for p in path:
    c = colors[p]
    dfs_color(p, -1, c)

B = 0
W = 0
for c in colors:
    if c==0:B+=1
    elif c==1:W+=1

if B>W:
    print('Fennec')
else:
    print('Snuke')