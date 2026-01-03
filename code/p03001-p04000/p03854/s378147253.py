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
sys.setrecursionlimit(1000000)
mod = 1000000007


#A
def A():
    a,b = LI()
    if not (a*b)%2:
        print("Even")
    else:
        print("Odd")
    return

#B
def B():
    s = S()
    print(s.count("1"))
    return

#C
def C():
    n = I()
    a = LI()
    f = 0
    for j in range(100000):
        for i in range(n):
            if a[i]%2:
                f = 1
                break
            a[i] //= 2
        if f:break
    print(j)
    return

#D
def D():
    a,b,c,x = IR(4)
    su = 0
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if 500*i+100*j+50*k == x:su += 1
    print(su)
    return

#E
def E():
    n,y = LI()
    for i in range(n+1):
        for j in range(n+1-i):
            k = n-i-j
            if 10000*i+5000*j+1000*k == y:
                print(i,j,k)
                quit()
    print(-1,-1,-1)
    return

#F
def F():
    s = input()
    while s:
        if s[:11] == "dreameraser":
            s = s[11:]
        elif s[:10] == "dreamerase":
            s = s[10:]
        elif s[:7] == "dreamer":
            s = s[7:]
        elif s[:6] == "eraser":
            s = s[6:]
        elif s[:5] == "dream":
            s = s[5:]
        elif s[:5] == "erase":
            s = s[5:]
        else:
            print("NO")
            quit()
    print("YES")
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == "__main__":
    F()
