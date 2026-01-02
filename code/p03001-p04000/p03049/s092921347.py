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
    n,k = LI()
    print(n-k+1)
    return

#B
def B():
    r,g,b,n = LI()
    ans = 0
    for i in range(n+1):
        x = r*i
        for j in range(n+1-x):
            y = g*j
            z = n-x-y
            if z%b != 0 or z < 0:continue
            ans += 1
    print(ans)
    return

#C
def C():
    n = I()
    s = SR(n)
    f = [0 for i in range(n)]
    a = deque()
    b = deque()
    ba = deque()
    c = deque()
    l = 0
    for i in range(n):
        l += len(s[i])
        if s[i][-1] == "A":
            f[i] += 1
        if s[i][0] == "B":
            f[i] += 2
        if f[i] == 0:
            c.append(s[i])
        elif f[i] == 1:
            a.append(s[i])
        elif f[i] == 2:
            b.append(s[i])
        else:
            ba.append(s[i])
    ans = [None for i in range(l)]
    i = 0
    while a or b or c or ba:
        if a:
            x = a.popleft()
            for j in x:
                ans[i] = j
                i += 1
            while ba:
                x = ba.popleft()
                for j in x:
                    ans[i] = j
                    i += 1
            if b:
                x = b.popleft()
                for j in x:
                    ans[i] = j
                    i += 1
        elif b:
            x = b.popleft()
            for j in x:
                ans[i] = j
                i += 1
        elif c:
            x = c.popleft()
            for j in x:
                ans[i] = j
                i += 1
        while ba:
            x = ba.popleft()
            for j in x:
                ans[i] = j
                i += 1
    s = 0
    for i in range(l-1):
        if ans[i] == "A" and ans[i+1] == "B":
            s += 1
    print(s)
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

#G
def G():
    n = I()

    return

#H
def H():
    n = I()

    return

#I
def I_():
    n = I()

    return

#J
def J():
    n = I()

    return

#Solve
if __name__ == "__main__":
    C()
