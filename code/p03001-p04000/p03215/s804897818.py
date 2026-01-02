from heapq import heappush, heappop
from collections import deque
import itertools
from itertools import permutations
import sys

import bisect
sys.setrecursionlimit(10**6)
def SI():
    return input().split()
def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
YN=['Yes','No']
YNeos='YNeos'
GYN=['Yes','trumpet']
mo=10**9+7
imp='IMPOSSIBLE'

n,k=MI()
a=LI()
A=[0]
for i in a:
    A+=[A[-1]+i]
b=[]
for i in range(n+1):
    for j in range(i+1,n+1):
        b+=[A[j]-A[i]]
        
c=sorted(b)#[-k:]
ans=0
i=0
i2=2**40
while i2>0:
#    print(i2,sum([(j&(ans+i2))==(ans+i2) for j in c]))
    ans+=i2 if sum([(j&(ans+i2))==(ans+i2) for j in c])>=k else 0
    i2//=2
    i+=1
    
print(ans)#,A,c)
#print()
