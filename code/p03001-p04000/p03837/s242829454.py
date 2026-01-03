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

n,m = li()

edges = []
graph = [[] for _ in range(n)]
adj_mat = [[0]*n for _ in range(n)]

for _ in range(m):
    a,b,c = li()
    a -= 1
    b -= 1
    graph[a].append((c,b))
    graph[b].append((c,a))
    edges.append((a,b,c))
    
# 各点からの最短dist
for i in range(n):
    adj_mat[i] = dijkstra(graph, n, i)
    
    
# 最短路とedgeの比較
ans = 0
for ai, bi, ci in edges:
    if adj_mat[ai][bi] < ci:
        ans += 1
        
print(ans)