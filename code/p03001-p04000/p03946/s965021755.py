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
mx=[0 for i in range(n)]
mx[-1]=lis[-1]
for i in range(n-1):
    j=n-i-1
    mx[j-1]=max(mx[j],lis[j-1])
#print(mx)
difmx=0

for i in range(n):
    if mx[i]-lis[i]>difmx:
        difmx=mx[i]-lis[i]
#print(lis)
#print(difmx)
new_mx=[[0,0] for i in range(n)]
new_mx[-1]=[lis[-1],1]
count=0
for i in range(n-1):
    j=n-i-1
    #print(new_mx)
    #print(count)
    new_mx[j-1]=new_mx[j]
    if new_mx[j][0]-lis[j-1]==difmx:
        count+=new_mx[j][1]
    if new_mx[j][0]==lis[j-1]:
        new_mx[j][1]+=1
    if new_mx[j][0]<lis[j-1]:
        new_mx[j-1][0]=lis[j-1]
        new_mx[j-1][1]=1
print(count)
    
    
    


