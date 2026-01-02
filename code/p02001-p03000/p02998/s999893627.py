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
    s = S()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            print("Bad")
            quit()
    print("Good")
    return

#B
def B():
    n,l = LI()
    a = [i+l for i in range(n)]
    ans = sum(a)
    m = n+l-1
    for i in a[::-1]:
        if i < 0:break
        m = min(m,i)
    ans -= m
    print(ans)
    return

#C
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
def C():
    a,b,c,d = LI()
    g = gcd(c,d)
    l = c*d//g
    sc = b//c-(a-1)//c
    sd = b//d-(a-1)//d
    sl = b//l-(a-1)//l
    print(b-a+1-sc-sd+sl)
    return

#D
def D():
    n = I()
    w = LIR(n)
    w.sort(key = lambda x: x[1])
    t = 0
    for a,b in w:
        if t+a > b:
            print("No")
            quit()
        t += a
    print("Yes")
    return

#E
def E():
    n,k = LI()
    if k == 0:
        m = (n*(n-1))//2
        print(m)
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                print(i,j)
    else:
        if k > ((n-1)*(n-2))//2:
            print(-1)
        else:
            ans = []
            for i in range(2,n+1):
                ans.append((1,i))
            m = ((n-1)*(n-2))//2
            for i in range(2,n+1):
                for j in range(i+1,n+1):
                    if m == k:break
                    ans.append((i,j))
                    m -= 1
                if m == k:break
            print(len(ans))
            for i,j in ans:
                print(i,j)
    return

#F
def F():
    def root(x):
        if par[x] == x:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(x,y):
        x = root(x)
        y = root(y)
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
    n = I()
    v = defaultdict(list)
    h = defaultdict(list)
    par = defaultdict(int)
    rank = defaultdict(int)
    for i in range(n):
        a,b = LI()
        v[a].append(b)
        h[b].append(a)
        par[a] = a
        rank[a] = 0
    h = h.values()
    for l in h:
        for i in range(len(l)-1):
            x = l[i]
            y = l[i+1]
            if root(x) != root(y):
                unite(x,y)
    h = defaultdict(list)
    for i in par.keys():
        par[i] = root(par[i])
        h[par[i]].append(i)
    h = h.values()
    ans = 0
    for k in h:
        f = defaultdict(lambda : 0)
        l = []
        m = 0
        for i in k:
            for j in v[i]:
                if not f[j]:
                    m += 1
                    f[j] = 1
        for i in k:
            ans += m-len(v[i])
    print(ans)
    return

#Solve
if __name__ == "__main__":
    F()
