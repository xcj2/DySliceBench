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
    return

#B
def B():
    return

#C
def C():
    def bfs(a,b):
        bfs_map = [1 for i in range(n)]
        bfs_map[0] = 0
        q = deque()
        q.append(0)
        s = 1
        while q:
            x = q.pop()
            for y in v[x]:
                if [x,y] != [a,b] and [x,y] != [b,a]:
                    if bfs_map[y]:
                        bfs_map[y] = 0
                        q.append(y)
                        s += 1
        return s
    n,m = LI()
    v = [deque() for i in range(n)]
    l = deque()
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
        l.append([a,b])
    ans = 0
    for a,b in l:
        s = bfs(a,b)
        if s < n:
            ans += 1
    print(ans)
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
