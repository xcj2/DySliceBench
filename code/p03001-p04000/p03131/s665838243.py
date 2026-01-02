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
n,k = LI()
if 2*(k-1) < n:
    print("YES")
else:
    print("NO")
"""

#B
"""
c = LIR(3)
v = [[] for i in range(4)]
for i in range(3):
    c[i][0] -= 1
    c[i][1] -= 1
    v[c[i][0]].append(c[i][1])
    v[c[i][1]].append(c[i][0])

for i in range(4):
    li = [True for i in range(4)]
    li[i] = False
    q = [i]
    c = 0
    while q:
        x = q.pop(-1)
        k = 0
        for j in v[x]:
            if li[j]:
                li[j] = False
                q.append(j)
                if k == 0:
                    c += 1
                    k += 1
    if c == 3:
        print("YES")
        quit()
print("NO")
"""

#C
k,a,b = LI()
if k <= a:
    print(k+1)
else:
    if b-a < 3:
        print(k+1)
    else:
        ans = a+((k-a+1)//2)*(b-a)+(k-a+1)%2
        print(ans)
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
