import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
from functools import lru_cache
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 998244353

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


def main():
    N = int(input())
    A = read_list()
    Q = int(input())

    D = dict()
    for a in A:
        D[a] = D.setdefault(a, 0) + 1
    res = [""] * Q
    S = sum(A)
    for q in range(Q):
        B, C = read_values()
        S += (C - B) * D.setdefault(B, 0)
        D[C] = D.setdefault(C, 0) + D[B]
        D[B] = 0
        res[q] = str(S)
    print("\n".join(res))


if __name__ == "__main__":
    main()

