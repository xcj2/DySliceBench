import bisect
import sys
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


def main():
    N, A, B, C = isRaw()
    AB = A+B
    AC = A+C
    BC = B+C
    ans = []
    Ss = [sRaw() for n in range(N)]
    
    for n in range(N):
        s = Ss[n]
        if s == "AB":
            if AB == 0:
                print("No")
                return
            if AC > BC:
                ans.append("B")
                AC -= 1
                BC += 1
            elif AC < BC:
                ans.append("A")
                AC += 1
                BC -= 1
            else:
                if n+1!=N and Ss[n+1]=="AC":
                    ans.append("A")
                    AC += 1
                    BC -= 1
                else:
                    ans.append("B")
                    AC -= 1
                    BC += 1
        if s == "AC":
            if AC == 0:
                print("No")
                return
            if AB > BC:
                ans.append("C")
                AB -= 1
                BC += 1
            elif AB < BC:
                ans.append("A")
                AB += 1
                BC -= 1
            else:
                if n+1 != N and Ss[n+1] == "AB":
                    ans.append("A")
                    AB += 1
                    BC -= 1
                else:
                    ans.append("C")
                    AB -= 1
                    BC += 1
        if s == "BC":
            if BC == 0:
                print("No")
                return
            if AB > AC:
                ans.append("C")
                AB -= 1
                AC += 1
            elif AB < AC:
                ans.append("B")
                AB += 1
                AC -= 1
            else:
                if n+1 != N and Ss[n+1] == "AB":
                    ans.append("B")
                    AB += 1
                    AC -= 1
                else:
                    ans.append("C")
                    AB -= 1
                    AC += 1
    print("Yes")
    print("\n".join(ans))


if __name__ == "__main__":
    main()
