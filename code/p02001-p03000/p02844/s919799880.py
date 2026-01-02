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
s=list(map(int,list(SI())))
pos=[[-1,-1] for i in range(10)]
for i in range(n):
    j=n-i-1
    if pos[s[i]][0]==-1:
        pos[s[i]][0]=i
    if pos[s[j]][1]==-1:
        pos[s[j]][1]=j
#print(pos)
count=0
for i in range(10):
    for j in range(10):
        lis=[0 for i in range(10)]
        if pos[i][0]<0 or pos[j][0]<0:
            continue
        for k in range(pos[i][0]+1,pos[j][1]):
            lis[s[k]]+=1
        for l in range(10):
            if lis[l]>0:
                count+=1
print(count)
            
        
        
            
    
            
            

    
    
            
            

