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

N,M=LI()
BS=list(map(lambda x: x//2, LI()))

LCM=1
GCD=BS[0]
for i in range(N):
    LCM = LCM*BS[i]//gcd(LCM, BS[i])
    GCD = gcd(GCD, BS[i])

# print("LCM:{}".format(LCM))

if (LCM//GCD) % 2 == 0:
    print(0)
else:
    print(M//LCM//2 + (M//LCM)%2)
