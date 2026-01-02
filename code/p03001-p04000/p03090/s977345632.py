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
sys.setrecursionlimit(1000000)

#A
def A():
    n = I()
    b = LI()
    d = defaultdict(int)
    for i in b:
        d[i] += 1
    a = []
    ans = []
    return
#B
def B():
    n = I()
    if n%2:
        ans = []
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j != n-i and j != i:
                    ans.append((min(i,j),max(i,j)))
        ans = list(set(ans))
        print(len(ans))
        ans.sort()
        for i in ans:
            print(*i)
    else:
        ans = []
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j != n+1-i and j != i:
                    ans.append((min(i,j),max(i,j)))
        ans = list(set(ans))
        print(len(ans))
        ans.sort()
        for i in ans:
            print(*i)
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

#Solve
if __name__ == "__main__":
    B()
