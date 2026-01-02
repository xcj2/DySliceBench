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
# from math import ceil, floor, log2
# from collections import deque
from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np
# from numpy import cumsum  # accumulate

def solve():
    N, K = MI()
    A = LI()
    for i in range(K):
        B = [0] * N
        for idx, a in enumerate(A):
            l = max(0, idx - a)
            r = idx + a + 1
            # print(idx, a, l, r)
            B[l] += 1
            if N > r:
                B[r] -= 1
        # print(B)
        B = list(accumulate(B))
        # print(B)
        if all([j == N for j in B]):
            printlist(B)
            return
        A = B
    printlist(A)



if __name__ == '__main__':
    solve()
