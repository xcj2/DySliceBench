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

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

def prime_factorization(n, res):
    for i in range(2, int(pow(n, 0.5))+1):
        if n % i: continue
        ex = 0
        while n % i == 0:
            n = n // i
            ex += 1
        res[i] = res.get(i, 0) + ex
    if n != 1:
        res[n] = res.get(n, 0) + 1
    return res

def solve():
    N = II()

    # print(make_divisors(120))
    memo = {}
    for i in range(1, N+1):
        memo = prime_factorization(i, memo)

    # print(memo)

    def e(num):
        res = 0
        for v in memo.values():
            if v >= num:
               res += 1
        return res

    ans = 0
    # 2 * 4 * 4
    ans += e(4) * (e(4) - 1) * (e(2) - 2) // 2


    # 4 * 14
    ans += (e(4) - 1) * e(14)

    # 2 * 24
    ans += (e(2) - 1) * e(24)

    # 74
    ans += e(74)

    print(ans)



if __name__ == '__main__':
    solve()
