#!/usr/bin/env python3
import sys
import heapq
sys.setrecursionlimit(10**8)
INF = float("inf")


class MaxHeap(object):
    def __init__(self, x, default=-INF):
        self.heap = [-e for e in x]
        self.default = default
        heapq.heapify(self.heap)

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        if len(self.heap) == 0:
            return self.default
        else:
            return -heapq.heappop(self.heap)


def solve(X: int, Y: int, A: int, B: int, C: int, p: "List[int]", q: "List[int]", r: "List[int]"):
    p.sort()
    p = p[-X:]
    q.sort()
    q = q[-Y:]

    h = sorted(p+q+r)
    print(sum(h[-X-Y:]))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    q = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    r = [int(next(tokens)) for _ in range(C)]  # type: "List[int]"
    solve(X, Y, A, B, C, p, q, r)


if __name__ == '__main__':
    main()
