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
mod = 1000000007

#A
def A():
    s = S()
    c = s.count("0")
    print(2*min(c,len(s)-c))
    return

#B
def B():
    n = I()
    h = LI()
    ans = 0
    m = min(h)
    while m:
        ans += m
        k = max(h)
        for i in range(n):
            if h[i] >= m:
                h[i] -= m
                if h[i]:k = min(k,h[i])
            else:break
        m = k
    print(ans)
    return

#C
def C():
    n,k = LI()
    x = LI()
    ans = float("inf")
    j = bisect.bisect_left(x,0)
    if n == 1:
        print(abs(x[0]))
        quit()
    if j < n:
        if x[j] == 0:
            k -= 1
            x.pop(j)
            n -= 1
    for i in range(n):
        if i < j:
            if abs(i-j) > k:continue
            elif abs(i-j) == k:ans = min(ans,abs(x[i]))
            elif k+i-1 < n:
                ans = min(ans,abs(x[i])+x[k+i-1]-x[i])
        else:
            if abs(i-j)+1 > k:continue
            elif abs(i-j)+1 == k:ans = min(ans,x[i])
            elif i-k+1 >= 0:
                ans = min(ans,abs(x[i])+x[i]-x[i-k+1])

    print(ans)
    return

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

#I
def I_():
    return

#J
def J():
    return

#Solve
if __name__ == "__main__":
    C()
