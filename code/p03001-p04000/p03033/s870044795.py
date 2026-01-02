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
    a,p = LI()
    print((a*3+p)//2)
    return

#B
def B():
    n = I()
    s = [None for i in range(n)]
    for i in range(n):
        l = input().split()
        s[i] = l+[i]
    s.sort(key = lambda x:(x[0],-int(x[1])))
    for i,a,b in s:
        print(b+1)
    return

#C
def C():
    def dfs(d,k):
        if d == n:
            l.append(k)
        else:
            dfs(d+1,k+[0])
            dfs(d+1,k+[1])
    n,m = LI()
    l = []
    dfs(0,[])
    qu = LIR(m)
    p = LI()
    ans = 0
    for k in l:
        s = 0
        for q in range(m):
            num = qu[q][0]
            lis = list(map(lambda x:x-1, qu[q][1:]))
            su = 0
            for i in lis:
                su ^= k[i]
            if su == p[q]:
                s += 1
        if s == m:
            ans += 1
    print(ans)
    return

#D
def D():
    n,k = LI()
    v = LI()
    ans = -float("inf")
    for l in range(min(k,n)+1):
        for r in range(min(k,n)-l+1):
            m = 0
            q = v[:l]+v[n-r:]
            q.sort()
            res = max(0,k-r-l)
            for i in range(len(q)):
                if q[i] < 0 and res > 0:
                    res -= 1
                else:
                    m += q[i]
            if m > ans:
                ans = m
    print(ans)
    return

#E
def E():
    n,Q = LI()
    e = []
    for i in range(n):
        s,t,x = LI()
        e.append((s-x,x,1))
        e.append((t-x-0.1,x,0))
    e.sort(key = lambda x : x[0])
    m = 2*n
    q = set()
    j = 0
    ans = float("inf")
    for i in range(Q):
        d = I()
        while j < m:
            t,x,k = e[j]
            if d < t:
                break
            if k:
                q.add(x)
                if x < ans:
                    ans = x
            else:
                q.remove(x)
                if ans == x:
                    if q:
                        ans = min(q)
                    else:
                        ans = float("inf")
            j += 1
        print(-1 if ans == float("inf") else ans)
    return

#F
def F():
    n = I()

    return

#Solve
if __name__ == "__main__":
    E()
