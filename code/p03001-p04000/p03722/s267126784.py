#!/usr/bin/env python3
import sys

def BellmanFord(graph: "List[List[int]]", s: int):
    """
    特定の始点から各点への最短距離を求めます。
    重みが負であっても動作します。
    ================
    s: 始点
    graph: 隣接リスト
    ----------------
    第一返り値: 負の閉路があるかいなか
    第二返り値: 最短距離のリスト
    """
    INF = 1e18
    n = len(graph)
    dist = [INF] * n
    dist[s] = 0
    for i in range(n):
        for v in range(n):
            for k in range(len(graph[v])):
                e  = graph[v][k]
                if dist[v] != INF and dist[e[0]] > dist[v] + e[1]:
                    dist[e[0]] = dist[v] + e[1]
                    if i == n-1 and e[0] == n-1:
                        return True, dist
    return False, dist

def solve(N: int, M: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    G = [[] for _ in range(N)]
    for i in range(M):
        G[a[i]-1].append((b[i]-1, c[i]))
    flag, cost = BellmanFord(G, 0)
    if flag:
        print('inf')
    else:
        print(-cost[N-1])
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = -1 * int(next(tokens))
    solve(N, M, a, b, c)

if __name__ == '__main__':
    main()
