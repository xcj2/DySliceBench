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


class BIT:
    def __init__(self, N):
        self.N = N
        self.T = [0] * (N + 1)

    def add(self, i, x):
        i += 1
        while i <= self.N:
            self.T[i] += x
            i += i & -i

    def _sum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.T[i]
            i -= i & -i
        return s

    def sum(self, i, j):
        si = self._sum(i - 1)
        sj = self._sum(j)
        return sj - si
    

def main():
    N, M = read_values()
    C = read_list()
    Q = []
    for i in range(M):
        l, r = read_index()
        Q.append((l, r, i))
    Q.sort(key=lambda a: a[1])

    ans = [0] * M
    T = [-1] * M
    bit = BIT(N)
    q = 0
    # print(Q)
    for i in range(N):
        c = C[i] - 1
        t = T[c]
        if t != -1:
            bit.add(t, -1)
        T[c] = i
        bit.add(i, 1)

        # print(i, T, bit.T)
        while q < len(Q) and i == Q[q][1]:
            l, r, k = Q[q]
            ans[k] = bit.sum(l, r)
            q += 1

    print("\n".join(map(str, ans))) 

  
if __name__ == "__main__":
    main()
