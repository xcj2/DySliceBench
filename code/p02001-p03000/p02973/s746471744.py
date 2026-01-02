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
def S(): return list(sys.stdin.readline())[:-1]
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
    n = I()
    print(3*n**2)
    return

#B
def B():
    n,d = LI()
    f = [1]*(n+2*d+2)
    ans = 0
    for i in range(n):
        if f[i]:
            for j in range(i,i+2*d+1):
                f[j] = 0
            ans += 1
    print(ans)
    return

#C
def C():
    n = I()
    a = IR(n)
    mi = max(a)
    if a.count(mi) > 1:
        for i in range(n):
            print(mi)
    else:
        b = [a[i] for i in range(n)]
        b.sort()
        b = b[::-1]
        for i in range(n):
            if mi != a[i]:
                print(mi)
            else:
                print(b[1])

    return

#D
def D():
    n = I()
    a = LI()
    b = [0]*(n+1)
    for i in range(1,n+1)[::-1]:
        j = 2*i
        k = 0
        while j <= n:
            k ^= b[j]
            j += i
        if a[i-1]^k:
            b[i] = 1
    ans = []
    for i in range(n+1):
        if b[i]:
            ans.append(i)
    print(len(ans))
    if ans:
        print(*ans)
    return

#E
def E():
    n = I()
    a = IR(n)
    mi = []
    ans = 0
    for i in range(n):
        j = bisect.bisect_right(mi,-a[i])
        if j == len(mi):
            mi.append(-a[i])
        else:
            mi[j] = -a[i]
    print(len(mi))
    return

#F
def F():
    n = I()

    return

#Solve
if __name__ == "__main__":
    E()
