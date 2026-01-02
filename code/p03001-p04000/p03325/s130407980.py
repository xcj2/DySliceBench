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
mod=10**9+7

def coutwo(n):
    count=0
    flag=True
    while flag==True:
        if n%2==0:
            count+=1
            n=n//2
        else:
            flag=False
    return count
#print(coutwo(4))
n=I()
lis=LI()
ans=0
for i in range(n):
    ans+=coutwo(lis[i])
print(ans)