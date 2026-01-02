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
    s = S()
    k = I()
    for i in range(k):
        if s[i] != "1":
            print(s[i])
            quit()
    print(1)

#D
def D():
    n,m,q = LI()
    v = [[] for i in range(n)]
    for i in range(m):
        l,r = LI()
        v[l-1].append(r-1)
    for i in range(n):
        v[i].sort()
    f = [[bisect.bisect_right(v[i],j) for j in range(n)] for i in range(n)]
    for i in range(q):
        p,q = LI()
        p -= 1
        q -= 1
        ans = 0
        for j in range(p,q+1):
            ans += f[j][q]
        print(ans)
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
    D()
