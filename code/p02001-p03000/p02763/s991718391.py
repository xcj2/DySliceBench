#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
n=int(input())
s=input()
q=int(input())

inf = set()
num_min =2**(n-1).bit_length()
dat=[inf]*(2*num_min-1)

#初期化
for i in range(n):
    dat[i+num_min-1]=set(s[i])
for i in range(num_min-2,-1,-1):
    dat[i]=dat[2*i+1].union(dat[2*i+2])

#親のノード(n-1)//2
#子のノード2n+1,2n+2

def segfunc(x,y):
    return x.union(y)

def update(i,x):
    i+=num_min-1
    dat[i]=x
    while i>0:
        i=(i-1)//2
        dat[i]=segfunc(dat[2*i+1],dat[2*i+2])
def query(a,b): #半開区間、[a,b)の最小値
    if b<=a:
        return inf
    res=inf
    a += num_min-1
    b += num_min-2
    while b-a>1:
        if a&1==0:
            res = segfunc(res,dat[a])
        if b&1==1:
            res = segfunc(res,dat[b])
            b-=1
        a=a//2
        b=(b-1)//2
    if a==b:
        res = segfunc(res,dat[a])
    else:
        res=segfunc(segfunc(res,dat[a]),dat[b])
    return res

for i in range(q):
  t,l,r=input().split()
  if t=="1":
    update(int(l)-1,set(r))
  else:
    ans=query(int(l)-1,int(r))
    print(len(ans))