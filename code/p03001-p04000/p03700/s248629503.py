#!/usr/bin/env python3
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
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
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
inf = float('INF')

#A
def A():
    a, b = LI()
    if a + b >= 10:
        print("error")
    else:
        print(a + b)
    return

#B
def B():
    s = S()
    if len(s) == len(set(s)):
        print("yes")
    else:
        print("no")
    return

#C
def C():
    n = II()
    m = inf
    ans = 0
    for _ in range(n):
        s = II()
        ans += s
        if s % 10:
            m = min(m, s)
    if ans % 10:
        print(ans)
    else:
        if m != inf:
            print(ans - m)
        else:
            print(0)
    return

# D
# 解説AC
# 解を2分探索で求める
# T回のときB*T以上の体力を持つ者に対しては(h-(B*T))/A-Bで最低必要な回数
# が求められることに気づけない
def D():
    def f(t):
        lh = list(map(lambda x: max(0, (x - b * t - 1) // (a - b) + 1), h))
        if sum(lh) <= t:
            return True
        return False
    n, a, b = LI()
    h = IR(n)
    maxh = max(h)
    ok = (maxh - 1) // b + 1
    ng = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
    return


#Solve
if __name__ == '__main__':
    D()
