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

n,k=MI()
lis=LI()
minus,plus=[],[]
for i in range(n):
    if lis[i]==0:
        k-=1
    elif lis[i]<0:
        minus.append(lis[i]*(-1))
    else:
        plus.append(lis[i])
minus=list(reversed(minus))
if k<=0:
    print(0)
    exit(0)
'''print(minus)
print(plus)'''
'''m=list(accumulate(minus))
p=list(accumulate(plus))'''
m=minus
p=plus
p=[0]+p
m=[0]+m
'''print(m)
print(p)'''
lens=[]

for i in range(k+1):
    im=i
    ip=k-i
    if im<len(m) and ip<len(p):
        dis=min(m[im],p[ip])*2+max(m[im],p[ip])
        lens.append(dis)
print(min(lens))