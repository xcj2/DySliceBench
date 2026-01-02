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
inf = float("INF")

#A
def A():
    a, b, c, d = LI()
    x = abs(a - b)
    y = abs(b - c)
    z = abs(a - c)
    if (x <= d and y <= d) or z <= d:
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    X = II()
    x = [False] * (10 ** 3 + 1)
    x[1] = True
    for i in range(2, int(10 ** 1.5) + 1):
        k = i*i
        while X >= k:
            x[k] = True
            k *= i
    for i in range(X, -1, -1):
        if x[i]:
            print(i)
            return
    return

#C
def C():
    s = stdin.readline().rstrip()
    K = II() - 1
    ans = []
    for i in range(len(s)):
        for k in range(K+1):
            b = s[i:i + k + 1]
            ans.append(b)
    ans = list(set(ans))
    ans.sort()
    print(ans[K])
    return

#D
def D():
    n, m = LI()
    p = LI_()
    xy = LIR_(m)
    size = [1 for _ in range(n)]
    height = [1 for _ in range(n)]
    par = [i for i in range(n)]
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def union(x, y):
        s1 = find(x)
        s2 = find(y)
        if s1 != s2:
            if height[s1] < height[s2]:
                par[s1] = s2
                size[s2] += size[s1]
                size[s1] = 0
            else:
                par[s2] = s1
                size[s1] += size[s2]
                size[s2] = 0
                if height[s1] == height[s2]:
                    height[s1] += 1

    for x,y in xy:
        union(x, y)
    ans = 0
    for i in range(n):
        if find(p[i]) == find(i):
            ans += 1
    
    print(ans)
    return

#Solve
if __name__ == '__main__':
    B()
