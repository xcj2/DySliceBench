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

    r = int(input())
    print(3 * (r ** 2))


if __name__ == '__main__':
    main()
