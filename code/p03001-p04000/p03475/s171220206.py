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
lis=[LI() for i in range(n)]
for i in range(n-1):
    time=lis[i][1]+lis[i][0]
    pos=i+1
    #print(time,end=" ")
    #print(pos)
    while pos<n-1:
        if time<lis[pos][1]:
            time=lis[pos][1]
        if time%lis[pos][2]!=0:
            time+=(lis[pos][2]-time%lis[pos][2])
        time+=lis[pos][0]
        pos+=1
        #print(time,end=" ")
        #print(pos)
    print(time)
print(0)