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
    def dfs(i,k):
        if i == d:
            l.append(k)
        else:
            for j in range(2):
                dfs(i+1,k+[j])
    d,g = LI()
    p = LIR(d)
    ans = float("inf")
    l = []
    dfs(0,[])
    for k in l:
        m = 0
        o = 0
        q = [[p[i][0],p[i][1]] for i in range(d)]
        for i in range(d):
            if k[i]:
                o += q[i][0]
                m += q[i][0]*(i+1)*100+q[i][1]
                q[i][0] = 0
        while m < g:
            for i in range(d)[::-1]:
                for j in range(q[i][0]):
                    m += (i+1)*100
                    o += 1
                    if m >= g:break
                if m >= g:break
        ans = min(ans,o)
    print(ans)
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
