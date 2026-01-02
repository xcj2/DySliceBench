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
lis=[LI() for i in range(n)]
lis.sort()
sq=[]
for i in range(n):
    for j in range(i+1,n+1):
        new_lis=lis[i:j]
        hor=new_lis[-1][0]-new_lis[0][0]
        #print(new_lis)
        if len(new_lis)<k:
            continue
        new_lis.sort(key=lambda x:x[1])
        #print(new_lis)
        u=len(new_lis)
        for i in range(u-k+1):
            sq.append(hor*(new_lis[i+k-1][1]-new_lis[i][1]))
#print(sq)
print(min(sq))
    
            
        
        
    

    
        
    
    
    