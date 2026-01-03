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

n=I()
u=[]
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        u.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            u.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        u.append(n)
    #return a
    return
for i in range(1,n+1):
    prime_factorize(i)
#print(u)
c=Counter(u)
ans=1
for j in c.keys():
    ans=ans*(c[j]+1)%mod
print(ans)