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
s1=SI()
s2=SI()
i=0
vh=[]
while i<n:
    if s1[i]==s2[i]:
        vh.append(1)
        i+=1
    else:
        vh.append(0)
        i+=2
#print(vh)
if vh[0]==1:
    ans=3
else:
    ans=6
#print(ans)
for i in range(len(vh)-1):
    if vh[i]==1 and vh[i+1]==1:
        ans=ans*2%mod
    elif vh[i]==0 and vh[i+1]==1:
        ans=ans
    elif vh[i]==1 and vh[i+1]==0:
        ans=ans*2%mod
    else:
        ans=ans*3%mod
print(ans)