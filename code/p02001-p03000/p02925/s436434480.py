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
MATCHES = [[(0,0) for _ in range(N-1)] for _ in range(N)]

for i in range(N):
    lis = LI()
    for j in range(N-1):
        if i+1 < lis[j]:
            MATCHES[i][j] = (i+1, lis[j])
        else:
            MATCHES[i][j] = (lis[j], i+1)

CONT = True
IDXS=[0]*N
days = 0
ST=set()

next_check = range(N)
while CONT:
    cont = False
    _next_check = []
    for i in next_check:
        if IDXS[i] < N-1:
            pair = MATCHES[i][IDXS[i]]
            p, q = pair
            if pair in ST:
                ST.remove(pair)
                # print("{}: {}".format(days, pair))
                if IDXS[i] < N-1:
                    IDXS[p-1] += 1
                    IDXS[q-1] += 1
                    cont = True
                    _next_check.append(p-1)
                    _next_check.append(q-1)
            else:
                ST.add(pair)
    next_check = _next_check
    CONT = cont
    days += cont

# print(IDXS)
if sum(IDXS) == N*(N-1):
    print(days)
else:
    print(-1)
