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
from collections import deque, defaultdict
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    N, X, M = MI()
    def f(x): return x % M
    # N += 2

    ans = 0
    r = [0] * (M+1)
    p = 1
    q = 0
    pre = X
    # S = [0] * (N+1)
    # S[0] = X
    S = [X]
    for i in range(1, N):
        tmp = f(pre ** 2) % M
        # print(tmp)
        if r[tmp]:
            # print('aa', i, r[tmp])
            left = N - r[tmp]
            loop = i - r[tmp]
            # print(left, loop)
            p, q = left // loop, left % loop
            # print(p, q, S[i-1] - S[r[tmp]-1], i-1, r[tmp]-1)
            # print(S)
            ans = S[r[tmp]-1]
            ans += p * (S[i-1] - S[r[tmp]-1])
            if q > 0:
                ans += (S[r[tmp]+q-1] - S[r[tmp]-1])
            print(ans)
            # ans += S[]
            return 
        pre = tmp
        r[tmp] = i
        # S[i] = tmp + S[i-1]
        S.append(tmp + S[i-1])
    else:
        # print(S)
        print(S[N-1])



if __name__ == '__main__':
    solve()

