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
n=I()
lis=list(SI())
orig=0
for i in range(n):
    if lis[i]=="0":
        lis[i]=0
    else:
        lis[i]=1
orcount=sum(lis)
m1=0
m3=0
if orcount==1:
    for i in range(n):
        if lis[i]==1:
            m3=(m3+pow(2,n-i-1,orcount+1))
elif orcount>1:
    for i in range(n):
        if lis[i]==1:
            m1=(m1+pow(2,n-i-1,orcount-1))
            m3=(m3+pow(2,n-i-1,orcount+1))
        
        
m1=m1
m3=m3
#print(m1)
#print(m3)
#print(orig)
dp=[0 for i in range(n+1)]
dp[1]=1
for i in range(1,n):
    #u=count1(i+1)
    count=0
    j=0
    while pow(2,j)<=i+1:
        if ((i+1)>>j) %2==1:
            count+=1
        j+=1
    z=1
    dp[i+1]=z+dp[(i+1)%count]
#print(dp)
for i in range(n):
    if lis[i]==0:
        #num=orig+pow(2,n-i-1)
        pr=orcount+1
        num=m3+pow(2,n-i-1,pr)
    else:
        #num=orig-pow(2,n-i-1)
        pr=orcount-1
        if pr!=0:
            num=m1-pow(2,n-i-1,pr)
    #print(num,pr)
    if pr==0:
        print(0)
    else:
        print(1+dp[num%pr])
