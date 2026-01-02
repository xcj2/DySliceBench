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
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

K=II()
S=input()
L=len(S)
FACT=FLIST(K+L)
def NCR(n, r):
    res = FACT[n-r]
    res *= FACT[r]
    res %= DVSR
    res = INV(res)
    res *= FACT[n]
    res %= DVSR
    return res

ans = 0
for i in range(K+1):
    v = NCR(L+K-i-1, L-1)
    v *= POW(25, K-i)
    v %= DVSR
    v *= POW(26, i)
    v %= DVSR
    ans += v

print(ans % DVSR)
