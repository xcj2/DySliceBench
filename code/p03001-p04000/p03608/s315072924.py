# coding:utf-8

import itertools

INF = float('inf')


def inpl(): return list(map(int, input().split()))


def dijkstra(graph, start):
    MAX_SIZE = len(graph)
    visited = [False for _ in range(MAX_SIZE)]
    cost = [INF for _ in range(MAX_SIZE)]
    prev = [None for _ in range(MAX_SIZE)]

    cost[start] = 0
    prev[start] = start
    path = [start + 1]
    while True:
        min_cost = INF
        next = -1
        visited[start] = True
        # 頂点の選択
        for i in range(MAX_SIZE):
            if visited[i]: continue  # 探索済みの頂点は飛ばす
            if graph[start][i]:  # 頂点startと接続されているか判定
                dist = cost[start] + graph[start][i]
                if dist < cost[i]:
                    cost[i] = dist
                    prev[i] = start

            if cost[i] < min_cost:
                min_cost = cost[i]
                next = i

        start = next
        path.append(next + 1)
        if next == -1: break

    # print(cost)
    # print(path)
    return cost


def main():
    N, M, R = inpl()
    r = inpl()

    G = [[None for _ in range(N)] for _ in range(N)]
    for i in range(M):
        a, b, c = inpl()
        G[a - 1][b - 1] = c
        G[b - 1][a - 1] = c

    min_cost = {}
    for s in r:
        min_cost[str(s)] = dijkstra(G, s - 1)

    ans = INF
    for root in itertools.permutations(r, R):
        dist = 0
        for i in range(R - 1):
            s = str(root[i])
            dist += min_cost[s][root[i + 1] - 1]
        ans = min(ans, dist)

    print(ans)


if __name__ == '__main__':
    main()
