import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7
#s=input().rstrip()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n,x=MI()
lis=LI()
for i in range(n):
    lis[i]=abs(lis[i]-x)
if n==1:
    print(lis[0])
    sys.exit()
a=lis[0]
b=lis[1]
for i in range(2,n):
    a=gcd(a,b)
    b=lis[i]
print(gcd(a,b))