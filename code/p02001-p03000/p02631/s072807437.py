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
lis=LI()
ans=[[0]*35 for i in range(n)]

#print(ans)
#sys.exit()
for i in range(35):
    bits=[0 for j in range(n)]
    for k in range(n):
        bits[k]=(lis[k]>>i) %2
    #print(bits)
    ans[0][i]=sum(bits[1:])%2
    sm=sum(bits[1:])%2+bits[0]%2
    for k in range(1,n):
        ans[k][i]=(bits[k]-sm)%2
#print(ans)
answer=[0 for i in range(n)]
for i in range(n):
    for j in range(35):
        answer[i]+=ans[i][j]*(2**j)
print(*answer)
        
    
    
    
    
