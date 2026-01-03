import sys
from math import log2
def input(): return sys.stdin.readline().strip()
sys.setrecursionlimit(10**6)


def main():
    """
    Kの指定があるのに気づかずダブリングでLCA求めちゃった・・・！
    https://algo-logic.info/lca/
    勉強になったから良しとする。ポイントとして
    1. parents[k][u]の求め方がまず再帰
    2. LCAでまず深さを揃えるとこも2べき（必ずfor文はint(log2(N))まで回すこと！）
    3. ダブリングは祖先が一致しない時だけ更新
    を押さえとけば自力で再現できそう？
    """
    N = int(input())
    repn = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        repn[a - 1].append((b - 1, c))
        repn[b - 1].append((a - 1, c))
    depth = [-1] * N
    dist = [0] * N
    parents = [[-1] * N for _ in range(int(log2(N)) + 3)]  # parents[k][u] = (頂点uから2^k先の祖先)

    def dfs(u):
        for v, c in repn[u]:
            if depth[v] != -1: continue
            depth[v] = depth[u] + 1
            dist[v] = dist[u] + c
            parents[0][v] = u
            dfs(v)

    depth[0] = 0
    dfs(0)

    for k in range(int(log2(N)) + 2):
        for u in range(N):
            if parents[k][u] < 0:
                parents[k + 1][u] = -1
            else:
                parents[k + 1][u] = parents[k][parents[k][u]]

    def doubling(u, v):
        if depth[u] < depth[v]: u, v = v, u
        for k in range(int(log2(N)) + 1):
            if ((depth[u] - depth[v]) & (1 << k)):
                u = parents[k][u]
                k += 1
        if u == v: return u
        for k in range(int(log2(N)) + 1, -1, -1):
            if parents[k][u] != parents[k][v]:
                u = parents[k][u]
                v = parents[k][v]
        return parents[0][u]

    Q, K = map(int, input().split())
    for _ in range(Q):
        u, v = map(int, input().split())
        lca1 = doubling(u - 1, K - 1)
        lca2 = doubling(K - 1, v - 1)
        d1 = dist[u - 1] + dist[K - 1] - dist[lca1] * 2
        d2 = dist[K - 1] + dist[v - 1] - dist[lca2] * 2
        print(d1 + d2)



if __name__ == "__main__":
    main()
