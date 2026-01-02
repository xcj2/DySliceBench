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

A, B, C, D = LI()

flag = False
for i in range(1000):
    if i % 2 == 0:
        C -= B
    else:
        A -= D

    if A <= 0:
        flag = False
        break
    elif C <= 0:
        flag = True
        break

YesNo(flag)
