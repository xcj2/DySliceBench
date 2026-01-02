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
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    n,m = LI()
    e = IR(m)
    f = [0 for i in range(n+1)]
    ans = [None for i in range(n)]
    i = m-1
    while i >= 0:
        if not f[e[i]]:
            f[e[i]] = 1
        else:
            e.pop(i)
        i -= 1
    ans[:len(e)] = e[::-1]
    k = sum(f)
    for i in range(1,n+1):
        if not f[i]:
            ans[k] = i
            k += 1
    for i in ans:
        print(i)
    return

#B
def B():
    def mul(a,b):
        return (a[0]*b[0]-a[1]*b[1])**2+(a[0]*b[1]+a[1]*b[0])**2
    def factorize(n):
        if n < 4:
            return []
        i = 2
        res = []
        while i**2 < n:
            if n%i == 0:
                res.append(i)
            i += 1
        return res
    q = I()
    power = [i**2 for i in range(1000000)]
    f = defaultdict(lambda : 0)
    for i in power:
        f[i] = 1
    for _ in range(q):
        a,b = LI()
        k = mul((a,b),(a,b))
        fa = factorize(k)
        ans = None
        for i in fa:
            j = k//i
            s = 0
            for m in power:
                if m > i:break
                n = i-m
                if f[n]:
                    s += 1
                    break
            for m in power:
                if m > j:break
                n = i-m
                if f[n]:
                    s += 1
                    break
            if s == 2:
                ans = "C"
                break
        if ans == None:
            print("P")
        else:
            print("C")
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
    B()

