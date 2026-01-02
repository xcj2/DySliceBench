# coding: utf-8
# Your code here!

N = int(input())
R = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]
B = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]
G = [[] for _ in range(2 * N + 2)]

def add_edge(f, to, cap):
    G[f].append([to, cap, len(G[to])])
    G[to].append([f, 0, len(G[f]) - 1])

# S -> R and B -> T
for i in range(N):
    add_edge(0, 1 + i, 1)
    add_edge(N + 1 + i, 2 * N + 1, 1)
    
# R -> B
for i in range(N):
    for j in range(N):
        if R[i][0] < B[j][0] and R[i][1] < B[j][1]:
            add_edge(1 + i, N + 1 + j, 1)

used = [False] * (2 * N + 2)
def dfs(v, t, f):
    if v == t: return f
    used[v] = True
    for i in range(len(G[v])):
        e_to, e_cap, e_rev = G[v][i]
        if used[e_to] == False and e_cap > 0:
            d = dfs(e_to, t, min(f, e_cap))
            if d > 0:
                G[v][i][1] -= d
                G[e_to][e_rev][1] += d
                return d
    return 0
    
def max_flow(s, t):
    global used
    flow = 0
    while True:
        used = [False] * (2 * N + 2)
        f = dfs(s, t, float('inf'))
        if f == 0: return flow
        flow += f
        
print(max_flow(0, 2 * N + 1))
