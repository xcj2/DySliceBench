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
    H, W = MI()
    G = LLS(H)

    R = [[] for _ in range(H)]
    for i, row in enumerate(G):
        tmp = [0] * (W+1)
        cnt = 0
        flag = True
        idx = -1
        # print(row)
        for j, h in enumerate(row):
            if h == '#':
                if cnt > 0:
                    tmp[idx] = tmp[idx] + cnt
                    tmp[j] = tmp[j] - cnt
                    cnt = 0
                    flag = True
            else:
                if flag:
                    idx = j
                    flag = False
                cnt = cnt + 1
        if cnt > 0:
            tmp[idx] = tmp[idx] + cnt
            tmp[-1] = - cnt

        # print(tmp)
        # print(*accumulate(tmp))
        R[i] = list(accumulate(tmp))
    # print(R)

    ans = -1
    for i in range(W):
        tmp2 = [0] * (H+1)
        cnt = 0
        flag2 = True
        idx = -1
        for j in range(H):
            d = G[j][i]
            if d == '#':
                if cnt > 0:
                    tmp2[idx] = cnt
                    tmp2[j] = - cnt
                    cnt = 0
                    flag2 = True
            else:
                if flag2:
                    idx = j
                    flag2 = False
                cnt = cnt + 1
        if cnt > 0:
            tmp2[idx] = cnt
            tmp2[-1] = - cnt
        # print(tmp2)
        # print(*accumulate(tmp2))
        for j, a in enumerate(list(accumulate(tmp2))[:-1]):
            ans = max(ans, R[j][i] + a - 1)

    print(ans)



if __name__ == '__main__':
    solve()
