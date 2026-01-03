# 入力
import sys
stdin = sys.stdin

def li(): return [int(x) for x in stdin.readline().split()]
def li_(): return [int(x)-1 for x in stdin.readline().split()]
def lf(): return [float(x) for x in stdin.readline().split()]
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(ns())
def nf(): return float(ns())


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

# 入力
n = ni()

# グラフ作成
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = li()
    a -= 1
    b -= 1
    graph[a].append((c,b))
    graph[b].append((c,a))
    
q,k = li()
query = []
for _ in range(q):
    x,y = li()
    x -= 1
    y -= 1
    query.append((x,y))

# Kからダイクストラ
dist_k = dijkstra(graph, n, k-1)
    

# クエリ処理
for x,y in query:
    print(dist_k[x] + dist_k[y])