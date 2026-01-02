import sys
from collections import deque
from functools import lru_cache
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
    N, K = read_values()
    P = [tuple(read_values()) for _ in range(N)]

    X = sorted([x for x, _ in P])
    Y = sorted([y for _, y in P])

    res = 10 ** 20
    for xl in range(N):
        for xr in range(xl + 1, N):
            for yl in range(N):
                for yr in range(yl + 1, N):
                    k = sum(X[xl] <= x <= X[xr] and Y[yl] <= y <= Y[yr] for x, y in P)
                    # print(f"X[{xl}, {xr}], Y[{yl}, {yr}] -> k:{k}")
                    if K <= k:
                        res = min(res, (X[xr] - X[xl]) * (Y[yr] - Y[yl]))
    print(res)



if __name__ == "__main__":
    main()

