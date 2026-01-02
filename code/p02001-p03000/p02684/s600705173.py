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

n,k=MI()
lis=LI()
i=0
x=0
plot=[0]
while i<n:
    x=lis[x]-1
    i+=1
    plot.append(x)
#print(plot)
y=plot[-1]
for i in range(n):
    j=n-i-1
    if y==plot[j]:
        t=i+1
        break
#print(t)
for i in range(n):
    if plot[i]==plot[i+t]:
        am=i
        break
#print(am)
if k<=am:
    print(plot[k]+1)
else:
    print(plot[am+(k-am)%t]+1)