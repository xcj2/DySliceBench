#!/usr/bin/env python3
import sys
INF = float("inf")
from collections import Counter
import heapq


class MinHeap(object):
    def __init__(self, x):
        self.heap = [e for e in x]
        heapq.heapify(self.heap)

    def push(self, value):
        heapq.heappush(self.heap, value)

    def pop(self):
        return heapq.heappop(self.heap)


def solve(N: int, K: int, a: "List[int]", b: "List[int]"):
    mh = MinHeap([])
    counter = Counter()
    for aa, bb in zip(a, b):
        if aa not in counter:
            mh.push(aa)
        counter[aa] += bb
    # print(mh.heap)
    # print(counter)

    while True:
        m = mh.pop()
        if counter[m] >= K:
            break
        else:
            K -= counter[m]
    print(m)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, K, a, b)


if __name__ == '__main__':
    main()
