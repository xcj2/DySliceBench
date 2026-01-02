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
    def add(i):
        while i < len(bit):
            bit[i] += 1
            i += i&-i
    def sum(i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i&-i
        return res
    n = I()
    a = LI()
    f = list(set(a))
    f.sort()
    c = [bisect.bisect_left(f,i) for i in a]
    k = ((n*(n+1)) >> 1) >> 1
    l = 0
    r = len(f)
    while r-l > 1:
        m = (l+r) >> 1
        b = [2*(i < m)-1 for i in c]
        s = [0]
        for i in b:
            s.append(s[-1]+i)
        b = list(set([i for i in s]))
        b.sort()
        s = [bisect.bisect_left(b,i)+1 for i in s]
        bit = [0]*(max(s)+1)
        res = 0
        for i in s:
            res += sum(i)
            add(i+1)
        if res <= k:
            l = m
        else:
            r = m
    print(f[l])
    return

#Solve
if __name__ == "__main__":
    solve()
