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
    S = sRaw()
    nRGB = [sum([1 for c in S if c == C]) for C in "RGB"]
    zen = nRGB[0]*nRGB[1]*nRGB[2]

    ans = 0
    ho = 0
    for a in range(1,N):
        c2 = S[a]
        for r in range(1,a+1):
            if a+r >= N:
                continue
            c1 = S[a-r]
            c3 = S[a+r]
            if c1!=c2 and c2!=c3 and c1!=c3:
                ho+=1             
    return zen-ho

if __name__ == "__main__":
    print(main())
