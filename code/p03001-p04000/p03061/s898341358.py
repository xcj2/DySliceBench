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

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort(reverse=True)
    return divisors
#print(make_divisors(10))
n=I()
lis=sorted(LI())
u=make_divisors(lis[0])

for j in range(len(u)):
    br=u[j]
    count=0
    #print(br)
    for i in range(n):
        if lis[i]%br!=0:
            count+=1
    if count<=1:
        ans1=br
        break
#print(ans1)

v=make_divisors(lis[1])

for j in range(len(v)):
    bre=v[j]
    counti=0
    #print(bre)
    for i in range(n):
        if lis[i]%bre!=0:
            counti+=1
    if counti<=1:
        ans2=bre
        break
#print(ans2)
print(max(ans1,ans2))