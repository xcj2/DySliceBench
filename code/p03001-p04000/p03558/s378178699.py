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
    s = S()
    t = S()
    if s+t == t[::-1]+s[::-1]:
        print("YES")
    else:
        print("NO")

#B
def B():
    n = I()
    for i in range(int(n**0.5)+2)[::-1]:
        if i*i <= n:
            print(i*i)
            quit()
#C
def C():
    n = I()
    a = LI()
    b = LI()
    c = LI()
    q = [0 for i in range(n)]
    ans = 0
    a.sort()
    b.sort()
    c.sort()
    for i in range(n):
        j = bisect.bisect_left(a,b[i])
        q[i] = j
    for i in range(n-1):
        q[i+1] += q[i]
    q.insert(0,0)
    for i in range(n):
        j = bisect.bisect_left(b,c[i])
        ans += q[j]
    print(ans)
#D
def D():
    def dijkstra():
        d = [float("inf") for i in range(k)]
        q = [[0,1]]
        d[1] = 0
        while q:
            dx,x = heappop(q)
            for y,dy in v[x]:
                if d[y] > dx+dy:
                    d[y] = dx+dy
                    heappush(q,[d[y],y])
        print(d[0]+1)
    k = I()
    if k == 1:
        print(1)
        quit()
    v = [[] for i in range(k)]
    for i in range(1,k):
        v[i].append([(i+1)%k,1])
        v[i].append([i*10%k,0])
    dijkstra()
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
    D()
