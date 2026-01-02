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
def primes(n):
    P = [2]
    for L in range(3, n):
        isP = True
        for L2 in P:
            isP = isP and L%L2
            if not isP: break
        if isP: P.append(L)
    return P

N,K=LI()
num_red = N-K
FACT=FLIST(4000)

for i in range(1, K+1):
    num_barr = i-1
    if num_barr > num_red or i > K:
        print(0)
    else:
        pat_blue = (((FACT[K+num_barr-i] * INV(FACT[num_barr])) % DVSR) * INV(FACT[K-i])) % DVSR
        pat_red = ((FACT[num_red+1] * INV(FACT[num_barr+1]) % DVSR) * INV(FACT[num_red - num_barr])) % DVSR
        # print("pat_blue {}, pat_red {}".format(pat_blue, pat_red))
        print(pat_red*pat_blue%DVSR)
