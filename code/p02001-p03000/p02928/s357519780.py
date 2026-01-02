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
    m,d = LI()
    ans = 0
    for i in range(1,m+1):
        for j in range(1,d+1):
            d1 = j%10
            d2 = j//10
            if d1 >= 2 and d2 >= 2 and d1*d2 == i:
                ans += 1
    print(ans)
    return

#B
def B():
    def add(i):
        while i <= m:
            bit[i] += 1
            i += i&-i

    def sum(i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i&-i
        return res

    n,k = LI()
    m = 2000
    a = LI()
    bit = [0]*(m+1)
    ans = 0
    for i in range(n):
        ans += (i-sum(a[i]))*k
        add(a[i])
    inv = pow(2,mod-2,mod)
    for i in range(n):
        ans += sum(a[i]-1)*k*(k-1)*inv%mod
    print(ans%mod)
    return

#C
def C():
    n = I()

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

#Solve
if __name__ == "__main__":
    B()
