n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append([])
    for j in range(n):
        graph[i].append(0)

for i in range(m):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

def adjacent(g, v):
    adj = []    
    for i in range(n):
        if g[v-1][i] == 1:
            adj.append(i+1)
    return adj


def dfs(g, v):
    visited = []
    stack = []
    
    stack.append(v)
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for w in adjacent(g, node):
                if w not in visited:
                    stack.append(w)
    return visited
            

def cut(g):
    bridge = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                g[i][j] = 0
                g[j][i] = 0
                if len(dfs(g,i+1)) < n:
                    bridge = bridge + 1
                g[i][j] = 1
                g[j][i] = 1
    bridge = bridge // 2
    return bridge

print(cut(graph))