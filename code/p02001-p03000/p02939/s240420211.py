#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    s = S()
    n = len(s)
    ans = 0
    i = 0
    pre = ""
    while i < n:
        if s[i] != pre:
            pre = s[i]
            i += 1
        else:
            if i == n-1:
                ans -= 1
            pre = s[i:i+2]
            i += 2
        ans += 1
    print(ans)
    return

#B
def B():
    n = I()

    return

#C
def C():
    n = I()
    a = LI()
    b = LI()
    q = []
    for i in range(n):
        if b[i] > a[i]:
            heappush(q,(-b[i],i))
    ans = 0
    while q:
        bi,i = heappop(q)
        r = (i+1)%n
        l = i-1
        s = b[l]+b[r]
        if a[i] < s:
            m = b[i]//s
            if m:
                ans += m
                b[i] %= s
                if b[i] != a[i]:
                    heappush(q,(-b[i],i))
        else:
            k = -bi-a[i]
            m = k//s
            b[i] -= m*s
            ans += m
            if b[i] != a[i]:
                break
    if a == b:
        print(ans)
    else:
        print(-1)
    return

#D
def D():

    return

#E
def E():
    n = I()

    return

#F
def F():
    n = I()

    return

#Solve
if __name__ == "__main__":
    A()
