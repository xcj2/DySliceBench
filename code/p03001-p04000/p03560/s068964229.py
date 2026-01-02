from heapq import *
from collections import deque

intinf = 10 ** 15

def bfs_01(n, graph, start):
    min_distance = [intinf] * n

    deq = deque()
    min_distance[start] = 0
    deq.append(start)

    while deq:
        src = deq.popleft()
        for dst, cost in graph[src]:
            next_d = min_distance[src] + cost
            if min_distance[dst] <= next_d:
                continue

            min_distance[dst] = next_d
            if cost == 0:
                deq.appendleft(dst)
            elif cost == 1:
                deq.append(dst)
            else:
                print('invalid cost in graph')
                raise ValueError

    return min_distance

def dijkstra(n, graph, start):
    min_distance = [intinf] * n

    # min-heap of (distance, vertex)
    heap = []

    heappush(heap, (0, start))
    min_distance[start] = 0

    while heap != []:
        d, src = heappop(heap)
        if min_distance[src] < d:
            continue
        for dst, cost in graph[src]:
            next_d = d + cost
            if next_d < min_distance[dst]:
                min_distance[dst] = next_d
                heappush(heap, (next_d, dst))

    return min_distance

def main():
    K = int(input())

    # (v, c) in graph[u] <=> u -> v with cost = c
    graph = [[] for _ in range(K)]

    for i in range(K):
        graph[i].append(((i+1) % K, 1))
        graph[i].append((i * 10 % K, 0))

    dist = dijkstra(K, graph, 1)
    # dist = bfs_01(K, graph, 1)

    print(dist[0] + 1)

if __name__ == '__main__':
    main()

