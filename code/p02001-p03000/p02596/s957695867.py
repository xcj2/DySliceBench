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

def solve():
    K = II()
    one = int(list(str(K))[-1])
    if one % 2 == 0 or one == 5:
        print(-1)
        return

    cnt = 1
    first_k = 7
    while 1:
        if first_k >= K:
            break
        first_k = first_k * 10 + 7
        cnt = cnt + 1
    # print(first_k)

    q = first_k % K
    while 1:
        if q == 0:
            print(cnt)
            return
        q = (q * 10 + 7) % K
        cnt = cnt + 1


if __name__ == '__main__':
    solve()
