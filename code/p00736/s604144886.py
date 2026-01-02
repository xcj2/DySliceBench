#!usr/bin/env python3
from collections import defaultdict,deque
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
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

#2005_c
"""
n = int(input())
k = list("mcxi")
for i in range(n):
    d = {"m":0,"c":0,"x":0,"i":0}
    a,b  = input().split()
    a = list(a)
    b = list(b)
    a.insert(0,1)
    b.insert(0,1)
    for j in range(1,len(a)):
        if a[j] in k:
            if a[j-1] in k:
                d[a[j]] += 1
            else:
                d[a[j]] += int(a[j-1])
    for j in range(1,len(b))[::-1]:
        if b[j] in k:
            if b[j-1] in k:
                d[b[j]] += 1
            else:
                d[b[j]] += int(b[j-1])
            if d[b[j]] >= 10:
                l = b[j]
                while d[l] >= 10:
                    d[l] -= 10
                    l = k[k.index(l)-1]
                    d[l] += 1
    for j in k:
        if d[j]:
            if d[j] == 1:
                print(j,end = "")
            else:
                print(str(d[j])+j,end = "")
    print()
"""

#2017_c
"""
while 1:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    s = [list(map(int, input().split())) for i in range(h)]

    ans = 0
    for u in range(h):
        for d in range(u+2,h):
            for l in range(w):
                for r in range(l+2,w):
                    m = float("inf")
                    for i in range(u,d+1):
                        m = min(m,s[i][l],s[i][r])
                    for i in range(l,r+1):
                        m = min(m,s[u][i],s[d][i])
                    f = 1
                    su = 0
                    for i in range(u+1,d):
                        for j in range(l+1,r):
                            su += (m-s[i][j])
                            if s[i][j] >= m:
                                f = 0
                                break
                        if not f:
                            break
                    if f:
                        ans = max(ans,su)
    print(ans)
"""

#2016_c
"""
while 1:
    m,n = map(int, input().split())
    if m == n == 0:
        break
    ma = 7368791
    d = [0]*(ma+1)
    z = m
    for i in range(n):
        while d[z]:
            z += 1
        j = z
        while j <= ma:
            d[j] = 1
            j += z
    for j in range(z,ma+1):
        if not d[j]:
            print(j)
            break
"""

#2018_c
"""
def factorize(n):
    if n < 4:
        return [1,n]
    i = 2
    l = [1]
    while i**2 <= n:
        if n%i == 0:
            l.append(i)
            if n//i != i:
                l.append(n//i)
        i += 1
    l.append(n)
    l.sort()
    return l
while 1:
    b = int(input())
    if b == 0:
        break
    f = factorize(2*b)
    for n in f[::-1]:
        a = 1-n+(2*b)//n
        if a >= 1 and a%2 == 0:
            print(a//2,n)
            break
"""

#2010_c
"""
import sys
dp = [100]*1000000
dp_2 = [100]*1000000
dp[0] = 0
dp_2[0] = 0
for i in range(1,181):
    s = i*(i+1)*(i+2)//6
    for j in range(s,1000000):
        if dp[j-s]+1 < dp[j]:
            dp[j] = dp[j-s]+1
    if s%2:
        for j in range(s,1000000):
            if dp_2[j-s]+1 < dp_2[j]:
                dp_2[j] = dp_2[j-s]+1
while 1:
    m = int(sys.stdin.readline())
    if m == 0:
        break
    print(dp[m],dp_2[m])
"""

#2015_c
"""
from collections import deque
while 1:
    n = int(input())
    if n == 0:
        break
    s = [input() for i in range(n)]
    d = [s[i].count(".") for i in range(n)]
    m = max(d)
    c = [s[i][-1] for i in range(n)]
    q = deque()
    for i in range(1,m+1)[::-1]:
        j = 0
        while j < n:
            for k in range(j,n):
                if d[k] == i:break
            else:
                break
            j = k
            op = c[j-1]
            while j < n and d[j] == i:
                q.append(j)
                j += 1
            j = k
            if op == "+":
                k = 0
                while q:
                    x = q.pop()
                    k += int(c[x])
                    c.pop(x)
                    d.pop(x)
                    n -= 1
            else:
                k = 1
                while q:
                    x = q.pop()
                    k *= int(c[x])
                    c.pop(x)
                    d.pop(x)
                    n -= 1
            c[j-1] = k
    print(c[0])
"""

#2013_c
"""
from collections import defaultdict

def parse_expr(s,i):
    i += 1
    if s[i] == "[":
        q = []
        while s[i] != "]":
            e,i = parse_expr(s,i)
            q.append(e)
        return (calc(q),i+1)
    else:
        n,i = parse_num(s,i)
        return (calc([n]),i+1)

def parse_num(s,i):
    m = int(s[i])
    i += 1
    while f_num[s[i]]:
        m *= 10
        m += int(s[i])
        i += 1
    return (m,i)

def calc(q):
    if len(q) == 1:
        return (q[0]+1)//2
    q.sort()
    return sum(q[:len(q)//2+1])

f_num = defaultdict(lambda : 0)
for i in range(10):
    f_num[str(i)] = 1

n = int(input())
for i in range(n):
    s = input()
    print(parse_expr(s,0)[0])
"""

#2003_C
"""
while 1:
    w,h = LI()
    if w == h == 0:
        break
    s = SR(h)
    dp = [[0]*w for i in range(h)]
    for y in range(h):
        for x in range(w):
            if s[y][x].isdecimal():
                dp[y][x] = max(dp[y-1][x],dp[y][x-1])*10+int(s[y][x])
    ans = 0
    for i in dp:
        ans = max(ans,max(i))
    print(ans)
"""
#2008_C
def parse_formula(s,i):
    if s[i] == "-":
        i += 1
        e,i = parse_formula(s,i)
        return 2-e,i
    elif s[i] == "(":
        i += 1
        e1,i = parse_formula(s,i)
        op = s[i]
        i += 1
        e2,i = parse_formula(s,i)
        i += 1
        return calc(op,e1,e2),i
    else:
        return int(s[i]),i+1

def calc(op,a,b):
    if op == "*":
        return min(a,b)
    else:
        return max(a,b)

while 1:
    s = S()
    if s[0] == ".":
        break
    t = []
    f = defaultdict(int)
    for p in range(3):
        f["P"] = p
        for q in range(3):
            f["Q"] = q
            for r in range(3):
                f["R"] = r
                t.append([f[s[i]] if s[i] in "PQR" else s[i] for i in range(len(s))])
    ans = 0
    for s in t:
        if parse_formula(s,0)[0] == 2:
            ans += 1
    print(ans)

