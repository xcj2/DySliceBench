import heapq
import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def dijkstra(edges, n_nodes, start=0):
    dist = [float("inf")] * n_nodes
    dist[start] = 0

    # 優先度キュー
    q = [(dist[start], start)]
    heapq.heapify(q)

    while q:
        d, i = heapq.heappop(q)

        if dist[i] < d:
            continue

        for weight, j in edges[i]:
            tmp = dist[i] + weight
            if dist[j] > tmp:
                dist[j] = tmp
                heapq.heappush(q, (dist[j], j))

    return dist


def main():
    N = int(input())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append((w, v))
        edges[v].append((w, u))

    dist = dijkstra(edges, N)

    for d in dist:
        if d % 2 == 0:
            print(0)
        else:
            print(1)


if __name__ == "__main__":
    main()
