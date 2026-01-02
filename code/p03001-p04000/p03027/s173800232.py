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
    n = I()
    print(180*(n-2))
    return

#B
def B():
    s = S()
    res = 15-len(s)
    k = s.count("o")
    if k+res >= 8:
        print("YES")
    else:
        print("NO")
    return

#C
def C():
    return

#D
def D():
    n = I()
    v = [[] for i in range(n)]
    f = [[0,i] for i in range(n)]
    for i in range(n-1):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
        f[a][0] += 1
        f[b][0] += 1
    f.sort(key = lambda x:-x[0])
    s = f[0][1]
    c = LI()
    c.sort(key = lambda x:-x)
    f[0][0] = c[0]
    q = deque()
    q.append(s)
    bfs = [1 for i in range(n)]
    f.sort(key = lambda x:x[1])
    bfs[s] = 0
    k = 1
    while q:
        x = q.popleft()
        for y in v[x]:
            if bfs[y]:
                bfs[y] = 0
                f[y][0] = c[k]
                k += 1
                q.append(y)
    ans = 0
    q.append(s)
    bfs = [1 for i in range(n)]
    bfs[s] = 0
    while q:
        x = q.popleft()
        for y in v[x]:
            ans += min(f[x][0],f[y][0])
            if bfs[y]:
                bfs[y] = 0
                q.append(y)
    print(ans//2)
    for i, j in f[:-1]:
        print(i,end = " ")
    print(f[-1][0])
    return

#E
def E():
    mod = 1000003
    f = [None for i in range(2*mod+1)]
    f[0] = 1
    for i in range(2*mod):
        f[i+1] = (i+1)*f[i]%mod
    inv_f = [0 for i in range(2*mod+1)]
    inv_f[mod-1] = pow(f[mod-1],mod-2,mod)
    for i in range(mod-1)[::-1]:
        inv_f[i] = inv_f[i+1]*(i+1)%mod
    q = I()
    for _ in range(q):
        x,d,n = LI()
        if x == 0:
            print(0)
        elif d == 0:
            print(pow(x,n,mod))
        elif n >= mod:
            print(0)
        else:
            ans = pow(d,n,mod)
            x *= pow(d,mod-2,mod)
            x %= mod
            ans *= f[x+n-1]*inv_f[x-1]%mod
            ans %= mod
            print(ans)
    return

#F
def F():
    n = I()
    return

#Solve
if __name__ == "__main__":
    E()
