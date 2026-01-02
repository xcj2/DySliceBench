#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
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
    print(n**3)
    return

#B
def B():
    n = II()
    a = LI()
    b = LI()
    c = LI()
    ans = 0
    for i in range(n):
        ans += b[a[i] - 1] + (c[a[i] - 1] if i != n - 1 and a[i] + 1 == a[i + 1] else 0)
    print(ans)
    return

#C
def C():
    n = II()
    b = LI()
    ans = b[0]
    for i in range(n-1):
        if b[i] >= b[i + 1]:
            ans += b[i + 1]
        else:
            ans += b[i]
    print(ans)
    return

#D
def D():
    n, k = LI()
    s = S()
    a = []
    for i in range(n):
        if i == n - 1:
            a.append(s[i])
        elif s[i] != s[i + 1]:
            a.append(s[i])
    print(min(n - 1, n - len(a) + 2 * k))
    return

#E
def E():
    return

#F
def F():
    return


#Solve
if __name__ == '__main__':
    B()
