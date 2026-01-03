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

    return

#C
def C():

    return

#D
def D():
    n,m = LI()
    x = LI()
    d = defaultdict(lambda : 0)
    for i in x:
        d[i] += 1
    f = [[0]*2 for i in range(m)]
    for i,j in d.items():
        k = i%m
        f[k][0] += j-(j&1)
        f[k][1] += j&1
    ans = sum(f[0])>>1
    for i in range(1,(m>>1)+1):
        if i == m-i:
            ans += sum(f[i])>>1
            break
        a,b,c,d = f[i][0],f[i][1],f[m-i][0],f[m-i][1]
        if a+b <= c+d:
            ans += a+b
            if a+b <= d:
                ans += c>>1
            else:
                ans += (c-(a+b-d))>>1
        else:
            ans += c+d
            if c+d <= b:
                ans += a>>1
            else:
                ans += (a-(c+d-b))>>1
    print(ans)
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
    D()
