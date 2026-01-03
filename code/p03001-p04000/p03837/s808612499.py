#2020-05-28 22:26:38
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, M = map(int,input().split())

def modify(x,y):
    if x>y:
        x,y = y,x
    return (x,y)


edge = [[] for _ in range(N)]
edgeid = dict()
for k in range(M):
    u,v,r = map(int,input().split())
    edge[u-1].append((v-1, r))
    edge[v-1].append((u-1, r))
    edgeid[modify(u-1,v-1)] = k

from heapq import heappop,heappush, heapify
INF = 10**20
def dijkstra2(S, N, Edge):
    # S: start vertex
    # N: number of vertices
    # Edge: adjacent list [node, cost]
    

    dist = [INF]*N
    dist[S] = 0
    root = [-1]*N
    que = [(0, S)]
    heapify(que)
    
    while que:
        c, v = heappop(que)
        if dist[v] < c: continue

        for nv, nc in Edge[v]:
            if c+nc < dist[nv]:
                dist[nv] = c+nc
                root[nv] = v
                heappush(que, (c+nc, nv))
    
    return [dist, root]

def find_path(S,T,root):
    # SからTへのパスを逆順で返す
    path = []
    cur = T
    while cur!=S:
        past = root[cur]
        path.append((past, cur))
        cur = past
    return path

unused_flag = [True] * M
for start in range(N):
    dist, root = dijkstra2(start, N, edge)
    for goal in range(N):
        if start==goal:continue
        for p in find_path(start, goal, root):
            unused_flag[edgeid[modify(p[0],p[1])]] = False

print(sum(unused_flag))