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

def solve(n,e,q):
    l = set([i for i in q])
    d = defaultdict(lambda : 0)
    for i in range(n):
        n,j,k = e[i]
        j = int(j)
        k = int(k)
        d[k-j+1] += i+1
        d[k+1] -= i+1
        l.add(k-j+1)
        l.add(k+1)
    l = list(l)
    l.sort()
    for i in range(len(l)-1):
        d[l[i+1]] += d[l[i]]
    for i in q:
        j = d[i]
        if j > 0:
            print(e[j-1][0],i-int(e[j-1][2])+int(e[j-1][1]))
        else:
            print("Unknown")
    return

#Solve
if __name__ == "__main__":
    while 1:
        n,Q = LI()
        if n == Q == 0:
            break
        e = [input().split() for i in range(n)]
        q = IR(Q)
        solve(n,e,q)

