import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
#from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
#from math import floor, ceil
#from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
#inf = 10**17
#mod = 10**9 + 7
a,b,k=MI()
count=0
for i in range(1,101):
    l=100-i+1
    if a%l==0 and b%l==0:
        count+=1
        if count==k:
            print(l)