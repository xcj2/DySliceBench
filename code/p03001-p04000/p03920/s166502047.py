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
    ans = 0
    for i in range(101):
        if i%3 and i%5:
            ans += i
    print(ans)
    return

#B
def B():
    a,b,n = LI()
    x = input()
    for i in x:
        if i == "S":
            a = max(0,a-1)
        elif i == "C":
            b = max(0,b-1)
        else:
            if a >= b:
                a = max(0,a-1)
            else:
                b = max(0,b-1)
    print(a)
    print(b)
    return

#C
def C():
    n = I()
    d = LI()
    m = I()
    t = LI()
    dic = defaultdict(lambda : 0)
    for i in d:
        dic[i] += 1
    for i in t:
        if not dic[i]:
            print("NO")
            return
        dic[i] -= 1
    print("YES")
    return

#D
def D():
    n,m = LI()
    v = []
    f = [defaultdict(list) for i in range(2001)]
    for i in range(m):
        a,b,l = LI()
        v.append((a,b,l))
        v.append((b,a,l))
        f[l][a].append(b)
        f[l][b].append(a)
    ans = 0
    for a,b,l in v:
        rest = 2540-l
        for c in f[rest][b]:
            if a < c:
                ans += 1
    print(ans)
    return

#E
def E():
    def sum(n):
        return n*(n+1)//2
    n = I()
    l = 0
    r = n+1
    while r-l > 1:
        m = (l+r)//2
        if sum(m) < n:
            l = m
        else:
            r = m
    ans = list(range(1,r+1))
    s = sum(r)
    for i in ans:
        if i != s-n:
            print(i)
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

#Solve
if __name__ == "__main__":
    E()
