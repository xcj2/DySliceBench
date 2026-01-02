import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7
#s=input().rstrip()
n=I()
lis=[[]for i in range(n)]
for i in range(n):
    u=I()
    for j in range(u):
        a,b=MI()
        lis[i].append([a,b])
#print(lis)
z=[]
for x in range(2**n):
    u=[]
    for j in range(n):
        u.append(x%2)
        x=x>>1
    #print(u)
    count2=0
    for i in range(n):
        if u[i]==1:
            count=0
            for k in range(len(lis[i])):
                if lis[i][k][1]==u[lis[i][k][0]-1]:
                    count+=1
            if count==len(lis[i]):
                count2+=1
    if count2==sum(u):
        z.append(sum(u))
print(max(z))