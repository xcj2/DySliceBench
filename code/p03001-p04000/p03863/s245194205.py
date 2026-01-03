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
    s = LS()
    print(s[0][0]+s[1][0]+s[2][0])
    return

#B
def B():
    a, b, x = LI()
    print(b // x - (a - 1) // x)
    
    return

#C
def C():
    n, x = LI()
    a = LI()
    ans = 0
    for i in range(n-1):
        if a[i] + a[i + 1] > x:
            if x > a[i]:
                ans += a[i] + a[i + 1] - x
                a[i + 1] = x - a[i]
            else:
                ans += a[i] + a[i + 1] - x
                a[i + 1] = 0
    print(ans)
    return

#D
def D():
    s = S()
    ans = ["First", "Second"]
    if s[-1] == s[0]:
        print(ans[len(s) % 2])
    else:
        print(ans[len(s) % 2 - 1])
    return


#Solve
if __name__ == '__main__':
    D()
