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
n,a,b = LI()
ans = [min(a,b),max(0,a+b-n)]
print(ans[0],ans[1])
"""

#B
"""
n = II()
a = S()
b = S()
c = S()
ans = 0
for i in range(n):
    if a[i] == b[i]:
        if b[i] == c[i]:
            continue
        else:
            ans += 1
    else:
        if b[i] == c[i] or c[i] == a[i]:
            ans += 1
        else:
            ans += 2
print(ans)
"""

#C
"""
n = II()
c = LIR(n)
c.sort(key = lambda x:-x[0]-x[1])
ans = 0
i = 0
for i in range(n):
    x,y = c.pop(0)
    if i%2 == 0:
        ans += x
    else:
        ans -= y
print(ans)
"""

#D
import queue
n,m = LI()
c = LIR(n-1+m)
for i in range(n-1+m):
    c[i][0] -= 1
    c[i][1] -= 1
v = [[] for i in range(n)]
ins = [0 for i in range(n)]
for a,b in c:
    v[a].append(b)
    ins[b] += 1
ans = [-1 for i in range(n)]
q = queue.Queue()
for i in range(n):
    if ins[i] == 0:
        q.put(i)
while not q.empty():
    i = q.get()
    for j in v[i]:
        ans[j] = i
        ins[j] -= 1
        if ins[j] == 0:
            q.put(j)
for i in ans:
    print(i+1)
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
