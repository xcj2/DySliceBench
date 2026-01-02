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
    s = S()
    s.append("o")
    a = s.count("o")-1
    print(700+a*100)
    return

#B
def B():
    n, x = LI()
    m = IR(n)
    m.sort()
    msum = sum(m)
    print(n + (x - msum) // m[0])
    return

#C
def C():
    a, b, c, x, y = LI()
    if c * 2 > a + b:
        print(x * a + y * b)
        return
    if x > y:
        if c * 2 > a:
            print(c * 2 * y + (x - y) * a)
            return
        print(c * 2 * x)
        return
    if c * 2 > b:
        print(c * 2 * x + (y - x) * b)
        return
    print(c * 2 * y)

    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    C()
