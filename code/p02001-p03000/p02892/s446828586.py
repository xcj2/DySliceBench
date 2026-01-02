# https://atcoder.jp/contests/agc039/submissions/7877660
from collections import deque

INF = float('inf')


def bfs(n, es):
    parity = [-1] * n
    parity[0] = 0

    dq = deque()
    dq.append(0)
    while dq:
        v = dq.popleft()
        nxt_par = parity[v] ^ 1
        for u in es[v]:
            if parity[u] == -1:
                parity[u] = nxt_par
                dq.append(u)
            else:
                if parity[u] != nxt_par:
                    return False
                    # bipartite = False
    return True
    # bipartite = True


def warshall_floyd(n, g):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    return g


def solve():
    n = int(input())
    es = tuple(set() for _ in range(n))
    g = []
    for v in range(n):
        s = input()
        for u, is_adj in enumerate(map(int, s)):
            if is_adj:
                es[v].add(u)
                es[u].add(v)
        g.append(list(map(int, s)))
    for r, row in enumerate(g):
        for c, cell in enumerate(row):
            if cell == 0 and r != c:
                g[r][c] = INF
        # 隣接頂点間: 1
        # 同一頂点間: 0
        # その他: INF
    # print(es)
    # print(g)

    # 二部グラフ判定
    bipartite = bfs(n, es)
    if not bipartite:
        return -1

    # 最遠点対間距離を求める
    g = warshall_floyd(n, g)
    d = max(max(row) for row in g)
    return d + 1


if __name__ == '__main__':
    print(solve())
