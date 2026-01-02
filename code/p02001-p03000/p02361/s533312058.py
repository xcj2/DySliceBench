#!/usr/bin/env python
import string
import sys
from itertools import chain, dropwhile, takewhile

INF = float("inf")


def read(
    *shape, f=int, it=chain.from_iterable(sys.stdin), whitespaces=set(string.whitespace)
):
    def read_word():
        w = lambda c: c in whitespaces
        nw = lambda c: c not in whitespaces
        return f("".join(takewhile(nw, dropwhile(w, it))))

    if not shape:
        return read_word()
    elif len(shape) == 1:
        return [read_word() for _ in range(shape[0])]
    elif len(shape) == 2:
        return [[read_word() for _ in range(shape[1])] for _ in range(shape[0])]


def readi(*shape):
    return read(*shape)


def readi1(*shape):
    return [i - 1 for i in readi(*shape)]


def readf(*shape):
    return read(*shape, f=float)


def reads(*shape):
    return read(*shape, f=str)


def arr(*shape, fill_value=0):
    if len(shape) == 1:
        return [fill_value] * shape[0]
    elif len(shape) == 2:
        return [[fill_value] * shape[1] for _ in range(shape[0])]


def dbg(**kwargs):
    print(
        ", ".join("{} = {}".format(k, repr(v)) for k, v in kwargs.items()),
        file=sys.stderr,
    )


from collections import defaultdict
import heapq
from collections.abc import MutableMapping


class HeapDict(MutableMapping):
    @staticmethod
    def _parent(i):
        return (i - 1) >> 1

    @staticmethod
    def _left(i):
        return (i << 1) + 1

    @staticmethod
    def _right(i):
        return (i + 1) << 1

    def __init__(self, *args, **kw):
        self.heap = []
        self.d = {}
        self.update(*args, **kw)

    def clear(self):
        del self.heap[:]
        self.d.clear()

    def __setitem__(self, key, value):
        if key in self.d:
            self.pop(key)
        wrapper = [value, key, len(self)]
        self.d[key] = wrapper
        self.heap.append(wrapper)
        self._decrease_key(len(self.heap) - 1)

    def _min_heapify(self, i):
        l = self._left(i)
        r = self._right(i)
        n = len(self.heap)
        if l < n and self.heap[l][0] < self.heap[i][0]:
            low = l
        else:
            low = i
        if r < n and self.heap[r][0] < self.heap[low][0]:
            low = r

        if low != i:
            self._swap(i, low)
            self._min_heapify(low)

    def _decrease_key(self, i):
        while i:
            parent = self._parent(i)
            if self.heap[parent][0] < self.heap[i][0]:
                break
            self._swap(i, parent)
            i = parent

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.heap[i][2] = i
        self.heap[j][2] = j

    def __delitem__(self, key):
        wrapper = self.d[key]
        while wrapper[2]:
            parentpos = self._parent(wrapper[2])
            parent = self.heap[parentpos]
            self._swap(wrapper[2], parent[2])
        self.popitem()

    def __getitem__(self, key):
        return self.d[key][0]

    def __iter__(self):
        return iter(self.d)

    def popitem(self):
        """Remove and return a (key, value) pair with the lowest value"""
        wrapper = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
        else:
            self.heap[0] = self.heap.pop(-1)
            self.heap[0][2] = 0
            self._min_heapify(0)
        del self.d[wrapper[1]]
        return wrapper[1], wrapper[0]

    def __len__(self):
        return len(self.d)

    def peekitem(self):
        """Retuen a (key, value) pair with the lowest value"""
        return (self.heap[0][1], self.heap[0][0])


def main():
    """http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=jp"""
    V, E, r = readi(3)
    G = defaultdict(list)
    cost = dict()
    for _ in range(E):
        s, t, d = readi(3)
        G[s].append(t)
        cost[(s, t)] = d

    dist = arr(V, fill_value=INF)
    dist[r] = 0
    # pq = HeapDict((v, dist[v]) for v in range(V))
    pq = [(dist[r], r)]
    while pq:
        # u, _ = pq.popitem()
        _, u = heapq.heappop(pq)
        for v in G[u]:
            new_d = dist[u] + cost[(u, v)]
            if new_d < dist[v]:
                dist[v] = new_d
                # pq[v] = new_d
                heapq.heappush(pq, (dist[v], v))

    for d in dist:
        print("INF" if d == INF else d)


if __name__ == "__main__":
    main()

