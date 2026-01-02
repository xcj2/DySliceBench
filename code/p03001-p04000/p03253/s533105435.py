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

def ncr(n, r, p=MOD):
    a = 1
    b = 1
    for i in range(r):
        a = (a * (n - i) % p)
        b = (b * (r - i) % p)

    return a * pow(b, p - 2, p) % p

N, M = LI()

i = 1
ans = 1
while i * i <= M:
    i += 1

    if M % i == 0:
        cnt = 0
        while M % i == 0:
            cnt += 1
            M //= i
        
        ans = ans * ncr(cnt+(N-1), (N-1)) % MOD

if M != 1:
    ans = ans * ncr(1+(N-1), (N-1)) % MOD

print(ans)
