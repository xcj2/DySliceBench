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
# from collections import deque, defaultdict
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

# from fractions import gcd
from math import gcd
# def lcm(x, y):
#   return x // gcd(x, y) * y

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

def solve():
    N = II()
    A = LI()
    mx = max(A)
    A = sorted(A, reverse=True)
    # print(A)
    g = A[0]
    flag_pc = True
    F = [0] * (mx+1)
    ff = True
    for a in A:
        g = gcd(g, a)
        # print(g)
        if g != 1:
            flag_pc = False
        
        # print(a)
        if F[a] > 0 and a != 1:
            ff = False

        if ff:
            for j in range(1, int(a**0.5)+1):
                if a % j == 0:
                    if F[j] > 0 and j != 1:
                        ff = False
                        break
                    F[j] += 1

                    if j != (a//j):
                        if F[a//j] > 0 and (a//j) != 1:
                            ff = False
                            break
                        F[a//j] += 1
    # print(F)
    # print(ff)

    if g == 1:
        if ff:
            print('pairwise coprime')
        else:
            print('setwise coprime')
    else:
        print('not coprime')


if __name__ == '__main__':
    solve()

