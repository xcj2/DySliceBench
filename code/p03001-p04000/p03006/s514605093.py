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
    n,k = LI()
    print(n%k)
    return

#B
def B():
    n = I()
    po = LIR(n)
    if n == 1:
        print(1)
        quit()
    ans = float("inf")
    for i in range(n):
        for j in range(n):
            if i == j:continue
            x,y = po[i]
            s,t = po[j]
            p,q = s-x,t-y
            m = n
            for k in range(n):
                for l in range(n):
                    if (po[k][0]-po[l][0],po[k][1]-po[l][1]) == (p,q):m -= 1
            if m < ans:
                ans = m
    print(ans)
    return

#C
def C():
    n = I()
    a = LI()
    a.sort()
    if a[0] >= 0:
        print(sum(a)-2*a[0])
        for i in range(1,n-1):
            print(a[0],a[i])
            a[0] -= a[i]
        print(a[n-1],a[0])
    else:
        if a[-1] < 0:
            print(2*a[-1]-sum(a))
            for i in range(n-1):
                print(a[-1],a[i])
                a[-1] -= a[i]
        else:
            m = bisect.bisect_left(a,0)
            p = n-m
            ans = -sum(a[:m])+sum(a[m:])
            print(ans)
            if p > m:
                l = a[-1]
                a = a[:-1]
                a = a[::-1]
                p -= 1
                p,m = m,p
                k = a[m]-a[m-1]
                print(a[m],a[m-1])
                for i in range(p-1):
                    print(a[m-i-2],k)
                    k = a[m-i-2]-k
                    print(a[m+i+1],k)
                    k = a[m+i+1]-k
                for i in range(m-p):
                    print(k,a[i])
                    k -= a[i]
                print(l,k)
            else:
                k = a[m]-a[m-1]
                print(a[m],a[m-1])
                for i in range(p-1):
                    print(a[m-i-2],k)
                    k = a[m-i-2]-k
                    print(a[m+i+1],k)
                    k = a[m+i+1]-k
                for i in range(m-p):
                    print(k,a[i])
                    k -= a[i]
    return

#D
def D():
    n = I()

    return

#E
def E():
    n = I()

    return

#F
def F():
    n = I()

    return

#G
def G():
    n = I()

    return

#H
def H():
    n = I()

    return

#I
def I_():
    n = I()

    return

#J
def J():
    n = I()

    return

#Solve
if __name__ == "__main__":
    B()
