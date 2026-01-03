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
s = S()
for i in range(len(s))[::-1]:
    if i%2 == 0:
        if s[:i//2] == s[i//2:i]:
            print(i)
            quit()
#C
"""
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
"""

#D
"""
n = I()
a = LI()
fact = [1 for i in range(n+2)]
for i in range(1,n+2):
    fact[i]*= fact[i-1]*i
    fact[i] %= mod
inv_fact = [1 for i in range(n+2)]
inv_fact[n+1] = pow(fact[n+1],mod-2,mod)
for i in range(1,n+1)[::-1]:
    inv_fact[i] = inv_fact[i+1]*(i+1)
    inv_fact[i] %= mod
count = [None for i in range(n+1)]
for i in range(n+1):
    if count[a[i]] != None:
        l = count[a[i]]
        r = n-i
        break
    count[a[i]] = i
for i in range(1,n+2):
    ans = fact[n+1]*inv_fact[i]*inv_fact[n+1-i]%mod
    if l+r >= i-1:
        ans -= fact[l+r]*inv_fact[i-1]*inv_fact[l+r-i+1]%mod
        ans %= mod
    print(ans)
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
