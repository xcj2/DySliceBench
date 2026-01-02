import sys
import math
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 998244353
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

N,M,K=LI()
FACT=FLIST(N+M+1)
FINV=[]
for i in FACT: FINV.append(INV(i))
if N == 1:
    print(M)
    exit()
if M == 1:
    if N - 1 == K: print(M)
    else: print(0)
    exit()

res = 0
def ncr(n, r):
    res = 1
    res *= FACT[n]
    res *= FINV[n-r]
    res %= DVSR
    res *= FINV[r]
    res %= DVSR
    return res

for k in range(K+1):
    v = ncr(N-1, k)*M
    v %= DVSR
    v *= POW(M-1, N-1-k)
    v %= DVSR
    res += v

print(res%DVSR)
