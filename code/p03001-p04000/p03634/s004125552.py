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
abc = []
for _ in range(n-1):
    a,b,c = li()
    a -= 1
    b -= 1
    abc.append((a,b,c))
q,k = li()
k -= 1
query = [li_() for _ in range(q)]

# 隣接リストつくる
graph = [[] for _ in range(n)]
for frm,to,cost in abc:
    graph[frm].append((cost,to))
    graph[to].append((cost,frm))

# 頂点Kをスタートとするダイクストラ
dist = dijkstra(graph, n, k)

# クエリ処理
for frm,to in query:
    print(dist[frm] + dist[to])