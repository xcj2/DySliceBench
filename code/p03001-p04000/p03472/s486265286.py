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
    n = I()
    print(n*800-200*(n//15))

#B
def B():
    k = I()
    ans = 0
    for i in range(1,k):
        for j in range(i+1,k+1):
            if (i%2)^(j%2):
                ans += 1
    print(ans)

#C
def C():
    x,t = LI()
    print(max(0,x-t))

#D
def D():
    n = I()
    ans = 1
    for i in range(1,n+1):
        ans *= i
        ans %= mod
    print(ans)

#E
def E():
    x,y,s,t = LI()
    return

#F
def F():
    n = I()
    x = LI()
    a = sorted(x)
    for i in range(n):
        j = bisect.bisect_left(a,x[i])
        if j >= n//2:
            print(a[n//2-1])
        else:
            print(a[n//2])

#G
def G():
    n,m = LI()
    if m <= 2*n:print(m//2)
    else:
        ans = n
        m -= 2*n
        ans += m//4
        print(ans)

#H
def H():
    n,k = LI()
    ans = 0
    fact
    for i in range(1,3*n+1):
        if i%k == 0:
            return

def J():
    n = I()
    d = defaultdict(int)
    for i in range(n):
        a = I()
        if d[a]:
            d[a] -= 1
        else:
            d[a] += 1
    print(sum(d.values()))

def K():
    n,h = LI()
    v = LIR(n)
    s = 0
    i = 0
    v.sort()
    m = v[-1][0]
    v.sort(key = lambda x:-x[1])
    for a,b in v:
        if b > m:
            s += b
            i += 1
            if s >= h:break
    ans = i+(max(0,h-s)//m)
    if max(0,h-s)%m>0:
        ans += 1
    print(ans)
#Solve
if __name__ == "__main__":
    K()
