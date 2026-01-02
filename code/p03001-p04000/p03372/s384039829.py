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

# A
"""
s = input()
sum = 700
for i in range(3):
    if s[i] == "o":
        sum += 100
print(sum)
"""
# B
"""
n, x = map(int, input().split(" "))
m = [0 for i in range(n)]
sum = 0
for i in range(n):
    m[i] = int(input())
m.sort()
for i in range(n):
    x -= m[i]
    sum += 1
sum += (x//m[0])
print(sum)
"""
# C
"""
a,b,c,x,y = map(int, input().split(" "))
sum = 0
if a+b >= c*2:
    v = min(x, y)
    for i in range(v):
        sum += 2*c
    x -= v
    y -= v

if a < c*2:
    sum += a*x
if b < c*2:
    sum += b*y
if a >= c*2:
    sum += 2*c*x
if b >= c*2:
    sum += 2*c*y
print(sum)
"""
# D
n,c = LI()
l = [0]
r = []
v = [0]
for i in range(n):
    a,b = LI()
    l.append(a)
    r.append(c-a)
    v.append(b)
r.append(0)
r = r[::-1]
sl = defaultdict(int)
sr = defaultdict(int)
sl[0] = 0
sr[0] = 0
for i in range(n):
    sl[i+1] = sl[i]+v[i+1]-l[i+1]+l[i]
for i in range(n):
    if sl[i+1] < sl[i]:
        sl[i+1] = sl[i]
for i in range(n):
    sr[i+1] = sr[i]+v[-i-1]-r[i+1]+r[i]
for i in range(n):
    if sr[i+1] < sr[i]:
        sr[i+1] = sr[i]
ans = 0
x = 0
for i in range(n+1):
    x += v[i]
    j = n-i
    m = max(x-l[i],x-2*l[i]+sr[j])
    ans = max(ans,m)

x = 0
for i in range(n+1):
    x += v[-i]
    j = n-i
    m = max(x-r[i],x-2*r[i]+sl[j])
    ans = max(ans,m)
print(ans)
