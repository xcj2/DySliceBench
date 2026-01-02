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

def SMI(): return input().split()
def SLI(): return list(input())

def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')

# from math import ceil, floor, log2
# from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np
# from numpy import cumsum  # accumulate

def solve():
    D, G = MI()
    P = []
    C = []
    for _ in range(D):
        p, c = MI()
        P.append(p)
        C.append(c)

    ans = INF
    for i in range(1 << D):
        bag = []
        cag = []
        for j in range(D):
            if (i >> j) & 1:
                bag.append(j)
            else:
                cag.append(j)
        # print(bag, cag)
        score = 0
        cnt = 0
        for b in bag:
            score += (b+1) * 100 * P[b] + C[b]
            cnt += P[b]
        # print(score, cnt, G)
        if score >= G:
            ans = min(ans, cnt)
            # print('a', ans)
        else:
            c = cag[-1]
            for i in range(P[c]):
                score += (c+1) * 100
                cnt += 1
                if score >= G:
                    ans = min(ans, cnt)
                    # print(ans)
                    break

    print(ans)


if __name__ == '__main__':
    solve()
