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

n,m,k=MI()
lisa=LI()
lisb=LI()
u=list(accumulate(lisa))
v=list(accumulate(lisb))
u=[0]+u
v=[0]+v
for i in range(n+1):
    if u[i]>k:
        i-=1
        break
'''print(i)
print(u)
print(v)'''
j=0
count=[]
while True:
    if i<0:
        i+=1
        count.append(i+j)
        break
    while True:
        #print(i,j)
        if j>=m+1:
            j-=1
            count.append(i+j)
            break
        if u[i]+v[j]<=k:
            j+=1
        else:
            j-=1
            count.append(i+j)
            break
    i-=1
print(max(count))
    
            
        
        
    
    
    
    

    
    


    
    

        
        
    


    