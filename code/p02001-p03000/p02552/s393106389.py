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


class Comb:
    def __init__(self, N):
        F = [1] * (N + 1)
        for i in range(N):
            F[i + 1] = (i + 1) * F[i] % mod

        self.d_inv = {}
        self.d_comb = {}
        self.F = F

    def inv(self, a):
        if a not in self.d_inv:
            self.d_inv[a] = pow(a, mod - 2, mod)
        return self.d_inv[a]

    def comb(self, a, b):
        if (a, b) not in self.d_comb:
            self.d_comb[(a, b)] = (self.F[a] * self.inv(self.F[a - b]) * self.inv(self.F[b])) % mod
            self.d_comb[(a, a - b)] = self.d_comb[(a, b)]
        return self.d_comb[(a, b)] 



def main():
    print(1 - int(input()))

if __name__ == "__main__":
    main()

