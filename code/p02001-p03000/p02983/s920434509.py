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
#mod = 10**9 + 7

mod=2019
l,r=MI()
mn=inf
mods=[]
#print(l,r)

#print(mods)
if (r-l)>=2018:
    ans=0
    #print(1)
else:
    for i in range(l,r+1):
        mods.append(i%mod)
    for i in range(r-l+1):
        for j in range(i+1,r-l+1):
            u=(mods[i])*(mods[j])%mod
            if u<mn:
                mn=u
    ans=mn
print(ans)

