#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.buffer.readline().split()]
def I(): return int(sys.stdin.buffer.readline())
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
    def fact(n):
        if n < 4:
            return [n,1]
        i = 2
        res = [1,n]
        while i*i <= n:
            if n%i == 0:
                res.append(i)
                m = n//i
                if m != i:
                    res.append(m)
            i += 1
        res.sort(reverse = True)
        return res
    n,k = LI()
    a = LI()
    s = sum(a)
    f = fact(s)
    for i in f:
        s = [j%i for j in a]
        s.sort()
        s = list(accumulate(s))
        l = 0
        r = n
        while r > l+1:
            j = (l+r) >> 1
            sl = s[j]
            sr = i*(n-j-1)-s[-1]+s[j]
            if sl <= sr:
                l = j
            else:
                r = j
        sl = s[l]
        sr = i*(n-l-1)-s[-1]+s[l]
        if sl == sr:
            if sl <= k:
                print(i)
                return
    return

#Solve
if __name__ == "__main__":
    solve()
