import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]
Y = [list(map(int, input().split())) for _ in range(N)]

def gen_graph(s, t, n, m):
    graph = [[] for _ in range(n + m + 2)]
    def add_edges(u, v, c):
        graph[u].append([v, c, len(graph[v])])
        graph[v].append([u, 0, len(graph[u]) - 1])

    for i in range(n):
        add_edges(s, i, 1)
    
    for i in range(m):
        add_edges(i + n, t, 1)
        
    for i, (a, b) in enumerate(X):
        for j, (c, d) in enumerate(Y):
            if a < c and b < d:
                add_edges(i, j + n, 1)
                
    return graph


def dfs(u, t, f):
    if u == t:
        return f
    
    used[u] = True
    for i in range(len(graph[u])):
        v, c, r = graph[u][i]
        if not used[v] and c > 0:
            d = dfs(v, t, min(f, c))
            if d > 0:
                graph[u][i][1] -= d
                graph[v][r][1] += d
                return d

    return 0


s = 2 * N
t = s + 1
graph = gen_graph(s, t, N, N)
flow = 0
while True:
    used = [False] * (2 * N + 2)
    f = dfs(s, t, 10 ** 9 + 7)
    flow += f
    if f == 0:
        break
        
print(flow)
