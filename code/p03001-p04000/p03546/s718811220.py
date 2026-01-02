import sys
from heapq import heappush, heappop
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

h,w = li()
graph = [[] for _ in range(10)]

for i in range(10):
    d = list(li())
    for j,dj in enumerate(d):
        graph[i].append((dj,j))
        
a = [list(li()) for _ in range(h)]

dist = [0]*10
for i in range(10):
    dist[i] = dijkstra(graph,10,i)[1]

ans = 0
for row in range(h):
    for col in range(w):
        if a[row][col] != -1:
            ans += dist[a[row][col]]
            
print(ans)