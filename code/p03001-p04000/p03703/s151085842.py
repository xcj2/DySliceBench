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
    n = I()

    return

#B
def B():
    n = I()

    return

#C
def C():
    def add(i):
        while i < len(bit):
            bit[i] += 1
            i += i&-i

    def sum(i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i&-i
        return res

    n,k = LI()
    a = IR(n)
    a.insert(0,0)
    for i in range(n+1):
        a[i] -= k
    for i in range(n):
        a[i+1] += a[i]
    b = list(set([a[i] for i in range(n+1)]))
    b.sort()
    for i in range(n+1):
        a[i] = bisect.bisect_right(b,a[i])
    bit = [0]*(max(a)+1)
    ans = 0
    for i in range(n+1):
        ans += sum(a[i])
        add(a[i])
    print(ans)
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
