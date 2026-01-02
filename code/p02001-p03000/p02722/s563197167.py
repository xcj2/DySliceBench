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

def divisor(N):
    res = []

    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i != 0:
            continue

        res.append(i)
        if i * i != N:
            res.append(N/i)
    
    return res

N = I()

ans = 0
for x in divisor(N):
    if x == 1:
        continue
    
    tmp = N
    while tmp % x == 0:
        tmp /= x
    tmp %= x

    if tmp == 1:
        ans += 1

ans += len(divisor(N-1)) - 1

print(ans)
