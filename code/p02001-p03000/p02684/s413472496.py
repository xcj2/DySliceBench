import sys
sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def MS(): return input().split()
def LS(): return list(input())
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')
from math import ceil, floor, log2
# from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np
# from numpy import cumsum  # accumulate
class Doubling:
    def __init__(self, lst, max_step):
        self.lst = lst
        self.max_step = max_step
        self.k = int(log2(max_step * 2 - 1)) + 1
        # print(self.k)
        self.D = self.create()

    def create(self):
        len_ = len(self.lst)
        D = [[-1] * len_ for _ in range(self.k)]
        D[0] = self.lst
        d = 2
        for i in range(1, self.k):
            for j in range(len_):
                D[i][j] = D[i - 1][D[i - 1][j]]
            d *= 2
        # print(D)
        return D

    def step(self, start, step):
        v = start
        for i in range(self.k, -1, -1):
            l = 1 << i
            if l <= step:
                v = self.D[i][v]
                # print(i, l)
                step -= l
        return v

def solve():
    N, K = MI()
    A = LI1()

    db = Doubling(A, K)
    v = db.step(0, K)
    print(v+1)

if __name__ == '__main__':
    solve()
