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


def argmax(a):
    value, n = -(1 << 31), -1
    for i, v in enumerate(a):
        if value < v:
            n, value = i, v
    return n, value


def solve(X: int, Y: int, A: int, B: int, C: int, p: "List[int]", q: "List[int]", r: "List[int]"):
    ABC = [MaxHeap(p), MaxHeap(q), MaxHeap(r)]

    upper = [X, Y]

    abc = [k.pop() for k in ABC]
    xyz = [0, 0, 0]
    tot = 0
    for _ in range(X+Y):
        i, m = argmax(abc)
        tot += m
        if (i < 2 and xyz[i] < upper[i]-1) or (i == 2):
            abc[i] = ABC[i].pop()
        else:
            abc[i] = -INF
        xyz[i] += 1
    print(tot)
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
