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
    n = II()
    a = LI()
    a.sort()
    x = list(set(a))
    if len(x) > 3:
        print("No")
    elif len(x) == 3:
        x1 = bisect_right(a, x[0]) - bisect_left(a, x[0])
        x2 = bisect_right(a, x[1]) - bisect_left(a, x[1])
        x3 = bisect_right(a, x[2]) - bisect_left(a, x[2])
        if ((x[0] ^ x[1] ^ x[2]) == 0) and (x1 == x2 == x3):
            print("Yes")
        else:
            print("No")
    elif len(x) == 2:
        x1 = bisect_right(a, x[0]) - bisect_left(a, x[0])
        x2 = bisect_right(a, x[1]) - bisect_left(a, x[1])
        if x1 * 2 == x2 and x[0] == 0:
            print("Yes")
        else:
            print("No")
    elif len(x) == 1:
        if x[0] == 0:
            print("Yes")
        else:
            print("No")
    return

#B
def B():
    n, m = LI()
    if m % 2:
        print(-1)
        return
    edg = [[] for _ in range(n)]
    ins = defaultdict(int)
    c = defaultdict(int)
    for _ in range(m):
        a, b = LI_()
        edg[a].append(b)
        edg[b].append(a)
        ins[a] += 1
        ins[b] += 1
    dag = [[] for _ in range(n)]
    q = deque()
    q.append((0, -1))
    for i in edg[0]:
        q.append((i, 0))
    while q:
        now, per = q.pop()
        if per == -1:
            continue
        if c[now]:
            pass
        
    for d in dag:
        if len(d) % 2:
            print(-1)
            return
    for num, d in enumerate(dag):
        for x in d:
            print(num + 1, x + 1)
    return

#C
def C():
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    A()
