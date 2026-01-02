
# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from pprint import pprint
from collections import Counter, defaultdict, deque
import queue
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub

sys.setrecursionlimit(10000)


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


def Prim(g):
    V = list(g.keys())
    for v in g.values():
        V.extend(list(v.keys()))
    V = list(set(V))

    used = set([])
    q = []
    heapq.heappush(q, (0, V[0]))

    ret = 0
    while q:
        c, v = heapq.heappop(q)

        if v in used:
            continue
        used.add(v)
        ret += c
        for u in g[v]:
            heapq.heappush(q, (g[v][u], u))
    return ret


class Dinic:
    def __init__(self, v, inf=sys.maxsize):
        self.V = v
        self.inf = inf
        self.G = [[] for _ in range(v)]
        self.level = [0 for _ in range(v)]
        self.iter = [0 for _ in range(v)]

    def add_edge(self, from_, to, cap):
        # to: 行き先, cap: 容量, rev: 反対側の辺
        self.G[from_].append({'to': to, 'cap': cap, 'rev': len(self.G[to])})
        self.G[to].append({'to': from_, 'cap': 0, 'rev': len(self.G[from_])-1})

    # sからの最短距離をbfsで計算
    def bfs(self, s):
        self.level = [-1 for _ in range(self.V)]
        self.level[s] = 0
        que = queue.Queue()
        que.put(s)
        while not que.empty():
            v = que.get()
            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if e['cap'] > 0 and self.level[e['to']] < 0:
                    self.level[e['to']] = self.level[v] + 1
                    que.put(e['to'])

    # 増加バスをdfsで探す
    def dfs(self, v, t, f):
        if v == t:
            return f
        for i in range(self.iter[v], len(self.G[v])):
            self.iter[v] = i
            e = self.G[v][i]
            if e['cap'] > 0 and self.level[v] < self.level[e['to']]:
                d = self.dfs(e['to'], t, min(f, e['cap']))
                if d > 0:
                    e['cap'] -= d
                    self.G[e['to']][e['rev']]['cap'] += d
                    return d

        return 0

    def max_flow(self, s, t):
        flow = 0
        while True:
            self.bfs(s)
            # bfsで到達不可
            if self.level[t] < 0:
                return flow
            self.iter = [0 for _ in range(self.V)]
            f = self.dfs(s, t, self.inf)
            while f > 0:
                flow += f
                f = self.dfs(s, t, self.inf)


@mt
def slv(N, AB, CD):
    cd_ = [(i+1, x, y) for i, (x, y) in enumerate(CD)]
    cd_x = sorted(cd_, key=lambda x: x[1])
    cd_x_keys = [x[1] for x in cd_x]
    cd_y = sorted(cd_, key=lambda x: x[2])
    cd_y_keys = [y[2] for y in cd_y]

    d = Dinic(2*N+2)
    for i in range(1, N+1):
        d.add_edge(0, i, 1)
        d.add_edge(i+N, 2*N+1, 1)
    for i, (x, y) in enumerate(AB):
        ix = bisect.bisect_left(cd_x_keys, x)
        iy = bisect.bisect_left(cd_y_keys, y)
        e = set([j for j, x, y in cd_x[ix:]]) & set(
            [j for j, x, y in cd_y[iy:]])
        for j in e:
            d.add_edge(i+1, j+N, 1)

    return d.max_flow(0, 2*N+1)


def main():
    N = read_int()
    AB = [read_int_n() for _ in range(N)]
    CD = [read_int_n() for _ in range(N)]

    print(slv(N, AB, CD))


if __name__ == '__main__':
    main()
