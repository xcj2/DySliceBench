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
    X, Y, Z, K = read_values()
    A = read_list()
    B = read_list()
    C = read_list()

    AB = sorted([a + b for a in A for b in B], reverse=True)
    C.sort()

    P = []
    for c in C:
        heapq.heappush(P, (-(c + AB[0]), 0))
    
    for _ in range(K):
        s, i = heapq.heappop(P)
        print(-s)
        if i + 1 < len(AB):
            heapq.heappush(P, (s + (AB[i] - AB[i + 1]), i + 1))


if __name__ == "__main__":
    main()

