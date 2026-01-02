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
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res
def gcd(x, y):
    if x < y: x, y = y, x
    div = x % y
    while div != 0:
        x, y = y, div
        div = x % y
    return y

N,Q=LI()
HQ=[]
EVS=[]
for i in range(N):
    S,T,X=LI()
    EVS.append((S-0.5-X, 1, X))
    EVS.append((T-0.5-X, 0, X))
for i in range(Q):
    D=II()
    EVS.append((D, 2, D))
EVS.sort()

st=set()
PQ=[]
for time, ev, loc in EVS:
    if ev == 1:
        heapq.heappush(PQ, loc)
        st.add(loc)
    elif ev == 0:
        st.remove(loc)
    else:
        while PQ and PQ[0] not in st:
            heapq.heappop(PQ)
        if PQ:
            print(PQ[0])
        else:
            print(-1)
