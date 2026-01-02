import sys

# import bisect
from collections import Counter, deque, defaultdict
# import copy
# from heapq import heappush, heappop, heapify
# from fractions import gcd
# import itertools
# from operator import attrgetter, itemgetter
import math

# import numpy as np

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

import heapq


class Reverse:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return repr(self.val)


class PriorityQueue:

    def __init__(self, x=[], desc=False):
        if desc:
            for i in range(len(x)):
                x[i] = Reverse(x[i])
        self._desc = desc
        self._container = x
        heapq.heapify(self._container)

    @property
    def is_empty(self):
        return not self._container

    def pop(self):
        if self._desc:
            return heapq.heappop(self._container).val
        else:
            return heapq.heappop(self._container)

    def push(self, item):
        if self._desc:
            heapq.heappush(self._container, Reverse(item))
        else:
            heapq.heappush(self._container, item)

    def top(self):
        if self._desc:
            return self._container[0].val
        else:
            return self._container[0]

    def sum(self):
        return sum(self._container)

    def __len__(self):
        return len(self._container)


def main():
    x, y, a, b, c = list(map(int, readline().split()))
    p = list(map(int, readline().split()))
    q = list(map(int, readline().split()))
    r = list(map(int, readline().split()))

    p.sort()
    q.sort()
    r = PriorityQueue(r,desc=True)

    eat = p[-x:]
    eat.extend(q[-y:])
    eat = PriorityQueue(eat)

    while eat.top() < r.top():
        _ = eat.pop()
        eat.push(r.pop())
        c -= 1
        if c == 0:
            break

    print(eat.sum())





if __name__ == '__main__':
    main()
