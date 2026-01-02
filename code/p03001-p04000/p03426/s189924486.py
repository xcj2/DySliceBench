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

h,w,d=MI()
mp=[LI() for i in range(h)]
lis=[[0,0] for i in range(w*h)]
for i in range(h):
    for j in range(w):
        lis[mp[i][j]-1]=[i,j]
#print(lis)

costs=[0 for i in range(h*w+1)]
for i in range(1,d+1):
    for j in range(0,h*w):
        if i+d*(j+1)<h*w+1:
            costs[i+d*(j+1)]=costs[i+d*j]+abs(lis[i+d*(j+1)-1][1]-lis[i+d*j-1][1])+abs(lis[i+d*(j+1)-1][0]-lis[i+d*j-1][0])
        else:
            break
q=I()
for i in range(q):
    l,r=MI()
    u=l%d
    print(costs[r]-costs[l])

        


    
    


    

    
            
        
        
    
    
    
    

    
    


    
    

        
        
    


    