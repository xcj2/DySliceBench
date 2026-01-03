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
"""
a,b,h = IR(3)
print(((a+b)*h)//2)
"""
#B
s = SR(3)
i = 0
while 1:
    if len(s[i]) == 0:
        if i == 0:print("A")
        if i == 1:print("B")
        if i == 2:print("C")
        quit()
    x = s[i].pop(0)
    if x == "a":i = 0
    if x == "b":i = 1
    if x == "c":i = 2
#C

#D
"""
h,w,n = LI()
dp = [0 for i in range(10)]
dp[0] = (h-2)*(w-2)
q = defaultdict(int)
for i in range(n):
    a,b = LI()
    a -= 1
    b -= 1
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if 0 < a+i < h-1 and 0 < b+j < w-1:
                q[(a+i)*w+b+j] += 1
                dp[q[(a+i)*w+b+j]] += 1
                dp[q[(a+i)*w+b+j]-1] -= 1
for i in dp:
    print(i)
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
