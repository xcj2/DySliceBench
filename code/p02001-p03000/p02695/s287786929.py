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

N, M, Q = LI()
ABCD = LRI(Q)

def calc(A):
    ret = 0

    for a, b, c, d in ABCD:
        if A[b] - A[a] == c:
            ret += d
    
    return ret

ans = 0
def dfs(A):
    global ans
    
    if len(A) == N+1:
        ans = max(ans, calc(A))
        return
    
    back = A[-1]
    while back <= M:
        dfs(A + [back])
        back += 1

dfs([1])

print(ans)
