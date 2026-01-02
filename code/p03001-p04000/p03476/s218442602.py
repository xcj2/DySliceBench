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

from math import sqrt
def prime(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            return False
    return True
n=10*5-1
dp=[0 for i in range(10**5//2)]
dp[0]=0
for i in range(1,10**5//2):
    odd=2*i+1
    if prime(i+1) and prime(odd):
        dp[i]=dp[i-1]+1
    else:
        dp[i]=dp[i-1]
q=I()
for i in range(q):
    a,b=MI()
    if a==1:
        print(dp[(b+1)//2-1])
    else:
        print(dp[(b+1)//2-1]-dp[(a+1)//2-2])
        