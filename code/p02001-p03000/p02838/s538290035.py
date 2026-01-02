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

N=II()
As=LI()

DIG_CUM = [[0]*60 for _ in range(N+1)]

for i in range(N):
    for s in range(60):
        DIG_CUM[i+1][s] = DIG_CUM[i][s] + ((As[i] >> s) & 1)

# for arr in DIG_CUM:
#     print(arr)
POW2 = [1]
for i in range(60): POW2.append(POW2[i]*2%DVSR)

res = 0
for i in range(N-1):
    for s in range(60):
        coef = DIG_CUM[N][s] - DIG_CUM[i+1][s]
        if (As[i] >> s) & 1: coef = N - i - 1 - coef
        res += coef * POW2[s]
    res %= DVSR
print(res)
