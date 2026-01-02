#!/usr/bin/python3
from collections import defaultdict
from heapq import heappush, heappop

inf = float('inf')

def inf_matrix(n):
    return [[inf for i in range(n)] for j in range(n)]

def dijkstra(r, w, V):
    result = [inf] * V
    q = []
    heappush(q, (0, r))
    result[r] = 0
    while len(q) > 0:
        min_w, min_next = heappop(q)
        for weight, nxt in w[min_next]:
            if result[nxt] > min_w + weight:
                result[nxt] = min_w + weight
                heappush(q, (min_w + weight, nxt))

    return result


def main():
    V, E, r = map(int, input().split())
    w = defaultdict(list)
    for e in range(E):
        s, t, d = map(int, input().split())
        w[s].append((d, t))

    result = dijkstra(r, w, V)
    for i in range(V):
        if result[i] == inf:
            print('INF')
        else:
            print(result[i])

main()