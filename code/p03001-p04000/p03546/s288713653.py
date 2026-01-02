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
    for i in range(2):
        if s[i] == s[i + 1] == s[i + 2]:
            print("Yes")
            return
    print("No")
    return

#B
def B():
    return

#C
def C():
    abcd = list(map(int, S()))
    op = itertools.product(range(2), repeat=3)
    for opx in op:
        ans = abcd[0]
        for num, opi in enumerate(opx):
            if opi:
                ans += abcd[num + 1]
            else:
                ans -= abcd[num + 1]
        if ans == 7:
            print(abcd[0],end="")
            for num, opi in enumerate(opx):
                print(["-", "+"][opi] + str(abcd[num + 1]), end="")
            print("=7")
            return
    return

#D
def D():
    h, w = LI()
    edg = LIR(10)
    for k in range(10):
        for x in range(10):
            for y in range(10):
                edg[x][y] = min(edg[x][k] + edg[k][y], edg[x][y])
    a = LIR(h)
    ans = 0
    for y in range(h):
        for x in range(w):
            if a[y][x] == -1:
                continue
            ans += edg[a[y][x]][1]
    print(ans)
    return

#Solve
if __name__ == '__main__':
    D()
