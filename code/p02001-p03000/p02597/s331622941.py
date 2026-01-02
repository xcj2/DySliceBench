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
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    N = II()
    C = LS()

    j = N-1
    cnt = 0
    # print(C)
    for i in range(N):
        if i >= j: break
        ci = C[i]
        if ci == 'W':
            # change
            # print(i, j)
            for k in range(j, i, -1):
                j = k-1
                ck = C[k]
                if ck == 'R':
                    # print(i, j)
                    # C[i], C[k] = ck, ci
                    cnt += 1
                    break

    # print(C)
    print(cnt)


if __name__ == '__main__':
    solve()
