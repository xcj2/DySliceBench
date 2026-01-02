# coding: utf-8

import sys
import math
import collections
import itertools
import bisect
INF = 10 ** 13
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def gcd(x, y) : return x if y == 0 else gcd(y, x%y)
def lcm(x, y) : return (x * y) // gcd(x, y)
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

A, B = LS()
A = int(A)

B = B.split('.')
Ba = int(B[0])
Bb = int(B[1])

c = 0
Bb *= A
Bb = str(Bb)
if len(Bb) >= 3:
    c = int(Bb[0:len(Bb)-2])

print(A*Ba + c)
