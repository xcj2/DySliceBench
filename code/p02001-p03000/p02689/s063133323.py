# coding: utf-8

import sys
import math
import collections
import itertools
import bisect
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

N, M = LI()
H = LI()
AB = LRI(M)

HS = [True] * N
for a, b in AB:
    if H[a-1] < H[b-1]:
        HS[a-1] = False
    elif H[a-1] > H[b-1]:
        HS[b-1] = False
    if H[a-1] == H[b-1]:
        HS[a-1] = False
        HS[b-1] = False

ans = 0
for hs in HS:
    if hs:
        ans += 1

print(ans)
