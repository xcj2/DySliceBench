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
    q,h,s,d = LI()
    n = I()
    print(min(d,s<<1,h<<2,q<<3)*((n<<2)>>3)+min(s,h<<1,q<<2)*(((n<<2)&((1<<3)-1))>>2)+min(h,q<<1)*(((n<<2)&((1<<2)-1))>>1)+q*((n<<2)&((1<<1)-1)))
    return
#B
def B():
    a = input()
    n = len(a)
    f = defaultdict(lambda : 0)
    for i in a:
        f[i] += 1
    ans = 1+(n*(n+1)>>1)
    for i in f.values():
        ans -= i*(i+1)>>1
    print(ans)
    return

#C
def C():

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
