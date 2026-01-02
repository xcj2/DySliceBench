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
    for i in range(1, n+1):
        res.append(res[i-1]*i % DVSR)
    return res


N = II()
AS = LI()
DP = {}
DP[(0, 0)] = 0

mm = -(10**18)
for i in range(N):
    NX = {}
    for ((cnt, isUsed), value) in DP.items():
        if isUsed:
            if cnt >= (i // 2 - 5):
                NX[(cnt, 0)] = max(value, NX.get((cnt, 0)) or mm)
        else:
            if cnt >= (i // 2 - 5):
                NX[(cnt, 0)] = max(value, NX.get((cnt, 0)) or mm)
            if cnt >= (i // 2 - 5):
                NX[(cnt+1, 1)] = max(value + AS[i],
                                     NX.get((cnt+1, 1)) or mm)
    DP = NX
    # print(NX)

res = -(10**18)
for ((cnt, _), value) in DP.items():
    if cnt == N//2:
        res = max(res, value)
print(res)
