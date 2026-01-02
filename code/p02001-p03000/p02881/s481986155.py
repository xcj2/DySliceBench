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
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    a, b = LI()
    def c(x):
        return 1 <= x <= 9
    if c(a) and c(b):
        print(a * b)
        return
    print(0)
    return

#B
def B():
    a = set()
    for i in range(10):
        for K in range(10):
            a.add(i * k)
    x = II()
    if x in a:
        print("Yes")
    else:
        print("No")
    return

#C
def C():
    n = II()
    factlize = []
    ans = inf
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            ans = min(ans, n // i + i - 2)
    print(ans)

    return

#D
def D():
    return

#E
def E():
    def solve(m):
        a1 = a[::-1]
        f1 = f[::1]
        res = 0
        for i in range(n):
            if a1[i] * f1[i] <= m:
                continue
            k = m // f1[i]
            res += a1[i] - k
            if res > K:
                return False
        return True

    n, K = LI()
    a = LI()
    a.sort()
    f = LI()
    f.sort()
    ok = max(a) * max(f)
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
    return

#F
def F():
    return


#Solve
if __name__ == '__main__':
    C()
