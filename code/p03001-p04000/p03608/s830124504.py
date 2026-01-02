import sys
stdin = sys.stdin

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from itertools import permutations
from heapq import heappush, heappop

def dijkstra(graph:list, node:int, start:int) -> list:
    # 未探索のノードは距離INF
    INF = float("inf")
    dist = [INF]*node
    
    # 始点ノードの距離を0とし、dfsのためのpriority queを作成
    dist[start] = 0
    heap = [(0,start)]
    searched = [False for _ in range(node)]
    
    # 未探索のノードをpriority queueに入れる
    while heap:
        cost, cur_node = heappop(heap)
        
        if searched[cur_node] or cost > dist[cur_node]:
            continue
        
        for nex_cost, nex_node in graph[cur_node]:
            dist_cand = dist[cur_node] + nex_cost
            if dist_cand < dist[nex_node]:
                dist[nex_node] = dist_cand
                heappush(heap, (dist[nex_node], nex_node))
    
        searched[cur_node] = True
        
        if sum(searched) == node:
            break
    
    return dist

n,m,r = li()
r = list(li_())
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b,c = li()
    a -= 1
    b -= 1
    graph[a].append((c,b))
    graph[b].append((c,a))
    
dists = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    dists[i] = dijkstra(graph, n, i)

routes = list(permutations(r))

ans = 2**64-1
for route in routes:
    temp = 0
    for i in range(len(route)-1):
        temp += dists[route[i]][route[i+1]]
        
    ans = min(ans,temp)
    
print(ans)