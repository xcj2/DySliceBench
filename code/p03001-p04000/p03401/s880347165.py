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
lis.insert(0,0)
lis.append(0)
ones=[]
twos=[]
for i in range(n+1):
    ones.append(abs(lis[i+1]-lis[i]))
    if i!=n:
        twos.append(abs(lis[i+2]-lis[i]))
#print(ones)
#print(twos)
u=sum(ones)
for i in range(n):
    ans=u-ones[i]-ones[i+1]+twos[i]
    print(ans)