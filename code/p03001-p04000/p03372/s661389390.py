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

n,c=MI()
cal1=[]
dis1=[]
for i in range(n):
    a,b=MI()
    cal1.append(b)
    dis1.append(a)
cal2=list(reversed(cal1))
dis2=[0 for i in range(n)]
for i in range(n):
    dis2[i]=c-dis1[i]
dis2=list(reversed(dis2))
#print(cal1)
#print(dis1)
#print(cal2)
#print(dis2)
u1=list(accumulate(cal1))
v1=list(accumulate(cal1))
u2=list(accumulate(cal2))
v2=list(accumulate(cal2))
for i in range(n):
    u1[i]-=dis1[i]
    v1[i]-=2*dis1[i]
    u2[i]-=dis2[i]
    v2[i]-=2*dis2[i]
'''print("u1")
print(u1)
print("u2")
print(u2)
print("v1")
print(v1)
print("v2")
print(v2)'''
ans=[]
ans.append(max(u1))
ans.append(max(u2))
#print(ans)
mxv1=[0 for i in range(n)]
mxv2=[0 for i in range(n)]
mxv1[0]=max(0,v1[0])
mxv2[0]=max(0,v2[0])
for i in range(n-1):
    mxv1[i+1]=max(v1[i+1],mxv1[i])
    mxv2[i+1]=max(v2[i+1],mxv2[i])
'''print("mxv1")
print(mxv1)
print("mxv2")
print(mxv2)'''
mxa=0
for i in range(n-1):
    sm=u1[i]+mxv2[n-i-2]
    #print(sm)
    if sm>mxa:
        mxa=sm
ans.append(mxa)
mxb=0
for i in range(n-1):
    sm=u2[i]+mxv1[n-i-2]
    #print(sm)
    if sm>mxb:
        mxb=sm
ans.append(mxb)
#print(ans)
print(max(ans))

    
    


    
    

        
        
    

