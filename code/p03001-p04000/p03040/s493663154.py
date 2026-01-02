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
MIT = lambda: tuple(MI())
MIS = lambda: input().split()


class WHeap(object):
    def __init__(self):
        self._heap1 = []
        self._heap2 = []
        self.sum_h1 = 0
        self.sum_h2 = 0

    def __len__(self):
        return len(self._heap1) + len(self._heap2)

    def iter(self):
        for i in self._heap1:
            yield -i
        for i in self._heap2:
            yield i

    def __str__(self):
        return str(self._heap1) + " " + str(self._heap2)

    def push(self, n):
        if len(self) % 2 == 0:
            if not self._heap2 or n <= self._heap2[0]:
                heapq.heappush(self._heap1, -n)
                self.sum_h1 += n
            else:
                d = self._heap2[0]
                heapq.heappush(self._heap1, -heapq.heappop(self._heap2))
                self.sum_h1 += d
                self.sum_h2 -= d
                heapq.heappush(self._heap2, n)
                self.sum_h2 += n
        else:
            if n < -self._heap1[0]:
                d = -self._heap1[0]
                heapq.heappush(self._heap2, -heapq.heappop(self._heap1))
                self.sum_h1 -= d
                self.sum_h2 += d
                heapq.heappush(self._heap1, -n)
                self.sum_h1 += n
            else:
                heapq.heappush(self._heap2, n)
                self.sum_h2 += n

    def med(self):
        return -self._heap1[0]

    def pop(self, n):
        result = self.med()
        if len(self) % 2 == 0:
            heapq.heappop(self._heap1)
            heapq.heappush(self._heap1, -heapq.heappop(self._heap2))
        else:
            heapq.heappop(self._heap1)


def main():
    Q = II()
    wh = WHeap()
    B = 0
    for _ in range(Q):
        query = MIT()
        if query[0] == 1:
            wh.push(query[1])
            B += query[2]
        else:
            x = wh.med()
            if len(wh) % 2 == 0:
                f = - wh.sum_h1 + wh.sum_h2 + B
            else:
                f = x - wh.sum_h1 + wh.sum_h2 + B
            print(x, f)


if __name__ == "__main__":
    main()
