#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007

#A
def A():
    a, b, c = LI()
    if a + b >= c:
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    n = II()
    s = SR(n)
    m = II()
    t = SR(m)
    ans = 0
    for si in s:
        ans = max(ans, s.count(si) - t.count(si))
    print(ans)
    return

#C
def C():
    n = II()
    ab = LIR(n)
    cd = LIR(n)
    ab.sort()
    cd.sort()
    check = [0 for i in range(n)]
    ans = 0
    for _, c in enumerate(cd):
        d = c[1]
        c = c[0]
        maxy = -1
        x = -1
        for k, a in enumerate(ab):
            b = a[1]
            a = a[0]
            if maxy < b and c > a and check[k] == 0 and d > b:
                maxy = b
                x = k
        if x != -1:
            ans += 1
            check[x] += 1
    print(ans)


    return

#D
def D():
    N = II()
    a = LI()
    b = LI()
    ans = 0
    for i in range(29):
        t = 2 ** i
        a2 = [A % (2 * t) for A in a]
        b2 = [B % (2 * t) for B in b]
        a2.sort()
        b2.sort()
        ansb = 0
        r1 = r2 = r3 = 0
        for A in reversed(a2):
            while r1 < N and A + b2[r1] < t:
                r1 += 1
            while r2 < N and A + b2[r2] < 2*t:
                r2 += 1
            while r3 < N and A + b2[r3] < 3*t:
                r3 += 1
            ansb += (r2 - r1) + (N - r3)
        ans += ((ansb %2 ) << i)
    print(ans)
    return

#Solve
if __name__ == '__main__':
    B()
