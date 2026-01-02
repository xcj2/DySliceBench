#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return input().rstrip()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float("inf")

#solve
def solve():
    a = S()
    b = S()
    c = S()
    def f(a, b, c):
        lena, lenb, lenc = len(a), len(b), len(c)
        dpab = [inf] * (lena + 1)
        dpbc = [inf] * (lenb + 1)
        dpac = [inf] * (lena + 1)
        for l in range(lena + 1):
            f = 0
            tl = l
            for r in range(lenb):
                if l == lena:
                    break
                if a[l] == b[r] or a[l] == "?" or b[r] == "?":
                    l += 1
                else:
                    f = 1
                    break
            if f:
                continue
            dpab[tl] = max(tl + lenb, lena)

        for l in range(lenb + 1):
            f = 0
            tl = l
            for r in range(lenc):
                if l == lenb:
                    break
                if b[l] == c[r] or b[l] == "?" or c[r] == "?":
                    l += 1
                else:
                    f = 1
                    break
            if f:
                continue
            dpbc[tl] = max(tl + lenc, lenb)

        for l in range(lena + 1):
            f = 0
            tl = l
            for r in range(lenc):
                if l == lena:
                    break
                if a[l] == c[r] or a[l] == "?" or c[r] == "?":
                    l += 1
                else:
                    f = 1
                    break
            if f:
                continue
            dpac[tl] = max(tl + lenc, lena)

        res = lena + lenb + lenc
        for l in range(lena + 1):
            for r in range(lenb + 1):
                lr = l + r
                if dpab[l] != inf and dpbc[r] != inf:
                    if lr > lena:
                        res = min(l + dpbc[r], res)
                    else:
                        if dpac[lr] != inf:
                            if dpbc[r] == lenb:
                                res = min(res, dpab[l])
                            else:
                                res = min(res, dpac[lr])
            for r in range(l + lenb, lena + 1):
                if dpab[l] == lena:
                    if dpac[r] != inf:
                        res = min(res, dpac[r])
        return res

    ans = len(a) + len(b) + len(c)
    ans = min(ans, f(a, b, c))
    ans = min(ans, f(a, c, b))
    ans = min(ans, f(b, a, c))
    ans = min(ans, f(b, c, a))
    ans = min(ans, f(c, b, a))
    ans = min(ans, f(c, a, b))
    print(ans)

    return


#main
if __name__ == '__main__':
    solve()
