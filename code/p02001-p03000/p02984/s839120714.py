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
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np
# from numpy import cumsum  # accumulate

def solve():
    N = II()
    A = LI()

    """
    A_i = (X_i + X_i+1) / 2 より
    2 * A_i = X_i + X_i+1
    
    また、答えのリストをXとすると、sum(A) == sum(X)　より
    X0 = sum(X) - (X1 + X2 + .. XN)
       = sum(A) - (2A1 + 2A3 + ... 2A_N-1)
       = sum(A) - 2 * (A1 + A3 + ... A_N-1)
    """
    sma = 0
    for i in range(1, N, 2):
        sma += A[i]

    ans = [-1] * N
    ans[0] = sum(A) - 2 * sma

    """
    X_i+1 = 2A_i - X_i 
    """
    for i in range(1, N):
        ans[i] = 2 * A[i-1] - ans[i-1]
    print(*ans)


if __name__ == '__main__':
    solve()
