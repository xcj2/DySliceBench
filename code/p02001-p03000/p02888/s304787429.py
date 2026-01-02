from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
import random  # randome is not available at Codeforces
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
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
#eps=10**(-10)
#ts=time.time()
#sys.setrecursionlimit(10**6)
input=lambda: sys.stdin.readline().rstrip()

show_flg=False
show_flg=True

n=I()
a=sorted(LI())[::-1]

def solve(a):
    s=set()
    for i in a:
        s.add(i)
    s=sorted(list(s))[::-1]
    L=1010
    k=[0]*(L)
    ak=[0]
    for i in a:
        k[i]+=1
    for i in range(L):
        ak.append(ak[-1]+k[i])
    ans,a1,a2,a3,a4=0,0,0,0,0
    un=len(s)
    for i in range(un):
        c=s[i]
        if k[c]>=3:
            a1+=k[c]*(k[c]-1)*(k[c]-2)//6
        if k[c]>=2:
            a2+=ak[c]*k[c]*(k[c]-1)//2
        for j in range(i+1,un):
            sc=s[j]
            a3+=(1 if 2*sc>c else 0)*k[c]*k[sc]*(k[sc]-1)//2
            mm=c-sc+1
            if mm<0:
                continue
            elif mm>sc:
                break
            else:
                a4+=k[c]*k[sc]*(ak[sc]-ak[mm])
            
    ans=a1+a2+a3+a4
    return ans,a1,a2,a3,a4

def naive(a):
    b=sorted(a)[::-1]
    n=len(b)
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if b[j]+b[k]>b[i]:
                    ans+=1
    return ans

print(solve(a)[0])
