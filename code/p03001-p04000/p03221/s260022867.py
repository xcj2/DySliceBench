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
    for i in range(n):l[i] = SR()
    return l
mod = 1000000007

#A
def A():
    return

#B
def B():
    return

#C
def C():
    n,m = LI()
    v = LIR(m)
    for i in range(m):
        v[i] = [v[i][0],v[i][1],i]
    v.sort(key = lambda x:x[1])
    f = [0 for i in range(n+1)]
    ans = [None for i in range(m)]
    for p,y,i in v:
        f[p] += 1
        s = "{:0>6}".format(p)
        t = "{:0>6}".format(f[p])
        ans[i] = s+t
    for i in ans:
        print(i)
#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == "__main__":
    C()
