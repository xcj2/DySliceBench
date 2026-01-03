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
    print((a+b)%24)
    return

#B
def B():
    n, m = LI()
    ab = LIR(n)
    cd = LIR(m)
    for a, b in ab:
        ans = inf
        an = 0
        for num, cdi in enumerate(cd):
            c, d = cdi
            if ans > abs(a - c) + abs(b - d):
                ans = abs(a - c) + abs(b - d)
                an = num
        print(an+1) 
    return

#C
def C():
    n = II()
    ans = inf
    for i in range(1, int(math.sqrt(n)) + 1):
        if not n % i:
            ans = min(ans, max(int(math.log(i, 10)), int(math.log(n // i, 10))))
    print(ans+1)
    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    C()
