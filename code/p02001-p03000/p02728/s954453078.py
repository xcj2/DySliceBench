import bisect,sys
import math
from collections import deque

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
            self.fac =fac
            self.finv = finv
            pass

        def ncr(self, n, k):
            if(n < k):
                return 0
            if(n < 0 or k < 0):
                return 0
            return fac[n]*(finv[k]*finv[n-k] % DIV) % DIV
        
    return CONV()



sys.setrecursionlimit(200005)


def main():
    N = iRaw()
    G = [[] for _ in range(N)]
    dp = [0]*N
    sizs = [0]*N
    CONV = CONV_TBL(N+1)

    for _ in range(N-1):
        a,b = isRaw()
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    
    def dfs(cur, pre):
        val = 1
        siz = 0
        for v in G[cur]:
            if v == pre:
                continue
            dfs(v, cur)
            siz += sizs[v]
            val = val * dp[v] * CONV.ncr(siz, sizs[v]) % DIV
        dp[cur] = val
        sizs[cur] = siz + 1
    
    def reroot(cur,pre):
        for v in G[cur]:
            if v == pre:
                continue
            val = dp[cur] * sizs[v]%DIV
            #val = val * CONV.fac[sizs[v]] * CONV.finv[sizs[v]-1]%DIV
            res = sizs[0]-sizs[v]
            dp[v] = val * CONV.finv[res] * CONV.fac[res-1] %DIV
            reroot(v,cur)
    
    dfs(0,-1)
    reroot(0,-1)
    return "\n".join([str(d) for d in dp])

if __name__ == "__main__":
    print(main())
