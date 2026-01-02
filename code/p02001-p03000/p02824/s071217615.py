import bisect
import copy
import heapq
import sys
import itertools
import math
import queue
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7

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


def f(A, M, V, P, m):
    N = len(A)
    a = A[m]
    i = bisect.bisect_right(A, a + M)
    C = N - i

    if C >= P:
        return False

    C = P - 1
    i = N - C

    U = 0
    for j in range(i):
        if j == m:
            continue
        U += min(a + M - A[j], M)

    return U >= (V - 1 - C) * M


def main():
    N, M, V, P = read_values()
    A = read_list()
    A.sort()
    
    l = 0
    r = N
    while l < r:
        m = (r + l) // 2
        if f(A, M, V, P, m):
            r = m
        else:
            l = m + 1

    print(N - r)


if __name__ == "__main__":
    main()
