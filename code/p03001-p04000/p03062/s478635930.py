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
from copy import deepcopy
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
inf = 10**17
mod = 10**9 + 7

n=I()
A=LI()
count=0
for i in range(n):
    if A[i]<0:
        count+=1
B=sorted(list(map(abs,A)))
if count%2==1:
    ans=sum(B)-2*B[0]
else:
    ans=sum(B)
print(ans)