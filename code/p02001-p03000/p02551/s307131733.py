import sys
from collections import deque
import bisect
import copy
import heapq
import itertools
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N, M = read_values()
    Q = [tuple(read_index()) for _ in range(M)]
    S = [N - 1] * N
    T = [N - 1] * N
    W, H = N - 1, N - 1
    res = (N - 2) ** 2
    for d, x in Q:
        if d == 0:
            if x < W:
                for i in range(x, W):
                    S[i] = H
                W = x
            res -= S[x] - 1
        if d == 1:
            if x < H:
                for i in range(x, H):
                    T[i] = W
                H = x
            res -= T[x] - 1
    print(res)


if __name__ == "__main__":
    main()
