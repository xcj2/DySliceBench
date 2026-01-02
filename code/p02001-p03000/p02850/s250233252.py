import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    """
    https://qiita.com/drken/items/4a7869c5e304883f539b#3-3-dfs-%E3%81%AE%E5%86%8D%E5%B8%B0%E9%96%A2%E6%95%B0%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F%E5%AE%9F%E8%A3%85
    cf. https://atcoder.jp/contests/abc138/submissions/13273052
    """

    from collections import deque

    N = int(input())
    M = N-1  # 頂点数，辺数
    # グラフ入力受取 (ここでは無向グラフを想定)
    G = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((b, i))
        G[b].append((a, i))

    seen = [False]*N
    res = [0]*M

    def dfs(G, v):
        col = 1
        parent_col = -1
        if col == parent_col:
            col += 1
        seen[v] = True
        stack = deque([(v, -1)])
        while stack:
            v, parent_col = stack.pop()
            col = 1
            for next_v, edge_ind in G[v]:
                if seen[next_v]:
                    continue
                if col == parent_col:
                    col += 1
                res[edge_ind] = col
                seen[next_v] = True
                stack.append((next_v, col))
                col += 1

    # 頂点 0 をスタートとした探索
    dfs(G, 0)
    print(max(res))
    for i in res:
        print(i)


resolve()