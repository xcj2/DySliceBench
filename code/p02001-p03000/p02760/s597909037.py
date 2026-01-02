# coding: utf-8

import sys
import math
import collections
import itertools
from inspect import currentframe
INF = 10 ** 10
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def gcd(x, y) : return y if x % y == 0 else gcd(y, x % y)
def lcm(x, y) : return (x * y) // gcd(x, y)
def I() : return int(input())
def MI() : return map(int, input().split())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def chkprint(*args) : names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}; print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

A = LRI(3)
N = I()
B = [b[0] for b in LRI(N)]

for i in range(3):
    for j in range(3):
        for b in B:
            if b == A[i][j]:
                A[i][j] = -1

flag = False
for i in range(3):
    if A[0][i] == -1 and A[1][i] == -1 and A[2][i] == -1:
        flag = True
    if A[i][0] == -1 and A[i][1] == -1 and A[i][2] == -1:
        flag = True

if A[0][0] == -1 and A[1][1] == -1 and A[2][2] == -1:
        flag = True
if A[0][2] == -1 and A[1][1] == -1 and A[2][0] == -1:
        flag = True

print("Yes" if flag else "No")