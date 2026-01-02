# coding: utf-8
# hello worldと表示する
#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

n,k=MI()
lis=LI()
minus=[]
plus=[]
zero=0
for i in range(n):
    if lis[i]<0:
        minus.append(lis[i])
    elif lis[i]>0:
        plus.append(lis[i])
    else:
        zero+=1
#print(plus)
#print(minus)
#print(zero)
p=len(plus)
m=len(minus)

if n-zero<k:
    ans=0
    print(ans%mod)
    sys.exit()
if p>=k:
    state="plus"
elif (k-p)%2==0:
    state="plus"
elif m>=k-p+1:
    if k%2==1:
        if p>0:
            state="plus"
        else:
            if zero>0:
                ans=0
                print(ans%mod)
                sys.exit()
            else:
                state="minus"
    else:    
        state="plus"
else:
    if zero>0:
        ans=0
        print(ans%mod)
        sys.exit()
    else:
        state="minus"
#print(state)
if state=="plus":
    ans=1
    plus.sort(reverse=True)
    minus.sort()
    pros=[]
    if k%2==1:
        ans*=plus[0]
        k-=1
        for i in range((p-1)//2):
            pros.append(plus[2*i+1]*plus[2*i+2])
    else:
        ans*=1
        for i in range(p//2):
            pros.append(plus[2*i]*plus[2*i+1])
    for i in range(m//2):
        pros.append(minus[2*i]*minus[2*i+1])
    pros.sort(reverse=True)
    for i in range(k//2):
        ans=(ans*pros[i])%mod
    print(ans%mod)
    sys.exit()
elif state=="minus":
    ans=1
    plus.sort()
    minus.sort(reverse=True)
    pros=[]
    ans*=minus[0]
    k-=1
    if k%2==1:
        ans*=plus[0]
        k-=1
        for i in range((p-1)//2):
            pros.append(plus[2*i+1]*plus[2*i+2])
    else:
        for i in range(p//2):
            pros.append(plus[2*i]*plus[2*i+1])
    for i in range((m-1)//2):
        pros.append(minus[2*i+1]*minus[2*i+2])
    pros.sort()
    for i in range(k//2):
        ans=(ans*pros[i])%mod
    print(ans%mod)
    sys.exit()
    
    
        
        
            
    
    
        
        

    