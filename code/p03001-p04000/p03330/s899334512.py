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
colors=[LI() for i in range(c)]
grid=[LI() for i in range(n)]
lis0=[]
lis1=[]
lis2=[]
for i in range(n):
    for j in range(n):
        if (i+j)%3==0:
            lis0.append(grid[i][j]-1)
        elif (i+j)%3==1:
            lis1.append(grid[i][j]-1)
        else:
            lis2.append(grid[i][j]-1)
#print(grid)
c0=Counter(lis0)
c1=Counter(lis1)
c2=Counter(lis2)
ind=[i for i in range(c)]
mn=inf
for i in product(ind,repeat=3):
    ans=0
    if i[0]==i[1] or i[1]==i[2] or i[2]==i[0]:
        continue
    #print(i[0],i[1],i[2])
    for x in c0.keys():
        #print(x,i[0])
        ans+=c0[x]*colors[x][i[0]]
    for y in c1.keys():
        #print(y,i[1])
        ans+=c1[y]*colors[y][i[1]]
    for z in c2.keys():
        #print(z,i[2])
        ans+=c2[z]*colors[z][i[2]]
    if ans<mn:
        mn=ans
print(mn)

        
    


    