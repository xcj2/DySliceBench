#!usr/bin/env python3
from collections import defaultdict
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
r,g,b = LI()
if (g*10+b)%4 == 0:
    print("YES")
else:
    print("NO")
#B

#C
"""
f = [0]
for i in range(1,400):
    f.append(0)
for i in range(400,800):
    f.append(1)
for i in range(800,1200):
    f.append(2)
for i in range(1200,1600):
    f.append(3)
for i in range(1600,2000):
    f.append(4)
for i in range(2000,2400):
    f.append(5)
for i in range(2400,2800):
    f.append(6)
for i in range(2800,3200):
    f.append(7)
for i in range(3200,4801):
    f.append(-1)
n = I()
a = LI()
k = [1 for i in range(8)]
s = 0
t = 0
for i in a:
    if f[i] >= 0:
        if k[f[i]]:
            k[f[i]] = 0
            s += 1
    else:
        t += 1
print(max(s,1),min(s+t,n))
"""

#D
"""
n = I()
s = S()
ans = []
k = 0
for i in range(n):
    if s[i] == ")":
        k += 1
    else:
        if k > 0:
            ans += ["("]*k
            k = 0
        k -= 1
if k < 0:
    ans += [")"]*(-k)
else:
    ans = ["("]*k+ans
i = 0
if len(ans) == 0:
    for i in s:
        print(i,end = "")
else:
    while ans[i] == "(":
        i += 1
        if i == len(ans):break
    for j in range(n):
        ans.insert(i+j,s[j])
    for i in ans:
        print(i,end = "")
print()
"""
#E

#F

#G

#H

#I

#J

#K

#L

#M

#N

#O

#P

#Q

#R

#S

#T
