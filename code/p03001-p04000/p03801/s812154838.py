from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations
import sys
import bisect
import string
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

n=I()
a=LI()

d={}
nd={}
for i,x in enumerate(a):
    if x in d:
        d[x]=min(i,d[x])
        nd[x]+=1
    else:
        d[x]=i
        nd[x]=1

A=[i for i in d.items()]
A=sorted(A,key=lambda x:x[0])
#[::-1]
ans=[0]*n
px,pm=A.pop()
nn=nd[px]
while A:
    x,m=A.pop()
    ans[pm]+=(px-x)*nn
    nn+=nd[x]
    px,pm=x,min(m,pm)
ans[0]+=sum(a)-sum(ans)
#print(n,sum(a),a)
#print(*ans)
for i in ans:print(i)
    