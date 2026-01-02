import bisect
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
def init_dp1(init, N): return [init for _ in range(N)]
def init_dp2(init, N, M): return [[init for _ in range(M)] for _ in range(N)]


class V:
    def __init__(self, f, v=None):
        self.f = f
        self.v = v
 
    def __str__(self):
        return str(self.v)
 
    def ud(self, n):
        if n is None:
            return

        if self.v is None:
            self.v = n
            return
        self.v = self.f(self.v, n) 


def functional(N):
    F = [1] * (N + 1)
    for i in range(N):
        F[i + 1] = (i + 1) * F[i] % mod
    return F

D = {}
def inv(a):
    if a in D:
        return D[a]
    
    d = pow(a, mod - 2, mod)
    D[a] = d
    return d


def C(F, a, b):
    return F[a] * inv(F[a - b]) * inv(F[b]) % mod 


def main():
    N, M, K = read_values()
    F = functional(N)
 
    res = 0
    for k in range(K + 1):
        res += M * pow(M - 1, N - 1 - k, mod) * C(F, N - 1, k) % mod
        res %= mod
 
    print(res % mod)


if __name__ == "__main__":
    main()

