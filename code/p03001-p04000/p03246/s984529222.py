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
    n = I()
    v = LI()
    d = [defaultdict(int) for i in range(2)]
    for i in range(n):
        d[i%2][v[i]] += 1
    if len(d[0].keys()) == len(d[1].keys()) == 1:
        if d[0].keys() == d[1].keys():
            ans = n//2
        else:
            d = [list(d[i].values()) for i in range(2)]
            ans = sum(d[0])-max(d[0])+sum(d[1])-max(d[1])
    else:
        d = [sorted(list(d[i].items()),key = lambda x:-x[1]) for i in range(2)]
        if d[0][0][0] != d[1][0][0]:
            ans = -d[0][0][1]-d[1][0][1]
            for i in range(len(d[0])):
                ans += d[0][i][1]
            for i in range(len(d[1])):
                ans += d[1][i][1]
        else:
            ans = -d[0][0][1]-d[1][1][1]
            for i in range(len(d[0])):
                ans += d[0][i][1]
            for i in range(len(d[1])):
                ans += d[1][i][1]
            ans2 = -d[0][1][1]-d[1][0][1]
            for i in range(len(d[0])):
                ans2 += d[0][i][1]
            for i in range(len(d[1])):
                ans2 += d[1][i][1]
            ans = min(ans,ans2)
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
