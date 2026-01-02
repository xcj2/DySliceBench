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
    a,b,c,d = IR(4)
    print(min(a,b)+min(c,d))

#B
def B():
    n = I()
    d,x = LI()
    a = IR(n)
    for i in range(1,d+1):
        for j in a:
            if (i-1)%j == 0:
                x += 1
    print(x)
#C
def C():
    n = I()
    a = LI()
    ans = abs(a[0])
    for i in range(n-1):
        ans += abs(a[i+1]-a[i])
    ans += abs(a[-1])
    a.insert(0,0)
    a.append(0)
    for i in range(1,n+1):
        if a[i-1] <= a[i] <= a[i+1] or a[i+1] <= a[i] <= a[i-1]:
            print(ans)
        else:
            print(ans-abs(a[i]-a[i-1])-abs(a[i+1]-a[i])+abs(a[i+1]-a[i-1]))
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
