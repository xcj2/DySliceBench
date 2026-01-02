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

def isnibu(graph:list, dist:list) -> bool:
    for i,edges in enumerate(graph):
        for _, j in edges:
            if dist[i]%2 == dist[j]%2:
                return False
    
    return True
    
    

n,m = li()

adj_lst = [set() for _ in range(n)]

for _ in range(m):
    a,b = li_()
    
    adj_lst[a].add((1,b))
    adj_lst[b].add((1,a))
    
dist = dfs(adj_lst, n, 0)

nibu = isnibu(adj_lst, dist)

ans = 0
if isnibu(adj_lst, dist):
    ans = sum([dist[i]%2 == 1 for i in range(n)]) * sum([dist[i]%2 == 0 for i in range(n)]) - m
    
else:
    ans = n*(n-1)//2 - m
    
print(ans)