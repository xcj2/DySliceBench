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
c=Counter(lis)
nums=[]
for i in c.keys():
    if c[i]>=2:
        nums.append(i)
nums.sort(reverse=True)
#print(nums)
if len(nums)==0:
    print(0)
elif len(nums)==1:
    if c[nums[0]]>=4:
        print(nums[0]**2)
    else:
        print(0)
else:
    if c[nums[0]]>=4:
        print(nums[0]**2)
    else:
        print(nums[0]*nums[1])
