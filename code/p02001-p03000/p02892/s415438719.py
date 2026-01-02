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
    s = S()
    k = I()
    n = len(s)
    for i in range(n):
        if s[i] != s[0]:
            break
    else:
        print((k*n)>>1)
        return
    s += s
    t = s[i-1]
    for j in range(n)[::-1]:
        if s[j] != t:
            break
    s = s[i:j+1]
    ans = (i>>1)+((n-1-j)>>1)+((n-1-j+i)>>1)*(k-1)
    i = 0
    n = len(s)
    while i < n:
        t = s[i]
        l = 0
        while i < n and t == s[i]:
            i += 1
            l += 1
        ans += (l >> 1)*k
    print(ans)
    return

#B
def B():
    n = I()
    s = [list(map(int, input())) for i in range(n)]
    v = [[] for i in range(n)]
    for i in range(n):
        for j  in range(i+1,n):
            if s[i][j]:
                v[i].append(j)
                v[j].append(i)
    bfs = [-1]*n
    q = deque([0])
    q[0] = 0
    f = 1
    while f and q:
        x = q.popleft()
        nb = 1-bfs[x]
        for y in v[x]:
            if bfs[y] >= 0:
                if bfs[y] != nb:
                    f = 0
                    break
            else:
                bfs[y] = nb
                q.append(y)
    if not f:
        print(-1)
        return
    ans = -1
    for i in range(n):
        bfs = [0]*n
        bfs[i] = 1
        q.append(i)
        while q:
            x = q.popleft()
            nb = bfs[x]+1
            for y in v[x]:
                if not bfs[y]:
                    bfs[y] = nb
                    q.append(y)
        m = max(bfs)
        if m > ans:
            ans = m
    print(ans)
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

#Solve
if __name__ == "__main__":
    B()
