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

def solve():
    N, K = MI()
    # A = LI1()

    D = [[0] * N for _ in range(int(log2(K))+1)]
    D[0] = LI1()
    
    for i in range(1, int(log2(K))+1):
        for j in range(N):
            tmp = D[i-1][j]
            D[i][j] = D[i-1][tmp]
    # print(D)
    
    v = 0
    while K > 0:
        tmp = int(log2(K))
        K = K - 2 ** tmp
        v = D[tmp][v]
        # print(tmp, K, v)
    print(v+1)

if __name__ == '__main__':
    solve()
