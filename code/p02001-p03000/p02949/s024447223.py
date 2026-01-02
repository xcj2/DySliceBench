import sys
sys.setrecursionlimit(100000)
from collections import defaultdict
edges = []
to = defaultdict(list) # 1から到達できるか
ot = defaultdict(list) # Nから到達できるか
N, M, P = map(int, input().split())
visited_toN = [False]*(N+1)
visited_fm1 = [False]*(N+1)    
for i in range(M):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a,b,-c+P))
    to[a].append(b)
    ot[b].append(a)

def dfs(v):
    global visited_fm1
    if visited_fm1[v]:return
    visited_fm1[v] = True
    for nxt in to[v]:
        dfs(nxt)
    
def dfs_r(v):
    global visited_toN
    if visited_toN[v]:return
    visited_toN[v] = True
    for nxt in ot[v]:
        dfs_r(nxt)
        
dfs(0)
dfs_r(N-1)
is_ok = []

for s, t in zip(visited_fm1,visited_toN):
    is_ok.append(s and t)


# BellmanFord    
INF = 10 ** 18
def bellmanFord(n, edges, s, g):
    """
    input
        n : 頂点の数
        edges : (始点, 終点, コスト)のリスト
        s : 探索の始点
        g : 探索の終点
    output
        sから各点への最短距離
    """    
    d = [INF] * n
    d[s] = 0
    cnt = 0
    while True:
        update = False
        for a, b, c in edges:
            if not is_ok[a]:continue
            if not is_ok[b]:continue
            if d[a] != INF and d[b] > d[a] + c:
                d[b] = d[a] + c
                update = True
        if not update:
            break
        cnt += 1
        # 負閉路の存在をチェック
        if cnt > n:
            print(-1)
            exit()
        # print(d,cnt)
    return d[g]



ans = bellmanFord(N,edges,0,N-1)
print(max(0,-ans))
