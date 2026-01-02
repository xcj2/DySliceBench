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
    s.sort()
    if s == ["a", "b", "c"]:
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    a, b, k = LI()
    ans = []
    for i in range(a, min(a + k, b + 1)):
        ans.append(i)
    for i in range(max(b - k + 1, a + k), b + 1):
        ans.append(i)
    for i in ans:
        print(i)
    return

#C
def C():
    abc= LI()
    abc.sort()
    a,b,c = abc
    a1 = (c - a) % 2
    b1 = (c - b) % 2
    if a1 and b1:
        print((c - a) // 2 + (c - b) // 2 + 1)
        return
    if a1 or b1:
        print((c - a) // 2 + (c - b) // 2 + 2)
        return
    print((c - a) // 2 + (c - b) // 2 )

    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    C()
