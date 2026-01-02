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

N,M=LI()
As=LI()
As.sort()
len_As = len(As)
Acum=[As[0]]
for i in range(1, len_As):
    Acum.append(Acum[i-1]+As[i])
# print(As)
# print(Acum)

ok = 0
ng = 2*max(As)+1

pat = 0
sm = 0
while ng - ok > 1:
    mid_sum = (ok + ng)//2
    pat = 0
    sm = 0
    for A in As:
        A2 = mid_sum - A
        # print(A2)
        lft = bisect.bisect_left(As, A2)
        pat += len_As - lft
        sm += Acum[len_As-1] - (lft and Acum[lft-1]) + (len_As - lft)*A
    # print(pat, M, ok, ng)

    if pat < M: ng = mid_sum
    else: ok = mid_sum

pat = 0
sm = 0
for A in As:
    A2 = ok - A
    # print(A2)
    lft = bisect.bisect_left(As, A2)
    pat += len_As - lft
    sm += Acum[len_As-1] - (lft and Acum[lft-1]) + (len_As - lft)*A

# print("lo:{} hi:{} pat:{} sum:{}".format(ok, ng, pat, sm))

print(sm - (pat-M)*ok)
