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
n = I()
a = LI()
b = [None for i in range(n)]
k = n//2
if n%2:
    for i in range(n):
        if i%2:
            b[k+(i+1)//2] = a[i]
        else:
            b[k-i//2] = a[i]
else:
    for i in range(n):
        if i%2:
            b[k-(i+1)//2] = a[i]
        else:
            b[k+i//2] = a[i]
print(*b)
#D

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
