#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from itertools import permutations
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
    def gcd(a,b):
        if a == 0:
            return b
        return gcd(b%a,a)
    n,m = LI()
    a = LI()
    k = [i&-i for i in a]
    if len(set(k)) > 1 or all([i == 1 for i in k]):
        print(0)
        return
    a = [i>>1 for i in a]
    l = a[0]
    for i in a[1:]:
        g = gcd(l,i)
        l *= i//g
    print(m//l-m//(2*l))
    return

#Solve
if __name__ == "__main__":
    solve()
