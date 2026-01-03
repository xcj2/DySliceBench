import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from heapq import heappush, heappop

def dijkstra(graph:list, node:int, start:int) -> list:
    # 未探索のノードは距離INF
    INF = float("inf")
    dist = [INF]*node
    
    # 始点ノードの距離を0とし、dfsのためのpriority queを作成
    dist[start] = 0
    heap = [(0,start)]
    
    # 未探索のノードをpriority queueに入れる
    while heap:
        cost, cur_node = heappop(heap)
        
        for nex_cost, nex_node in graph[cur_node]:
            dist_cand = dist[cur_node] + nex_cost
            if dist_cand < dist[nex_node]:
                dist[nex_node] = dist_cand
                heappush(heap, (dist[nex_node], nex_node))
    
    return dist

n = ni()
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = li()
    a -= 1
    b -= 1
    graph[a].append((c,b))
    graph[b].append((c,a))
    
q,k = li()

dist = dijkstra(graph,n,k-1)

xy = [tuple(li_()) for _ in range(q)]

for x,y in xy:
    print(dist[x]+dist[y])