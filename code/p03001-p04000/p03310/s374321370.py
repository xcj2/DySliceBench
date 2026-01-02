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
def S(): return list(sys.stdin.readline())[:-1]
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
    def f(x,y,i):
        p = [a[x],a[i-1]-a[x],b[y],b[-i-1]-b[y]]
        if 0 in p:
            return float("inf")
        return max(p)-min(p)

    n = I()
    a = LI()
    b = [a[i] for i in range(n)]
    for i in range(n-1):
        a[i+1] += a[i]
    for i in range(n-1)[::-1]:
        b[i] += b[i+1]
    b.sort()
    ans = float("inf")
    for i in range(2,n-1):
        l = a[i-1]
        r = b[-1-i]
        li = bisect.bisect_left(a,l/2)
        ri = bisect.bisect_left(b,r/2)
        for x in range(max(li-1,0),min(li+2,i-1)):
            for y in range(max(ri-1,0),min(ri+2,n-i-1)):
                ans = min(f(x,y,i),ans)
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
