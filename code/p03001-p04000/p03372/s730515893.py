import sys
from collections import deque
from functools import lru_cache
import bisect
import copy
import heapq
import itertools
import math
import random
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N, C = read_values()
    D = read_lists(N)
    A = [0] * (N + 1)
    A2 = [0] * (N + 1)
    V = 0
    res = 0
    for i, (X, v) in enumerate(D):
        V += v
        A[i + 1] = max(A[i], V - X)
        A2[i + 1] = max(A2[i], V - 2 * X)
        res = max(res, A[i + 1], A2[i + 1])

    V = 0
    for b in range(N - 1, -1, -1):
        x, v = D[b]
        X = C - x
        V += v
        res = max(res, V - 2 * X + A[b], V - X + A2[b])

    print(res)


if __name__ == "__main__":
    main()

