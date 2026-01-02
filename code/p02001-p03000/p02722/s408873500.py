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
            return set([n])
        i = 2
        res = set([n])
        while i ** 2<= n:
            if n%i == 0:
                res.add(i)
                m = n//i
                if m != i:
                    res.add(m)
            i += 1
        return res

    def check(n,i):
        while n >= i:
            if n%i == 0:
                n //= i
            else:
                n -= i
        if n == 1:
            return 1
        return 0
    n = I()
    if n == 2:
        print(1)
        return
    ans = {2,n}
    f = fact(n)
    for i in f:
        m = n
        while not m%i:
            m //= i
        if m % i == 1:
            ans.add(i)
    ans |= fact(n-1)
    print(len(ans))
    return

#Solve
if __name__ == "__main__":
    solve()
