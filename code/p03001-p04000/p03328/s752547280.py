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
    if n < 1000:
        print("ABC")
    else:
        print("ABD")
    return

#B
def B():
    a,b = LI()
    n = b-a
    c = (n*(n+1))//2
    print(c-b)
    return

#C
def C():
    n = I()
    ans = float("inf")
    for i in range(n+1):
        m = 0
        k = i
        while k > 0:
            m += k%6
            k //= 6
        k = n-i
        while k > 0:
            m += k%9
            k //= 9
        ans = min(ans,m)
    print(ans)
#D
def D():
    n,C = LI()
    f = LIR(C)
    c = LIR(n)
    d = [defaultdict(int) for i in range(3)]
    for i in range(n):
        for j in range(n):
            d[(i+j+2)%3][c[i][j]-1] += 1
    ans = float("inf")
    for i in range(C):
        for j in range(C):
            if i != j:
                for k in range(C):
                    if k != i and k != j:
                        m = 0
                        for a in d[0].keys():
                            m += d[0][a]*f[a][i]
                        for a in d[1].keys():
                            m += d[1][a]*f[a][j]
                        for a in d[2].keys():
                            m += d[2][a]*f[a][k]
                        ans = min(ans,m)
    print(ans)


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

#Solve
if __name__ == "__main__":
    B()
