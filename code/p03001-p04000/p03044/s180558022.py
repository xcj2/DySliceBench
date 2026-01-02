# coding: utf-8

import sys
import math

import array
import bisect
import collections
from collections import Counter, defaultdict
import fractions
import heapq
import re

sys.setrecursionlimit(1000000)


def array2d(dim1, dim2, init=None):
    return [[init for _ in range(dim2)] for _ in range(dim1)]

def argsort(l, reverse=False):
    return sorted(range(len(l)), key=lambda i: l[i], reverse=reverse)

def argmin(l):
    return l.index(min(l))

def YESNO(ans, yes="YES", no="NO"):
    print([no, yes][ans])

II = lambda: int(input())
MI = lambda: map(int, input().split())
MIL = lambda: list(MI())
MIS = lambda: input().split()


def bfs(nm, N):
    color = [None] * N
    visited = [False] * N
    q = collections.deque()

    def _bfs(node, before):
        if visited[node]: return
        visited[node] = True
        if before is None:
            color[node] = 0
        else:
            if nm[node][before] % 2 == 0:
                color[node] = color[before]
            else:
                color[node] = 0 if color[before] == 1 else 1
        for k in nm[node].keys():
            q.append((k, node))
        while(q):
            n, b = q.pop()
            _bfs(n, b)

    _bfs(0, None)
    return color


def main():
    N = II()
    nm = {i: {} for i in range(N)}
    for i in range(N-1):
        u, v, w = MI()
        nm[u-1][v-1] = nm[v-1][u-1] = w
    for c in bfs(nm, N):
        print(c)


if __name__ == "__main__":
    main()
