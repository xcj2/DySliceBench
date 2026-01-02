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


N,K=LI()
MP=[0] + LI()
LG = 10**15
DP=[[LG]*(N+1) for i in range(N-K+2)]

for i in range(1, N+1):
    DP[0][i] = 0
    DP[1][i] = MP[i]

for i in range(1, N-K):
    for j in range(1, N+1):
        for k in range(1, j):
            DP[i+1][j] = min(DP[i+1][j], DP[i][k] + max(0, MP[j] - MP[k]))

res = 10**15
for i in range(1, N+1):
    res = min(res, DP[N-K][i])
print(res)
