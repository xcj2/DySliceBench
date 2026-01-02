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
lis=[[0,0] for i in range(48)]
lis[0]=[0,1]
sup=1
low=0
for i in range(1,48):
    #print(low,sup)
    lis[i][0]=low+(-2)**i
    lis[i][1]=sup+(-2)**i
    if i%2==1:
        low+=(-2)**i
    else:
        sup+=(-2)**i
#print(lis)
x=47
table=[0 for i in range(48)]
while x>0:
    if lis[x][0]<=n<=lis[x][1]:
        table[x]=1
        n-=(-2)**x
    x-=1
if n==1:
    table[0]=1
#print(table)
u=sum(table)
if u==0:
    print(0)
    sys.exit()
goal=[]
y=0
sm=0
while sm<u:
    if table[y]==1:
        sm+=1
    goal.append(table[y])
    y+=1
#print(goal)
print(''.join(list(map(str,list(reversed(goal))))))