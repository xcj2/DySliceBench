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
    a = I()
    s = input()
    if a >= 3200:
        print(s)
    else:
        print("red")
    return

#B
def B():
    n = I()
    a = LI()
    ans = 0
    for i in a:
        ans += 1/i
    print(1/ans)
    return

#C
def C():
    n = I()
    v = LI()
    q = []
    for i in v:
        heappush(q,i)
    while q:
        x = heappop(q)
        if not q:
            print(x)
            return
        y = heappop(q)
        heappush(q,(x+y)/2)
    return

#D
def D():
    def dfs(x,d,s):
        for y in v[x]:
            if d[y]:
                s += f[y]
                ans[y] = s
                d[y] = 0
                dfs(y,d,s)
                s -= f[y]
    n,q = LI()
    v = [[] for i in range(n)]
    for i in range(n-1):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
    f = [0]*n
    for i in range(q):
        p,x = LI()
        p -= 1
        f[p] += x
    ans = [0]*n
    d = [1]*n
    d[0] = 0
    ans[0] = f[0]
    s = f[0]
    dfs(0,d,s)
    print(*ans)
    return

#E
def E():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    d = defaultdict(lambda : [])
    for i in range(n):
        d[s[i]].append(i)
    f = [-1]*m
    alp = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(m):
        if not d[t[i]]:
            print(-1)
            return
        j = bisect.bisect_right(d[t[i]],f[i-1])
        if j == len(d[t[i]]):
            f[i] = d[t[i]][0]
        else:
            f[i] = d[t[i]][j]
    ans = 0
    for i in range(m-1):
        if f[i] >= f[i+1]:
            ans += 1
    print(ans*n+f[-1]+1)
    return

#F
def F():

    return

#Solve
if __name__ == "__main__":
    E()
