# coding: utf-8

import sys
import math
import collections
import itertools
INF = 10 ** 13
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def lcm(x, y) : return (x * y) // math.gcd(x, y)
def I() : return int(input())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def LS() : return input().split()
def RS(N) : return [input() for _ in range(N)]
def LRS(N) : return [input().split() for _ in range(N)]
def PL(L) : print(*L, sep="\n")
def YesNo(B) : print("Yes" if B else "No")
def YESNO(B) : print("YES" if B else "NO")

def F(A, B, x):
    return math.floor(A*x / B) - A*math.floor(x / B)
# def F1(A, B, x):
#     return math.floor(A*x / B)
# def F2(A, B, x):
#     return A*math.floor(x / B)

A, B, N = LI()

# import matplotlib.pyplot as plt
# plt.plot(range(1, N+1), [F(A, B, y) for y in range(1, N+1)])
# plt.plot(range(1, N+1), [F1(A, B, y) for y in range(1, N+1)])
# plt.plot(range(1, N+1), [F2(A, B, y) for y in range(1, N+1)])
# plt.show()

if N < B:
    print(F(A, B, N))
else:
    print(F(A, B, B-1))
