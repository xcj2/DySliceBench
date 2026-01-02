#!/usr/bin/env python3
# DPL_1_G: Combinatorial - Knapsack Problem with Limitations

from functools import lru_cache
from heapq import heappop, heappush


@lru_cache(maxsize=None)
def index(i, j, sep):
    return (j-i) // sep


def max_value(total_weight, items):
    vs1 = [0] * (total_weight+1)
    vs2 = vs1[:]
    for item in items:
        v, w, m = item
        for i in range(w):
            heap = []
            for j in range(i, total_weight+1, w):
                heappush(heap, (-vs1[j] + index(i, j, w)*v, j))
                x, k = heap[0]
                while index(k, j, w) > m:
                    heappop(heap)
                    x, k = heap[0]
                vs2[j] = vs1[k] + index(k, j, w)*v

        vs1, vs2 = vs2, vs1

    return vs1[total_weight]


def run():
    n, t = [int(i) for i in input().split()]
    vs = []

    for _ in range(n):
        v, w, m = [int(i) for i in input().split()]
        vs.append((v, w, m))

    print(max_value(t, vs))


if __name__ == '__main__':
    run()

