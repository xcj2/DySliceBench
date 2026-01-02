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
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

N,K = LI()
AS=LI()
AS.sort(reverse=True)
res = 1
if AS[0] >= 0 and AS[N-1] >= 0:
    for i in range(K):
        res *= AS[i]
        res %= DVSR
elif AS[0] > 0:
    if N != K:
        PS = []
        NS = []
        for i in AS:
            if i >= 0:
                PS.append(i)
            else:
                NS.append(-i)
        PS.sort(reverse=True)
        NS.sort(reverse=True)
        i = 0
        j = 0

        for k in range(K):
            if i < len(PS) and j < len(NS):
                if PS[i] > NS[j]:
                    res *= PS[i]
                    i += 1
                else:
                    res *= NS[j]
                    j += 1
            else:
                if i < len(PS):
                    res *= PS[i]
                    i += 1
                else:
                    res *= NS[j]
                    j += 1
            res %= DVSR
            # print(res)
        # print("i:{} j:{}".format(i, j))
        if j % 2:
            if j < len(NS) and i < len(PS) and i > 0 and j > 0:
                if NS[j]*NS[j-1] > PS[i-1]*PS[i]:
                    res *= INV(PS[i-1])
                    res %= DVSR
                    res *= NS[j]
                    j += 1
                else:
                    res *= INV(NS[j-1])
                    res %= DVSR
                    res *= PS[i]
                    i += 1
            else:
                if j < len(NS) and i > 0:
                    res *= INV(PS[i-1])
                    res %= DVSR
                    res *= NS[j]
                    j += 1
                else:
                    res *= INV(NS[j-1])
                    res %= DVSR
                    res *= PS[i]
                    i += 1
            res %= DVSR
            # print(res)
    else:
        for i in range(N):
            res *= AS[i]
            res %= DVSR
else: # AS[0] <= 0
    if K % 2:
        v1 = 1
        v2 = 1
        for i in range(K):
            v1 *= AS[i]
            v1 %= DVSR
        res = v1
    else:
        res = 1
        for i in range(N-K, N):
            res *= AS[i]
            res %= DVSR

print(res%DVSR)
