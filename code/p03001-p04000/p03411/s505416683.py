import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7
INF = 10 ** 9

N = int(input())

AB = [tuple(map(int, input().split())) for _ in range(N)]
CD = [tuple(map(int, input().split())) for _ in range(N)]

G = [[] for _ in range(2 * N + 2)]

def dfs(v, t, f):
    if v == t:
        return f
    used[v] = True
    for i in range(len(G[v])):
        e = G[v][i]
        if (not used[e[0]]) and e[1] > 0: #辺が使われていなくてかつ残量が0より多い
            d = dfs(e[0], t, min(f, e[1]))
            if d > 0: #更新できるとき
                e[1] -= d
                G[e[0]][e[2]][1] += d
                return d
    return 0

def max_flow(s, f):
    flow = 0
    while True:
        global used
        used = [False] * (2 * N + 2)
        t = dfs(s, f, INF)
        if t == 0:
            return flow
        flow += t

def add_edge(fr, to, cap):
    G[fr].append([to, cap, len(G[to])])
    G[to].append([fr, 0, len(G[fr]) - 1])

for i in range(N):
    add_edge(2 * N, i, 1)
    add_edge(N + i, 2 * N + 1, 1)

for i, (a, b) in enumerate(AB):
    for j, (c, d) in enumerate(CD):
        if a < c and b < d:
            add_edge(i, j + N, 1)
 
print (max_flow(2 * N, 2 * N + 1))
