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
    n = I()
    v = defaultdict(list)
    l = []
    f = defaultdict(lambda : 1)
    for i in range(n):
        x,y = LI()
        y += 100001
        v[x].append(y)
        v[y].append(x)
        if f[x]:
            f[x] = 0
            l.append(x)
        if f[y]:
            f[y] = 0
            l.append(y)
    ans = 0
    bfs = defaultdict(lambda : 1)
    q = deque()
    for i in l:
        if bfs[i]:
            bfs[i] = 0
            q.append(i)
            nx = (i < 100001)
            ny = 1-nx
            while q:
                x = q.popleft()
                for y in v[x]:
                    if bfs[y]:
                        bfs[y] = 0
                        q.append(y)
                        k = (y < 100001)
                        nx += k
                        ny += (1-k)
            ans += nx*ny
    print(ans-n)
    return

#Solve
if __name__ == "__main__":
    F()
