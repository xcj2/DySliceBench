#!/usr/bin/env python3

from pprint import pprint
from collections import deque, defaultdict
import itertools
import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.buffer.readline
INF = float('inf')


n, q = map(int, input().split())
queries = []
for _ in range(q):
    com, x, y = map(int, input().split())
    queries.append([com, x, y])

parents = [i for i in range(n)]
size = [1 for _ in range(n)]


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
        return
    if x_root < y_root:
        x_root, y_root = y_root, x_root
    parents[y_root] = x_root
    size[x_root] += size[y_root]


for com, x, y in queries:
    if com == 0:
        unite(x, y)
    else:
        if same(x, y):
            print(1)
        else:
            print(0)

