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
    r,g = IR(2)
    print(2*g-r)

#B
def B():
    n = I()
    k = I()
    a = 1
    for i in range(n):
        if a > k:
            a += k
        else:
            a *= 2
    print(a)
#C
def C():
    def check(a,b):
        for i in range(len(a)):
            if a[i] != b[i] and a[i] != "?":
                return False
        return True
    def f(c):
        if c == "?":return "a"
        return c
    s = S()
    t = S()
    n = len(s)
    l = len(t)
    ans = []
    for i in range(n-l+1)[::-1]:
        if check(s[i:i+l],t):
            c = [f(s[j]) for j in range(i)]
            c += t
            for j in range(i+l,n):
                c += f(s[j])
            ans.append(c)
    if not len(ans):
        print("UNRESTORABLE")
    else:
        ans.sort()
        for i in ans[0]:
            print(i,end = "")
        print()
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

#Solve
if __name__ == "__main__":
    C()
