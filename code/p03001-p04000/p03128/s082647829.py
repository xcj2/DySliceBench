#!usr/bin/env python3
from collections import defaultdict
import math
import bisect
import random
def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return list(input())
def IIR(n): return [II() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
mod = 1000000007

#A
"""
a,b = LI()
if b % a == 0:
    print(a+b)
else:
    print(b-a)
"""

#B
"""
n,m = LI()
lis = [0 for i in range(m)]
for i in range(n):
    k = LI()
    for j in k[1:]:
        lis[j-1] += 1
ans = 0
for i in lis:
    if i == n:ans += 1
print(ans)
"""

#C
"""
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)
n = II()
a = LI()
ans = a[0]
for i in range(1,n):
    ans = gcd(ans,a[i])
print(ans)
"""

#D
n,m = LI()
a = LI()
f = [0,2,5,5,4,5,6,3,7,6]
for i in range(m):
    a[i] = [a[i],f[a[i]]]
a.sort(key = lambda x:x[1])
dp = [[] for i in range(n+10)]
for i in a:
    dp[i[1]] = [i[0]]
for i in range(n+1):
    for j in a:
        if i-j[1] >= 0 and len(dp[i-j[1]]) > 0:
            if len(dp[i]) < len(dp[i-j[1]])+1:
                dp[i] = dp[i-j[1]]+[j[0]]
                dp[i].sort()
                dp[i] = dp[i][::-1]
            else:
                if len(dp[i]) == len(dp[i-j[1]])+1:
                    d = sorted(dp[i-j[1]]+[j[0]])
                    d = d[::-1]
                    k = [dp[i],d]
                    k.sort()
                    if k[1] == d:
                        dp[i] = d
ans = 0
k = 1
l = len(dp[n])
for i in range(l):
    ans += k*dp[n][l-i-1]
    k *= 10
print(ans)

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
