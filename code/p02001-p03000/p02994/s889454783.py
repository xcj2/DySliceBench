# coding: utf-8

import sys
import math
import collections
import itertools
INF = 10 ** 10
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def gcd(x, y) : return y if x % y == 0 else gcd(y, x % y)
def lcm(x, y) : return (x * y) // gcd(x, y)
def I() : return int(input())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def PL(L) : print(*L, sep="\n")

N, L = LI()

A = [x for x in range(L, L+N)]
A.sort(key=lambda x : abs(x))

print(sum(A[1:]))
