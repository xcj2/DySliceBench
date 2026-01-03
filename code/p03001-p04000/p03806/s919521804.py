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
    n, m = LI()
    edg = [[] for i in range(n)]
    for _ in range(m):
        a, b = LI_()
        edg[a].append(b)
        edg[b].append(a)
    def dfs(i, c):
        res = 0
        c[i] = False
        if not (True in c):
            c[i] = True
            return 1
        for e in edg[i]:
            if c[e]:
                res += dfs(e, c)
        c[i] = True
        return res
    print(dfs(0, [True] * n))
    return

#D
def D():
    n, Ma, Mb = LI()
    abc = LIR(n)
    dp = [[inf] * (10 * n + 1) for i in range(10 * n + 1)]
    dp[0][0] = 0
    for a, b, c in abc:
        for i in range(10 * n, a - 1, -1):
            for j in range(10 * n, b - 1, -1):
                dp[i][j] = min(dp[i - a][j - b] + c, dp[i][j])
    ans = inf
    ma = Ma
    mb = Mb
    i = 1
    while 1:
        ans = min(ans, dp[ma * i][mb * i])
        i += 1
        if ma * i > 10 * n or mb * i > 10 * n:
            break
    if ans == inf:
        print(-1)
        return
    
    print(ans)
    return

#Solve
if __name__ == '__main__':
    D()