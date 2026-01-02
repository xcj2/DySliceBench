# coding: utf-8

import sys
import math
import fractions
import heapq
import collections
import re
import array
import bisect
sys.setrecursionlimit(1000000)

from collections import Counter, defaultdict


def array2d(dim1, dim2, init=None):
    return [[init for _ in range(dim2)] for _ in range(dim1)]

def argsort(l, reverse=False):
    return sorted(range(len(l)), key=lambda i: l[i], reverse=reverse)

def argmin(l):
    return l.index(min(l))


II = lambda: int(input())
MI = lambda: map(int, input().split())



def main():
    N, M = MI()
    in_edges = [set() for _ in range(N)]
    out_edges = [set() for _ in range(N)]
    num_in_edges = [0] * N
    for _ in range(N - 1 + M):
        a, b = MI()
        a -= 1
        b -= 1
        num_in_edges[b] += 1
        in_edges[b].add(a)
        out_edges[a].add(b)
    Root = argmin(num_in_edges)
    parent = [0] * N
    parent[Root] = -1

    q = [Root]

    while q:
        v = q.pop()
        for child in out_edges[v]:
            in_edges[child].remove(v)
            num_in_edges[child] -= 1
            if num_in_edges[child] == 0:
                parent[child] = v
                q.append(child)

    for p in parent:
        print(p + 1)


if __name__ == "__main__":
    main()
