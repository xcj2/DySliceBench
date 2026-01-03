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

n,m=MI()
lis=[LI() for i in range(m)]
nums=[]
for i in range(m):
    if lis[i][0]==1:
        nums.append(lis[i][1])
    if lis[i][1]==n:
        nums.append(lis[i][0])
#print(nums)
if len(nums)>len(list(set(nums))):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")