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
    n,a,b = LI()
    print(min(n*a,b))
    return

#B
def B():
    s = S()
    print(s.count("1"))
    return

#C
def C():
    n = list(map(int, S()))
    k = 0
    s = sum(n)
    for i in range(len(n)):
        k *= 10
        k += n[i]
    if k%s == 0:
        print("Yes")
    else:
        print("No")
    return

#D
def D():
    n = I()
    a = LI()
    ans = float("inf")
    for i in range(n):
        m = 0
        while a[i]%2 == 0:
            m += 1
            a[i] //= 2
        ans = min(m,ans)
    print(ans)
    return

#E
def E():
    def dfs(n,k):
        if n == 10:
            l.append(k)
        else:
            dfs(n+1,k+[0])
            dfs(n+1,k+[1])
    n = I()
    f = LIR(n)
    p = LIR(n)
    l = []
    dfs(0,[])
    ans = -float("inf")
    for k in l[1:]:
        m = 0
        c = [0 for i in range(n)]
        for i in range(n):
            for j in range(10):
                c[i] += f[i][j]&k[j]
            m += p[i][c[i]]
        ans = max(m,ans)
    print(ans)
    return

#F
def F():
    n,k = LI()
    a = LI()
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    d = list(d.values())
    d.sort()
    ans = 0
    for i in range(len(d)-k):
        ans += d[i]
    print(ans)
    return

#G
def G():
    n,c = LI()
    ch = LIR(n)
    T = [[0 for i in range(100002)] for j in range(c+1)]
    for s,t,cha in ch:
        T[cha-1][s] += 1
        T[cha-1][t+1] -= 1
    for i in range(c):
        for j in range(100000):
            T[i][j+1] += T[i][j]
            if T[i][j] >= 1:
                T[i][j] = 1
    ans = 0
    for i in range(100001):
        m = 0
        for j in range(c+1):
            m += T[j][i]
        ans = max(m,ans)
    print(ans)
    return

#H
def H():
    n = I()
    a = LI()
    ma = a.index(max(a))
    mi = a.index(min(a))
    ans = []
    if abs(a[ma]) > abs(a[mi]):
        ans.append([ma+1,1])
        ans.append([ma+1,1])
        a[0] += 2*a[ma]
        for i in range(n-1):
            ans.append([i+1,i+2])
            ans.append([i+1,i+2])
            a[i+1] += 2*a[i]
    else:
        ans.append([mi+1,n])
        ans.append([mi+1,n])
        a[-1] += 2*a[mi]
        for i in range(n-1)[::-1]:
            ans.append([i+2,i+1])
            ans.append([i+2,i+1])
            a[i] += 2*a[i+1]
    print(len(ans))
    for i in ans:
        print(*i)
    return

#I
def I_():
    n = I()
    print(1080/(n-1))
    return

#J
def J():
    h,w,n = LI()
    p = LIR(n)
    if n%2 == 1:
        print(-1)
        quit()
    ans = []
    for i in range(1,h+1):
        c = 0
        m = i/w
        for x,y in p:
            if m*x < y:c += 1
            elif m*x == y:
                c = 0
                break
        if c == n//2:
            ans.append([w,i])

    for i in range(1,w):
        c = 0
        m = h/i
        for x,y in p:
            if m*x < y:c += 1
            elif m*x == y:
                c = 0
                break
        if c == n//2:
            ans.append([i,h])
    if len(ans) == 0:
        print(-1)
        quit()
    ans.sort()
    for x,y in ans:
        print("("+str(x)+","+str(y)+")")
    return

#K

#L
def L():
    return

#M
def M():
    return


#Solve
if __name__ == "__main__":
    E()
