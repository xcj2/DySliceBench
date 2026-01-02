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
inf = float('INF')

#A
def A():
    n = II()
    if n == 1:
        print("Hello World")
    else:
        print(II()+II())
    return

#B
def B():
    return

#C
def C():
    n = II()
    xyh = LIR(n)
    xyh.sort(key = lambda x:x[2], reverse = True)
    x1, y1, h1 = xyh[0]
    del xyh[0]
    for x in range(101):
        for y in range(101):
            h = abs(x - x1) + abs(y - y1) + h1
            flg = True
            for xn, yn, hn in xyh:
                if max(h - abs(x - xn) - abs(y - yn), 0) == hn:
                    continue
                flg = False
                break
            if flg:
                print(x, y, h)
                return 
    return

#D
def D():
    n, m = LI()
    ans = 1
    for i in range(1,int(math.sqrt(m)+1)):
        if m % i == 0:
            a = m // i
            #print(i,a)
            if a * n <= m:
                ans = max(ans, a)
            if i * n <= m:
                ans = max(ans, i)
    print(ans)
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
