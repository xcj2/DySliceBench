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


def f(N, E, memo):
    if N == 0:
        return 0
    
    if N == 1:
        return E[-1]

    if N in memo:
        return memo[N]

    res = N * E[-1]
    for k in (2, 3, 5):
        l = (N // k) * k
        r = ((N - 1) // k + 1) * k

        res = min(res, (N - l) * E[-1] + E[k] + f(l // k, E, memo))
        res = min(res, (r - N) * E[-1] + E[k] + f(r // k, E, memo))
    memo[N] = res
    return res
   

def main():
    T = int(input())
    for _ in range(T):
        N, A, B, C, D = read_values()
        E = (0, 0, A, B, 0, C, D)
        memo = dict()
        print(f(N, E, memo))


if __name__ == "__main__":
    main()

