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
    n = input()
    if n == "A":
        print("T")
    elif n == "C":
        print("G")
    elif n == "G":
        print("C")
    else:
        print("A")
    return

#B
def B():
    s = S()
    ans = 0
    n = len(s)
    for i in range(n):
        for j in range(i,n):
            f = 1
            for k in range(i,j+1):
                if s[k] not in list("AGCT"):f = 0
            if f:
                ans = max(ans,j+1-i)
    print(ans)
#C
def C():
    n,q = LI()
    s = S()
    f = [0 for i in range(n)]
    for i in range(n-1):
        if s[i:i+2] == ["A","C"]:
            f[i+1] += 1
    for i in range(n-1):
        f[i+1] += f[i]
    f.insert(0,0)
    for i in range(q):
        l,r = LI()
        print(f[r]-f[l])
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

#Solve
if __name__ == "__main__":
    C()
