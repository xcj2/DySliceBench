import sys
import math
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res
def gcd(x, y):
    if x < y: x, y = y, x
    div = x % y
    while div != 0:
        x, y = y, div
        div = x % y
    return y


N,Q=LI()
TR=[[] for i in range(N+1)]
TR_score = [0] * (N+1)
RES = [-1]*(N+1)

for i in range(N-1):
    i,j=LI()
    TR[i].append(j)
    TR[j].append(i)

for i in range(Q):
    p, x = LI()
    TR_score[p] += x

ST = [(1, TR_score[1])]
while ST:
    i, score = ST.pop()
    RES[i] = score
    for j in TR[i]:
        if RES[j] == -1:
            ST.append((j, score + TR_score[j]))

for value in RES[1:-1]: print(value, end=" ")
print(RES[-1])
