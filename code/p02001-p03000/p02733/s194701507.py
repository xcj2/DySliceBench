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

def check(j):
    global cur

    for i in range(g):
        cur[i] += c[i][j]

    flag = True
    for curr in cur:
        if curr > K:
            flag = False

    return flag

H, W, K = LI()
S = RS(H)

ans = INF
N = H-1
for bit in range(1 << N):
    g = 0
    id = [0] * H

    for i in range(H):
        id[i] = g
        if (bit >> i) & 1:
            g += 1

    g += 1    
            
    c = [[0] * W for _ in range(g)]
    for i in range(H):
        for j in range(W):
            c[id[i]][j] += int(S[i][j])

    num = g-1
    cur = [0] * g
    for i in range(W):
        if not check(i):
            num += 1
            cur = [0] * g

            if not check(i):
                num = INF
                break
    
    ans = min(ans, num)

print(ans)
