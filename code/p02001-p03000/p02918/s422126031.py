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

n,k=MI()
s=input()
#print(s)
ans=0
for i in range(n-1):
    u=s[i:i+1]
    v=s[i+1:i+2]
    if u==v:
        ans+=1
print(min(n-1,ans+2*k))