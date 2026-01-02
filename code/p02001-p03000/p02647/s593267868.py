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
import copy
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
n,k=MI()
lis=LI()
for i in range(min(k,100)):
    lis2=[0 for i in range(n)]
    for i in range(n):
        lis2[max(0,i-lis[i])]+=1
        if i+lis[i]+1<n:
            lis2[i+lis[i]+1]+=-1
    lis=list(accumulate(lis2))
    #print(lis)
print(*lis)
        
        
        
