#!/usr/bin/env python3
import sys
import itertools
import collections
import functools
import math
from queue import Queue
# import numpy as np
INF = float("inf")
import heapq


def solve(X: int, Y: int, Z: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    XYZ = [X, Y, Z]
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    ABC = [A, B, C]

    base = A[0]+B[0]+C[0]
    cand = [[0, 0, 0, 0]]
    heapq.heapify(cand)
    # print(cand)
    for i in range(K):
        a = heapq.heappop(cand)
        for j in range(1, 4):
            if a[j]+1 < XYZ[j-1]:
                b = [a[0]+ABC[j-1][a[j]]-ABC[j-1][a[j]+1],
                     a[1]+int(j == 1),
                     a[2]+int(j == 2),
                     a[3]+int(j == 3)]
                if b not in cand:
                    heapq.heappush(cand, b)
        # print(cand)
        print(base-a[0])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(X)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(Y)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(Z)]  # type: "List[int]"
    solve(X, Y, Z, K, A, B, C)


if __name__ == '__main__':
    main()
