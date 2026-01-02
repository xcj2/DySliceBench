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
ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            pro=[0,0,0]
            pro[0]=lis[i]
            pro[1]=lis[j]
            pro[2]=lis[k]
            if pro[0]==pro[1] or pro[0]==pro[2] or pro[1]==pro[2]:
                continue
            pro.sort()
            if pro[0]+pro[1]>pro[2]:
                ans+=1
print(ans)
    
            
            