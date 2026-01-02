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

n,a,b,c=MI()
mn=inf
lis=[I() for i in range(n)]
for i in list(product([0,1,2,3],repeat=n)):
    x=[]
    y=[]
    z=[]
    for j in range(n):
        if i[j]==0:
            x.append(lis[j])
        elif i[j]==1:
            y.append(lis[j])
        elif i[j]==2:
            z.append(lis[j])
    if len(x)==0 or len(y)==0 or len(z)==0:
        ans=inf
    else:
        ans=abs(sum(x)-a)+10*(len(x)-1)+abs(sum(y)-b)+10*(len(y)-1)+abs(sum(z)-c)+10*(len(z)-1)
    #print(ans)
    if ans<mn:
        mn=ans
        X=x
        Y=y
        Z=z
print(mn)
'''print(X)
print(Y)
print(Z)
'''