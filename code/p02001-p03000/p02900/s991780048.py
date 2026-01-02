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
    P=[2]
    for L in range(3, n):
        isP = True
        for L2 in P: isP = isP and L%L2
        if isP: P.append(L)
    return P

A,B=LI()
gd = gcd(A,B)
if gd == 1:
    print(1)
    exit()

# print("gcd: {}".format(gd))
cands = []
prs = []

for i in range(2, math.ceil(math.sqrt(gd))+1):
    if gd%i == 0:
        cands.append(i)
        cands.append(gd//i)

cands.sort()
cands.append(gd)

for i in range(0, len(cands)):
    ok = True
    for prime in prs:
        if cands[i]%prime == 0:
            ok = False
            break
    if ok:
        prs.append(cands[i])

# print(prs)
print(len(prs)+ 1)
