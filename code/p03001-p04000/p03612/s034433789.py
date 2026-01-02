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
    x, t = LI()
    print(max(0, x-t))
    return

#B
def B():
    s = S()
    print("".join(s[::2]))
    return

#C
def C():
    II()
    a = LI()
    lis = [0] * (max(a) + 3)
    for ai in a:
        lis[ai - 1] += 1
        lis[ai] += 1
        lis[ai + 1] += 1
    print(lis)
    print(max(lis))
    return

#D
def D():
    n = II()
    p = LI()
    ans = 0
    a = 0
    for i in range(n):
        k = i + 1
        if p[i] == k:
            a += 1
        else:
            ans += (a + 1) // 2
            a = 0
    print(ans + (a + 1) // 2)
    return

#Solve
if __name__ == '__main__':
    D()
