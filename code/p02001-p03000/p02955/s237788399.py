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

    M = sum(A)
    divs = []
    for i in range(1, int(pow(M, 0.5))+1):
        if M % i: continue
        divs.append(i)
        if i != M//i: divs.append(M//i)
    divs.sort(reverse=True)

    for d in divs:
        B = list(map(lambda x: x%d, A))
        B.sort()
        C = list(map(lambda x: d-x, B))
        # print(d, B, C)
        # print(list(accumulate(B)), list(accumulate(C)))
        Ba = list(accumulate(B))
        Ca = list(accumulate(C))
        for i in range(0, N-1):
            b = Ba[i]
            c = Ca[-1] - Ca[i]
            # print(b, c)
            if b == c and b <= K:
                print(d)
                return
    print(1)


if __name__ == '__main__':
    solve()
