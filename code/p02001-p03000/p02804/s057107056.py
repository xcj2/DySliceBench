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

N,K=LI()
AS=LI()
AS.sort()
FL=FLIST(N)
INV_FL=list(map(INV,FL))
K_2=K-2
N_1=N-1

if K == 1:
    print(0)
    exit()

# nC(k-2) の累積和
NCSUM=[0]*N
for i in range(K-2, N_1):
    # print("i:{} K-2:{} value:{}".format(i, K_2, (((FL[i]*INV_FL[i-K_2])%DVSR)*INV_FL[K_2])%DVSR))
    NCSUM[i+1] = (NCSUM[i] + (((FL[i]*INV_FL[i-K_2])%DVSR)*INV_FL[K_2])%DVSR )%DVSR

# print(NCSUM)

res = 0
# 最小値側
for i in range(N-K+1):
    res -= (NCSUM[N_1-i]-NCSUM[K_2])*AS[i]%DVSR
res %= DVSR

# 最大値側
for i in range(N-K+1):
    res += (NCSUM[N_1-i]-NCSUM[K_2])*AS[N_1-i]%DVSR
res %= DVSR
print(res)
