import math
import sys
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

N,T=LI()
lis=[tuple(LI()) for i in range(N)]
lis.sort()
RES=[[0]*(T+1) for i in range(N+1)]
for i in range(1, N+1):
    A, B = lis[i-1]
    for t in range(T):
        if (t-A >= 0):
            RES[i][t] = max(RES[i-1][t], RES[i-1][t-A]+B)
        else:
            RES[i][t] = RES[i-1][t]
    RES[i][T] = max(RES[i-1][T], RES[i-1][T-1]+B)

print(RES[i][T])
