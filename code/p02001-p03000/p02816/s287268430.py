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
    def Z_algorithm(s):
        n = len(s)
        z = [0]*n
        z[0] = n
        c = 1
        for i in range(1,n):
            if i+z[i-c] < c+z[c]:
                z[i] = z[i-c]
            else:
                j = max(0,c+z[c]-i)
                while i+j < n and s[j] == s[i+j]:
                    j += 1
                z[i] = j
                c = i
        return z
    n = I()
    a = LI()
    b = LI()
    c = [a[i]^a[(i+1)%n] for i in range(n)]
    d = [b[i]^b[(i+1)%n] for i in range(n)]
    z = Z_algorithm(d+c*2)[n:2*n]
    for k in range(n):
        if z[k] >= n:
            print(k,a[k]^b[0])
    return

#Solve
if __name__ == "__main__":
    solve()
