from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    depth[0] = 0
    queue = deque([])
    queue.append(0)
    
    while queue:
        current_node = queue.popleft()
        
        for next_node in adj_list[current_node]:
            if depth[next_node] == -1:
                parent[0][next_node] = current_node
                depth[next_node] = depth[current_node] + 1
                queue.append(next_node)
    
def init():
    bfs() #initialize depth and parent[0]
    
    for k in range(1, log_size):
        for v in range(N):
            if parent[k-1][v] < 0:
                parent[k][v] = -1
            else:
                parent[k][v] = parent[k-1][parent[k-1][v]]

def lca(u, v): #return lowest common ancestor when 0 is root node
    if depth[u] > depth[v]:
        u, v = v, u
    
    for k in range(log_size):
        if (depth[v]-depth[u])>>k & 1:
            v = parent[k][v]
    
    if u == v:
        return u
    
    for k in range(log_size-1, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    
    return parent[0][u]
    
N = int(input())
log_size = N.bit_length() #ceil(log)
depth = [-1] * N
parent = [[-1] * N for _ in range(log_size)]
adj_list = [[] for _ in range(N)]

for i in range(N):
    kc = list(map(int, input().split()))
    
    for ci in kc[1:]:
        adj_list[i].append(ci)
        adj_list[ci].append(i)

init()
q = int(input())

for _ in range(q):
    ui, vi = map(int, input().split())
    print(lca(ui, vi))
