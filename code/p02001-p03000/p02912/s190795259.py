import sys
from collections import defaultdict, deque

import heapq
import math


class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        return heapq.heappop(self.hq) * self.sign

    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)

    def top(self):
        return self.hq[0] * self.sign

    def sum(self):
        return -sum(self.hq)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    heap = Heapq(A, True)

    for _ in range(M):
        a = heap.pop()
        heap.push(math.floor(a / 2))

    print(heap.sum())


if __name__ == '__main__':
    main()
