import sys
import math
import heapq
import bisect
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

# j - i == S[j] - S[i] # MOD K
# S[i] - i == S[j] - j

N,K=LI()
As=LI()

Cum=[0]*(N+1)
for i in range(N):
    Cum[i+1] = Cum[i] + As[i]

REM2IDX = {}
for i in range(0,N+1):
    rem = (Cum[i] - i) % K
    if not rem in REM2IDX: REM2IDX[rem] = []
    REM2IDX[rem].append(i)

res = 0
for i in range(0,N+1):
    rem = (Cum[i] - i) % K
    cnt = len(REM2IDX[rem])
    l = bisect.bisect_right(REM2IDX[rem], i)
    r = bisect.bisect_right(REM2IDX[rem], i+K-1)
    res += (r-l)

print(res)
