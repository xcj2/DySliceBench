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

def dfs(graph:list, node:int, start:int) -> list:
    # 未探索のノードは距離INF
    INF = float("inf")
    dist = [INF]*node
    
    # 始点ノードの距離を0とし、dfsのためのstackを作成
    dist[start] = 0
    stack = [(0,start)]
    
    while stack:
        cost, cur_node = stack.pop()

        # 未探索のノードをstackに入れる
        for nex_cost, nex_node in graph[cur_node]:
            if dist[nex_node] != INF:
                continue
            else:
                dist[nex_node] = dist[cur_node] + nex_cost
                stack.append((dist[nex_node],nex_node))
                
    return dist

n = ni()
a = [ni() for _ in range(n)]

adj = [[] for _ in range(n)]

for i in range(n):
    adj[i].append((1,a[i]-1))

dist = dfs(adj, n, 0)

if dist[1] != float("inf"):
    print(dist[1])
else:
    print(-1)