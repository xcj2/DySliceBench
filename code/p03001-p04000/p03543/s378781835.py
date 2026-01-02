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
    n = S()
    if n[1] == n[2]:
        if n[0] == n[1] or n[2] == n[3]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    return

#B
def B():
    return

#C
def C():
    a,b,c,d = list(map(int, S()))
    s = ["-","+"]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if eval(str(a)+s[i]+str(b)+s[j]+str(c)+s[k]+str(d)) == 7:
                    print(str(a)+s[i]+str(b)+s[j]+str(c)+s[k]+str(d)+"=7")
                    quit()
#D
def D():
    h,w = LI()
    d = [None for i in range(10)]
    for i in range(10):
        d[i] = LI()
    for k in range(10):
        for i in range(10):
            for j in range(10):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    ans = 0
    for i in range(h):
        s = LI()
        for k in s:
            if k != -1:
                ans += d[k][1]
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
    A()
