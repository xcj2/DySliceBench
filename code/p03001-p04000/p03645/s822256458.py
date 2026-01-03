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
    n = II()
    print("ABC"+str(n))
    return

#B
def B():
    ni = [2 ** i for i in range(1, 10)]
    n = II()
    ans = 1
    for i in range(1, n + 1):
        if i in ni:
            ans = i
    print(ans)        
    return

#C
def C():
    n, m = LI()
    edg = [[] for i in range(n)]
    for _ in range(m):
        a, b = LI_()
        edg[a].append(b)
        edg[b].append(a)
    next = []
    for i in edg[0]:
        next.append(i)
    for ne in next:
        for i in edg[ne]:
            if i == n - 1:
                print("POSSIBLE")
                return
    print("IMPOSSIBLE")
    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    C()
