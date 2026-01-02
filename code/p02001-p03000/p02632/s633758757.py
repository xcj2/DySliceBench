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
    K = int(input())
    S = input().strip()

    F25 = [1] * (K + 2)
    F26 = [1] * (K + 2)
    T = [1] * (K + 2)
    for i in range(K + 1):
        F25[i + 1] = (25 * F25[i]) % mod
        F26[i + 1] = (26 * F26[i]) % mod
        if i != 0:
            T[i] = pow(i, mod - 2, mod)

    r = 1
    res = 0
    for k in range(K + 1):
        res += ((F25[k] * F26[K - k]) % mod * r) % mod
        r *= (len(S) - 1 + k + 1)
        r %= mod
        r *= T[k + 1]
        r %= mod
        res %= mod
     
    print(res)


if __name__ == "__main__":
    main()

