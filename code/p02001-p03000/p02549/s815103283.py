import bisect
from collections import deque
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
# mod = 10 ** 9 + 7
mod = 998244353

def read_values(): return map(int, input().split())
def read_index(): return map(lambda x: int(x) - 1, input().split())
def read_list(): return list(read_values())
def read_lists(N): return [read_list() for n in range(N)]


class BIT:
    def __init__(self, N):
        self.N = N
        self.T = [0] * (N + 1)
 
    def add(self, i, x):
        i += 1
        while i <= self.N:
            self.T[i] += x
            self.T[i] %= mod
            i += i & -i
 
    def _sum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.T[i]
            s %= mod
            i -= i & -i
        return s % mod
 
    def sum(self, i, j):
        si = self._sum(i - 1)
        sj = self._sum(j)
        return (sj - si) % mod


def main():
    N, K = read_values()
    F = read_lists(K)

    bit = BIT(N)
    bit.add(0, 1)
    for i in range(1, N):
        s = 0
        for l, r in F:
            if i - l < 0:
                continue
            c = bit.sum(max(0, i - r), i - l)
            # print(i, i - r, i - l, c)
            s += c
        # print(s)
        bit.add(i, s)
        # print([bit.sum(i, i) for i in range(N)]) 
    print(bit.sum(N - 1, N - 1) % mod)


if __name__ == "__main__":
    main()