import numpy as np
from collections import defaultdict
from heapq import heappush, heappop


def djkstra_adj_list(adj_list, src):
    dist = defaultdict(lambda: np.inf)
    dist[src] = 0

    prev = defaultdict(lambda: None)

    queue = []
    heappush(queue, (dist[src], src))

    while len(queue) > 0:
        dist_u, u = heappop(queue)
        vs = adj_list[u]
        for v, weight in vs:
            alt = dist_u + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heappush(queue, (alt, v))

    return dist, prev


def djkstra_adj_mat(adj_mat, src):
    dist = defaultdict(lambda: np.inf)
    dist[src] = 0

    prev = defaultdict(lambda: None)

    queue = []
    heappush(queue, (dist[src], src))

    while len(queue) > 0:
        dist_u, u = heappop(queue)
        vs = np.argwhere(adj_mat[u] > 0).flatten()
        for v in vs:
            weight = adj_mat[u, v]
            alt = dist_u + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heappush(queue, (alt, v))

    return dist, prev


def main():
    N = int(input())

    adj_list = [[] for _ in range(N)]

    for _ in range(N-1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        adj_list[a].append((b, c))
        adj_list[b].append((a, c))

    Q, K = map(int, input().split())
    K -= 1

    dist, prev = djkstra_adj_list(adj_list, K)

    ans = []
    for _ in range(Q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        ans.append(dist[x] + dist[y])

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
