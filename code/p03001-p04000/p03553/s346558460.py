import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 6))
from collections import deque

MAX_V = 100000
G = [[] for _ in range(MAX_V)]
level = [0 for _ in range(MAX_V)]
iter = [0 for _ in range(MAX_V)]


def add_edge(fr, to, cp):
    G[fr].append((to, cp, len(G[to])))
    G[to].append((fr, 0, len(G[fr])-1))


# sからの最短距離をBFSで計算
def bfs(s):
    for i in range(MAX_V):
        level[i] = -1
    que = deque()
    level[s] = 0
    que.append(s)
    while len(que) != 0:
        v = que.popleft()
        for e in G[v]:
            if e[1] > 0 and level[e[0]] < 0:
                level[e[0]] = level[v] + 1
                que.append(e[0])


def dfs(v, t, f):
    if v == t:
        return f
    for i in range(iter[v], len(G[v])):
        if G[v][i][1] > 0 and level[v] < level[G[v][i][0]]:
            d = dfs(G[v][i][0], t, min(G[v][i][1], f))
            if d > 0:
                G[v][i] = (G[v][i][0], G[v][i][1]-d, G[v][i][2])
                G[G[v][i][0]][G[v][i][2]] = (G[G[v][i][0]][G[v][i][2]][0], G[G[v][i][0]][G[v][i][2]][1]+d, G[G[v][i][0]][G[v][i][2]][2])
                return d
    return 0


def max_flow(s, t, FLW_LIM=10**18):
    flow = 0
    while True:
        bfs(s)
        if level[t] < 0:
            return flow
        for i in range(MAX_V):
            iter[i] = 0
        f = 0
        while True:
            f = dfs(s, t, FLW_LIM)
            if f == 0:
                break
            flow += f


def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            add_edge(i, j, 10**18+5)
    for i, _a in enumerate(a):
        if _a < 0:
            add_edge(0, i+1, -_a)
        else:
            add_edge(i+1, n+1, _a)
    ans = 0
    for _a in a:
        if _a > 0:
            ans += _a
    print(ans - max_flow(0, n+1))


if __name__ == '__main__':
    main()
