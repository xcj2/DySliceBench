# coding: utf-8
# hello worldと表示する
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

n=I()
lis=LI()
dic=[0 for i in range(9)]
for i in range(n):
    if lis[i]//400>=8:
        dic[8]+=1
    else:
        if dic[lis[i]//400]==0:
            dic[lis[i]//400]=1
        
#print(dic)
#print(sum(dic[0:8]))
if sum(dic[0:8])==0:
    mn=1
    mx=dic[-1]
else:
    mn=sum(dic[0:8])
    mx=sum(dic[0:8])+dic[-1]
print(mn,mx)