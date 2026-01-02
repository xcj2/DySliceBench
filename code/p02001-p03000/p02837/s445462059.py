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
DATA=[[] for i in range(N+1)]

for i in range(1, N+1):
    for _ in range(II()):
        DATA[i].append(LI())

res = 0
for FLGS in range(1 << N):
    ok = True
    for i in range(N):
        if (FLGS >> i) & 1:
            for j, k in DATA[i+1]:
                ok = ok and ((FLGS >> (j-1)) & 1) == k
                # print("j:{} FLGS >> (j-1):{} k:{}".format(j, FLGS >> (j-1), k))
    if ok:
        pos_res = 0
        for s in range(N): pos_res += (FLGS >> s) & 1
        res = max(res, pos_res)
        # print("{:015b}".format(FLGS))
print(res)
