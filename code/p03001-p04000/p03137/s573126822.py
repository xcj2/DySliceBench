#!usr/bin/env python3
from collections import defaultdict
import math
def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()
def IIR(n): return [II() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
mod = 1000000007

#A
"""
t,x = LI()
print(t/x)
"""

#B
"""
n= II()
a = LI()
m = max(a)
if m >= sum(a)-m:
    print("No")
else:
    print("Yes")
"""

#C
n,m = LI()
x = LI()
x.sort()
l = [x[i+1]-x[i] for i in range(m-1)]
l.sort()
l = l[::-1]
ans = sum(l[max(n-1,0):])
print(ans)
#D
"""
n,k = LI()
a = LI()
l = 0
b = [0 for i in range(n)]
for i in range(n):
    b[i] = list(bin(a[i]))[2:]
    l = max(l,len(b[i]))
s = [0 for i in range(l)]
for i in range(n):
    for j in range(l-len(b[i])):
        b[i].insert(0,"0")
for i in range(n):
    for j in range(l):
        s[j] += 1-int(b[i][j])
ke = 1
for i in range(l)[::-1]:
    if s[i] <= n//2:
        s[i] = [(n-s[i])*ke,0,float("inf")]
    else:
        s[i] = [(n-s[i])*ke,s[i]*ke,ke]
    ke *= 2
s.sort(key = lambda x:x[0])
d = 0
ans = 0
key = len(list(bin(k)))-2
key -= l
ke = 2**l
print(s)
for i in range(key):
    d += ke
    ans += n*ke
    ke *= 2
for i in range(l):
    r,q,p = s[i]
    if d+p <= k:
        d += p
        ans += q
    else:
        ans += r
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
