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

N, K = LI()
A = LI()

D = 60
to = [[-1] * N for _ in range(D)]
to[0] = [a-1 for a in A]

for i in range(D-1):
    for j in range(N):
        to[i+1][j] = to[i][to[i][j]]

now = 0
time = 0
while K > 0:
    if K&1:
        now = to[time][now]
    
    K >>= 1
    time += 1

print(now+1)
