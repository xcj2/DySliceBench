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

def ceil(x,y):
    return -((-x)//y)
#print(ceil(5,2))
n,a,b=MI()
hp=[I() for i in range(n)]
x=0
y=10**9+1
while x+1<y:
    mid=(x+y)//2
    count=0
    for i in range(n):
        count+=max(0,ceil(hp[i]-b*mid,a-b))
    #print(mid,end=" ")
    #print(count<=mid)
    if count<=mid:
        y=mid
    else:
        x=mid
print(y)
    

    
            
        
        
    
    
    
    

    
    


    
    

        
        
    


    