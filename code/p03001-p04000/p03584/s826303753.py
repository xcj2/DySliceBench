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
    n,k = LI()
    s = defaultdict(lambda : 0)
    v = []
    for i in range(n):
        a,b = LI()
        s[a] += b
        v.append((a,b))
    v.sort()
    f = [0]*31
    i = 0
    j = 1
    su = 0
    for a,b in v:
        if a > j:
            f[i] = su
            i += 1
            j <<= 1
            j += 1
        su += b
    f[i] = su
    for j in range(i,30):
        f[j+1] = f[j]
    f.insert(0,0)
    l = []
    for i in range(31):
        if k&(1<<i):
            l.append(i)
    l = l[::-1]
    ans = s[0]
    p = 0
    for i in l:
        p |= (1<<i)-1
        res = 0
        for a,b in v:
            if a&p == a:
                res += b
        if ans < res:
            ans = res
        p += 1
        res = 0
        for a,b in v:
            if a&p == a:
                res += b
        if ans < res:
            ans = res
    print(ans)
    return


#Solve
if __name__ == "__main__":
    solve()
