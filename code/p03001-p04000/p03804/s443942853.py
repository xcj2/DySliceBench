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
    a -= 2
    b -= 2
    a %= 13
    b %= 13
    if a > b:
        print("Alice")
    elif a < b:
        print("Bob")
    else:
        print("Draw")
    return

#B
def B():
    n, m = LI()
    a = SR(n)
    b = SR(m)
    if a == b:
        print("Yes")
        return
    for y in range(n - m):
        for x in range(n - m):
            if a[y][x] == b[0][0]:
                flg = 0
                for yi in range(m):
                    for xi in range(m):
                        if b[yi][xi] == a[y + yi][x + xi]:
                            continue
                        flg = 1
                        break
                    if flg:
                        break
                if flg:
                    continue
                print("Yes")
                return
    print("No")
    return

#C
def C():
    return

#D
def D():
    return

#Solve
if __name__ == '__main__':
    B()
