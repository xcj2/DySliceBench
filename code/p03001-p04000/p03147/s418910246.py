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
lis=LI()
count=0
while sum(lis)>0:
    i=0
    state=""
    while i<n:
        if lis[i]>0:
            lis[i]-=1
            state="water"
            #print(1)
        elif lis[i]==0 and state=="water":
            count+=1
            state=""
            #print(2)
        if i==n-1 and state=="water":
            count+=1
            state=""
            #print(3)
        i+=1
print(count)