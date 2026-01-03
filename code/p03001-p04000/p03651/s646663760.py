import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
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
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
lis.sort()
x=lis[0]
for i in range(n-1):
    x=gcd(x,lis[i+1])
if lis[-1]-k>=0 and (lis[-1]-k)%x==0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")

