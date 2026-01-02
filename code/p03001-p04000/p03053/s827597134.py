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
xy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


#A
def A():
    h, w = LI()
    A = SR(h)
    check = [[True for _ in range(w)] for i in range(h)]
    q = deque([])
    for tate in range(h):
        for yoko in range(w):
            if A[tate][yoko] == "#":
                q.append((tate, yoko))
                check[tate][yoko] = False
    new_q = deque([])
    ans = 0
    while True:
        while q:
            y, x = q.pop()
            for movex, movey in xy:
                if 0 <= y + movey < h and 0 <= x + movex < w and check[y + movey][x + movex]:
                    check[y + movey][x + movex] = False
                    new_q.append((y + movey, x + movex))
        if not new_q:
            break
        ans += 1
        q = new_q
        new_q = deque([])
    print(ans)
                    

        
    return

#B
def B():
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
