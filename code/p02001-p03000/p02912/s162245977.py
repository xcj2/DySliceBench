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

n,m=MI()
As=LI()
for i in range(n):
    As[i]*=-1
    
#print(As)

heapify(As)
for i in range(m):
    mn=heappop(As)
    mn=(abs(mn)//2)*(-1)
    heappush(As,mn)

print(-sum(As))