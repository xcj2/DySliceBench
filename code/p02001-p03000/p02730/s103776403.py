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

S = input()

def isKaibun(S):
    flag = True

    for i in range(len(S)):
        if S[i] != S[len(S) - i - 1]:
            flag = False
    
    return flag

N = len(S)
print("Yes" if (isKaibun(S) and isKaibun(S[0 : int((N-1)/2)]) and isKaibun(S[int((N+3)/2)-1 : N])) else "No")
