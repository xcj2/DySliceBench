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
    while 1:
        n = I()
        if n == 0:
            break
        m = 24*60**2
        a = [0]*m
        for i in range(n):
            l,r = input().split()
            l = list(map(int, l.split(":")))
            r = list(map(int, r.split(":")))
            l = l[2]+60*(l[1]+60*(l[0]))
            r = r[2]+60*(r[1]+60*(r[0]))
            a[l] += 1
            a[r] -= 1
        for i in range(m-1):
            a[i+1] += a[i]
        print(max(a))
    return

#Solve
if __name__ == "__main__":
    solve()

