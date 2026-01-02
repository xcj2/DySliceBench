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
    S = LS()

    R = []
    G = []
    B = []
    for i, s in enumerate(S):
        if s == 'R':
            R.append(i)
        elif s == 'G':
            G.append(i)
        else:
            B.append(i)

    len_r = len(R)
    len_g = len(G)
    len_b = len(B)

    def g(lst, r,  j):
        l = -1
        while r - l > 1:
            m = (l + r) // 2
            if lst[m] <= j:
                l = m
            else:
                r = m
        return r


    def f(lst, r, out):
        l = -1
        while r - l > 1:
            m = (r + l) // 2
            if out < lst[m]:
                r = m
            elif out > lst[m]:
                l = m
            else:
                return True
        return False

    ans = 0
    for i in range(N):
        si = S[i]
        for j in range(i+1, N):
            sj = S[j]
            if si == sj: continue
            out = j + j - i
            # print(i, j, si, sj, out)
            if si == 'R':
                if sj == 'G':
                    # B
                    k = g(B, len_b, j)
                    # print(k)
                    ans += len_b - k
                    if f(B, len_b, out):
                        ans -= 1
                elif sj == 'B':
                    # G
                    k = g(G, len_g, j)
                    ans += len_g - k
                    if f(G, len_g, out):
                        ans -= 1
            elif si == 'G':
                if sj == 'R':
                    # B
                    k = g(B, len_b, j)
                    ans += len_b - k
                    if f(B, len_b, out):
                        ans -= 1
                elif sj == 'B':
                    # R
                    k = g(R, len_r, j)
                    ans += len_r - k
                    if f(R, len_r, out):
                        ans -= 1
            elif si == 'B':
                if sj == 'R':
                    # G
                    k = g(G, len_g, j)
                    ans += len_g - k
                    if f(G, len_g, out):
                        ans -= 1
                elif sj == 'G':
                    # R
                    k = g(R, len_r, j)
                    ans += len_r - k
                    if f(R, len_r, out):
                        ans -= 1
    print(ans)




if __name__ == '__main__':
    solve()
