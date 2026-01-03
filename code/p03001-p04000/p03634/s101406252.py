import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    # https://atcoder.jp/contests/abc070/tasks/abc070_d
    # https://atcoder.jp/contests/abc070/submissions/12486326

    import sys
    from collections import deque

    def dijkstra(V, adj, root):
        que = deque()
        que.append(root)
        seen = [-1] * (N + 1)
        seen[root] = 0
        par = [0] * (N + 1)
        child = [[] for _ in range(N + 1)]
        seq = []
        while que:
            v = que.popleft()
            seq.append(v)
            for u, c in adj[v]:
                if seen[u] == -1:
                    seen[u] = seen[v] + c
                    par[u] = v
                    child[v].append(u)
                    que.append(u)
        seq.reverse()

        return seen

    N = int(input())
    V, E = N, N - 1  # 頂点の数、辺の数

    adj = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        a, b, c = map(int, input().split())  # 頂点aからbにコストc
        adj[a].append((b, c))
        adj[b].append((a, c))
    Q, root = map(int, input().split())  # rootはスタート地点

    d = dijkstra(V, adj, root)
    for _ in range(Q):
        x, y = map(int, input().split())
        print(d[x] + d[y])


resolve()