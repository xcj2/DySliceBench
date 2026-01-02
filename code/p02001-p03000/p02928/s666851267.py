from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
from itertools import permutations,groupby
import sys
import bisect
import string
alp=string.ascii_lowercase
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
mo=10**9+7
#mo=998244353
#input=sys.stdin.readline

n,k=MI()
a=LI()
c=[0]*(2000+10)
t=[0]*(2000+10)
for i in range(n):
    c[a[i]]+=1
    tmp=0
    for j in range(i):
        tmp+=1 if a[j]>a[i] else 0
    t[i]=tmp

A=[0]
for i in c:
    A+=[i+A[-1]]
q=0
for i in range(n):
    q+=A[a[i]]
#q=sum(A[:-1])
q%=mo
q*=k*(k-1)//2
q%=mo

ans=k*sum(t)%mo
ans+=q
print(ans%mo)
#print(c,A,t,ans%mo)