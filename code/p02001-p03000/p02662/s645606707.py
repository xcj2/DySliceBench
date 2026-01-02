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

N,S=LI()
DP = [[0 for i in range(S+1)] for j in range(N+1)]
LIS=LI()
DP[0][0]=1
for i in range(N):
    v = LIS[i]
    for j in range(S+1):
        if j-v >= 0:
            DP[i+1][j] = (2*DP[i][j] + DP[i][j-v])%DVSR
        else:
            DP[i+1][j] = (2*DP[i][j])%DVSR

print(DP[N][S])
