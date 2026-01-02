#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
import sys
import math
import bisect
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
    n,d,a = LI()
    p = LIR(n)
    s = [0]*(n+1)
    p.sort()
    ans = 0
    X = [p[i][0] for i in range(n)]
    for i in range(n):
        x,h = p[i]
        j = bisect.bisect_left(X,x-2*d)
        if i != j:
            su = s[i-1]
            if j > 0:
                su -= s[j-1]
            h -=  su
        if h > 0:
            l = x
            k = math.ceil(h/a)
            ans += k
            s[i] = k*a
        s[i] += s[i-1]
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()
