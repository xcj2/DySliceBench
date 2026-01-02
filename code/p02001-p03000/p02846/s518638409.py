from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import time
import random
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def StoI():
    return [ord(i)-97 for i in input()]
def ItoS(nn):
    return chr(nn+97)
'''
def GI(V,E,DAG=False,index=0):
    g=[[] for i in range(n)]
    for i in range(E):
        inp=LI()
        if index==0:
            inp[0]-=1
            inp[1]-=1
        if len(inp)==2:
            a,b=inp
        elif len(inp)==3:
            a,b,c=inp
            aa=(inp[1:])
            bb=(inp[1:])
        g[a].append(b)
        if g[b].append(a)
        h.append(b)
'''

def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
u_alp=string.ascii_uppercase
ts=time.time()
sys.setrecursionlimit(10**5)
input=lambda: sys.stdin.readline().rstrip()
 
show_flg=False
show_flg=True

ans=0

s,t=LI()
a,c=LI()
b,d=LI()
if a*s+c*t<b*s+d*t:
    a,b,c,d=b,a,d,c
if a*s+c*t==b*s+d*t:
    print('infinity')
    exit()
p,q=(a-b)*s,(c-d)*t
if p>0 and p+q>0:
    print(0)
    exit()

#(p+q)*n+p<0
n=-p//(p+q)
ans=2*n+1
if -p%(p+q)==0:
    ans-=1

print(ans)