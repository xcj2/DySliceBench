#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
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

a,x=MI()
size=[0 for i in range(a+1)]
size[0]=1
for i in range(a):
    size[i+1]=size[i]*2+3
#print(size)
#print(size[1])
patty=[0 for i in range(a+1)]
patty[0]=1
for i in range(a):
    patty[i+1]=2*patty[i]+1

def porb(k,n):
    if k==1 and n==0:
        return 1
    elif k==1:
        return 0
    elif k==size[n]:
        return patty[n]
    elif k>(size[n]+1)//2:
        return patty[n-1]+1+porb(k-(size[n]+1)//2,n-1)
    elif k==(size[n]+1)//2:
        return patty[n-1]+1
    else:
        return porb(k-1,n-1)

print(porb(x,a))