
def s0():return input()
def s1():return input().split()
def s2(n):return [input() for x in range(n)]
def s3(n):return [[input().split()] for _ in range(n)]
def n0():return int(input())
def n1():return [int(x) for x in input().split()]
def n2(n):return [int(input()) for _ in range(n)]
def n3(n):return [[int(x) for x in input().split()] for _ in range(n)]

n=n0()
a=n1()
b=n1()
c=n1()

a.sort()
b.sort()
c.sort()

from bisect import bisect_left,bisect_right
b2=[]
for i in b:
    b2.append(bisect_left(a,i))

import itertools
b3=list(itertools.accumulate(b2))
    
ans=0
for i in c:
    t=bisect_left(b,i)
    if t>0:
        ans+=b3[t-1]
    
print(ans)