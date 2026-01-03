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

    return

#B
def B():
    n,m = LI()
    f = [1]*n
    l = [0]*n
    l[0] = 1
    for i in range(m):
        x,y = LI()
        x -= 1
        y -= 1
        if l[x]:
            l[y] = 1
        f[x] -= 1
        f[y] += 1
        if f[x] == 0:
            l[x] = 0
    ans = 0
    for i in range(n):
        if l[i]:
            ans += 1
    print(ans)
    return

#C
def C():
    n,l = LI()
    a = LI()
    for i in range(n-1):
        if a[i]+a[i+1] >= l:
            break
    else:
        print("Impossible")
        return
    ans = list(range(1,i+1))+list(range(i+2,n))[::-1]+[i+1]
    print("Possible")
    for i in ans:
        print(i)
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
    C()
