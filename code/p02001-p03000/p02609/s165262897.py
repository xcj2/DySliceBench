import bisect
import sys
import math
from collections import deque
from heapq import heappush, heappop

def sRaw():
    return input().rstrip("\r")


def iRaw():
    return int(input())


def ssRaw():
    return input().split()


def isRaw():
    return list(map(int, ssRaw()))


INF = 1 << 29

DIV = (10**9) + 7
#DIV = 998244353

def mod_inv_prime(a, mod=DIV):
    return pow(a, mod-2, mod)


def mod_inv(a, b):
    r = a
    w = b
    u = 1
    v = 0
    while w != 0:
        t = r//w
        r -= t*w
        r, w = w, r
        u -= t*v
        u, v = v, u
    return (u % b+b) % b


def CONV_TBL(max, mod=DIV):
    fac, finv, inv = [0]*max, [0]*max, [0]*max
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, max):
        fac[i] = fac[i-1]*i % mod
        inv[i] = mod - inv[mod % i] * (mod//i) % mod
        finv[i] = finv[i-1]*inv[i] % mod

    class CONV:
        def __init__(self):
            self.fac = fac
            self.finv = finv
            pass

        def ncr(self, n, k):
            if(n < k):
                return 0
            if(n < 0 or k < 0):
                return 0
            return fac[n]*(finv[k]*finv[n-k] % DIV) % DIV

    return CONV()


def cumsum(As):
    s = 0
    for a in As:
        s += a
        yield s


sys.setrecursionlimit(200005)


def dijkstra(G,start=0):
    heap = []
    cost = [INF]*len(G)
    heappush(heap,(0,start))
    while len(heap)!=0:
        c,n = heappop(heap)
        if cost[n] !=INF:
            continue
        cost[n]=c
        for e in G[n]:
            ec,v = e
            if cost[v]!=INF:
                continue
            heappush(heap,(ec+c,v))
    return cost


def main():
    cache={"0":0}
    def get_pc(s):
        pc = sum([c == '1' for c in s])
        return pc

    def modPC(s,pc=None):
        if pc==None:
            pc =get_pc(s)
        return int(s,2)%pc

    def f(s,cur=0):
        if s in cache:
            return cache[s]
        next_s = bin(modPC(s))[2:]
        ret = f(next_s,cur+1)+1
        cache[s]=ret
        return ret
    N=iRaw()
    Xs=sRaw()
    XPC = get_pc(Xs)
    XmodPC=None
    if XPC!=0:
        XmodPC = modPC(Xs,XPC)
    XmodPCP = modPC(Xs,XPC+1)
    XmodPCN = None
    if XPC>1:
        XmodPCN= modPC(Xs,XPC-1)

    for n in range(N):
        if Xs[n]=='1':
            if XPC==1:
                print(0)
            else:
                nxt=(XmodPCN-pow(2,N-n-1,XPC-1))%(XPC-1)
                nxt = bin(nxt)[2:]
                print(f(nxt)+1)
        else:
            nxt = (XmodPCP+pow(2, N-n-1, XPC+1)) % (XPC+1)
            nxt = bin(nxt)[2:]
            print(f(nxt)+1)

main()
