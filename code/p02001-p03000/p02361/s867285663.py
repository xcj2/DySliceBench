import sys
stdin = sys.stdin
 
sys.setrecursionlimit(10**7) 
 
def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


'''
ダイクストラ法
----------
input
    graph: 隣接リスト (list)
    start: 開始ノード番号
    INF  : distの最大値

output
    dist : startから各ノードへの距離 (list)
    
'''
from heapq import heappush, heappop

def dijkstra(graph: list, start, INF=float('inf')) -> list:
    n = len(graph)
    dist = [INF]*n
    visited = [False]*n
    
    dist[start] = 0
    que = [(0, start)]
    
    while que:
        cost, cur = heappop(que)
        
        if visited[cur]:
            continue
        
        visited[cur] = True
        
        for nextnode, edgecost in graph[cur]:
            nextcost = cost + edgecost
            if nextcost < dist[nextnode]:
                dist[nextnode] = nextcost
                heappush(que, (nextcost, nextnode))
      
    return dist

n,e,r = li()
graph = [[] for _ in range(n)]

for _ in range(e):
    s,t,d = li()
    graph[s].append((t, d))

INF = 1<<62
dist = dijkstra(graph, r, INF)

for di in dist:
    print('INF' if di == INF else di)
