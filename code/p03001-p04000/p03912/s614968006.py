#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    n,m = LI()
    x = LI()
    d = [[0]*2 for i in range(m)]
    for i in x:
        d[i%m][0] += 1
    x.sort()
    for i in range(max(x)+1):
        k = bisect.bisect_right(x,i)-bisect.bisect_left(x,i)
        if k > 1:
            p = i%m
            s = k >> 1
            d[p][0] -= 2*s
            d[p][1] += 2*s
    ans = 0
    for i in range(1,((m+1)>>1)):
        a,b = d[i]
        c,d_ = d[m-i]
        if a+b > c+d_:
            a,c = c,a
            b,d_ = d_,b
        ans += a+b
        if a+b <= c:
            c -= a+b
            ans += d_ >> 1
        else:
            d_ -= (a+b-c)
            ans += d_ >> 1
    ans += sum(d[0])>>1
    if not m&1:
        k = m >> 1
        ans += sum(d[k])>>1
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
