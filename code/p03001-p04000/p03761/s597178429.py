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
    a, b, c = LI()
    if b - a == c - b:
        print("YES")
    else:
        print("NO")
    return

#B
def B():
    o = S()
    e = S()
    for i in range(len(e)):
        print(o[i] + e[i], end="")
    if len(e) != len(o):
        print(o[-1], end="")
    print()
    return

#C
def C():
    l = [inf] * 27
    n = II()
    for _ in range(n):
        b = [0] * 27
        for si in S():
            b[ord(si) - 97] += 1
        for i in range(27):
            l[i] = min(l[i], b[i])
    ans = []
    for i in range(27):
        ans.append(chr(97 + i) * l[i])
    print("".join(ans))
    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    C()
