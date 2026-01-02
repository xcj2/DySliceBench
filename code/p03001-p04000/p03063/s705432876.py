#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 998244353

#C
def C():
    n = I()
    s = S()
    ans = float("inf")
    b = [0 for i in range(n)]
    for i in range(n):
        if s[i] == "#":
            b[i] = 1
    w = [0 for i in range(n)]
    for i in range(n):
        if s[i] == ".":
            w[i] = 1
    b.insert(0,0)
    w.insert(0,0)
    for i in range(n):
        b[i+1] += b[i]
        w[i+1] += w[i]
    for i in range(n+1):
        m = b[i]+w[n]-w[i]
        ans = min(ans,m)
    print(ans)
    return

#D
def D():
    n = I()
    a = IR(n)

    return

#E
def E():
    n = I()

    return

#F
def F():
    return


#Solve
if __name__ == "__main__":
    C()
