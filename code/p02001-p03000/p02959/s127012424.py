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
    a,b = LI()
    if (a-b)%2 == 0:
        print((a+b)//2)
    else:
        print("IMPOSSIBLE")
    return

#B
def B():
    n = I()
    p = LI()
    k = [p[i] for i in range(n)]
    k.sort()
    s = 0
    for i in range(n):
        s += (p[i] != k[i])
    if s < 3:
        print("YES")
    else:
        print("NO")
    return

#C
def C():
    n = I()
    a = LI()
    b = LI()
    b.append(0)
    ans = 0
    sb = sum(b)
    i = n
    while i >= 0:
        if a[i] > b[i]:
            a[i] -= b[i]
            b[i] = 0
        else:
            b[i] -= a[i]
            a[i] = 0
        if a[i] > b[i-1]:
            a[i] -= b[i-1]
            b[i-1] = 0
        else:
            b[i-1] -= a[i]
            a[i] = 0
        i -= 1

    print(sb-sum(b))
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

#Solve
if __name__ == "__main__":
    C()
