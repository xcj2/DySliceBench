import time
st_time=time.time()

from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import random
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
ts=time.time()
sys.setrecursionlimit(10**6)
#input=sys.stdin.readline
show_flg=False
#show_flg=True

di='URLD'
mp=dict(zip(list(di),range(4)))
rv=dict(zip(list(di),list(di[::-1])))

h,w,n=LI()
b=[h,w,w,h]
r,c=LI()
st=[h-r+1,c,w-c+1,r]
s=input()
t=[rv[i] for i in input()]
ans=True
for j,i in mp.items():
    c=st[i]
    for k in range(n):
        c+=1*(s[k]==j)
        if c>b[i]:
            ans=False
        if c>1:
            c-=1*(t[k]==j)
            
show(s)
show(t)
show(mp,rv,di)
if ans:
    print('YES')
else:
    print('NO')
