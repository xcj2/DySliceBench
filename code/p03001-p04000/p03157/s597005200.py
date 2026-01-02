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
    h = II()
    w = II()
    print((n-h+1)*(n-w+1))
    return

#B
def B():
    n = II()
    a, b = LI()
    p = LI()
    p.sort()
    ans = [0 for i in range(3)]
    for p_ in p:
        if p_ <= a:
            ans[0] += 1
        elif a < p_ <= b:
            ans[1] += 1
        else:
            ans[2] += 1
    print(min(ans))
    return

#C
def C():
    h, w = LI()
    s = SR(h)
    def bfs(x, y):
        xy_ = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        count1 = 1
        count2 = 0
        q = deque([])
        q.append((x,y))
        while q:
            x,y = q.popleft()
            for xy in xy_:
                x_, y_ = x + xy[0], y + xy[1]
                if 0 <= x_ < w and 0 <= y_ < h:
                    if s[y_][x_] != s[y][x] and field[y_][x_]:
                        field[y_][x_] = False
                        if s[y_][x_] == "#":
                            count1 += 1
                        else:
                            count2 += 1
                        q.append((x_, y_))
        return count1*count2
                        
    field = [[True for i in range(w)] for k in range(h)]
    ans = 0
    for y in range(h):
        for x in range(w):
            if s[y][x] == "#" and field[y][x]:
                field[y][x] = False
                ans += bfs(x, y)
    
    print(ans)
    
        
    return

#D
def D():
    n, q = LI()
    a = LI()
    xq = IR(n)

    for x in xq:
        print(ans[x])
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
    C()
