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

#B

#C
"""
n,m = LI()
if m <= 2*n:print(m//2)
else:
    ans = n
    m -= 2*n
    ans += m//4
    print(ans)
"""

#D
def f(a,b,c):
    k = a^b
    if c == "x":
        k = 1-k
    return k
n = I()
s = S()
s.append(s[0])
na = ["S","W"]
pre = [0,0]
for i in range(1,n+1):
    pre.append(f(pre[-2],pre[-1],s[i]))
if pre[0] == pre[-2] and pre[1] == pre[-1]:
    for i in range(n-1):
        print(na[pre[i]],end = "")
    print(na[pre[n-1]])
    quit()
pre = [0,1]
for i in range(1,n+1):
    pre.append(f(pre[-2],pre[-1],s[i]))
if pre[0] == pre[-2] and pre[1] == pre[-1]:
    for i in range(n-1):
        print(na[pre[i]],end = "")
    print(na[pre[n-1]])
    quit()
pre = [1,0]
for i in range(1,n+1):
    pre.append(f(pre[-2],pre[-1],s[i]))
if pre[0] == pre[-2] and pre[1] == pre[-1]:
    for i in range(n-1):
        print(na[pre[i]],end = "")
    print(na[pre[n-1]])
    quit()
pre = [1,1]
for i in range(1,n+1):
    pre.append(f(pre[-2],pre[-1],s[i]))
if pre[0] == pre[-2] and pre[1] == pre[-1]:
    for i in range(n-1):
        print(na[pre[i]],end = "")
    print(na[pre[n-1]])
    quit()
print(-1)
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
