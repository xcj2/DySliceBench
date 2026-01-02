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

n=I()
m,a,r,c,h=0,0,0,0,0
for i in range(n):
    s=SI()
    if s[0]=="M":
        m+=1
    elif s[0]=="A":
        a+=1
    elif s[0]=="R":
        r+=1
    elif s[0]=="C":
        c+=1
    elif s[0]=="H":
        h+=1
lis=[]
lis.append(m)
lis.append(a)
lis.append(r)
lis.append(c)
lis.append(h)
u=[0,1,2,3,4]
ans=0
for i in combinations(u,3):
    pro=1
    for j in range(3):
        pro*=lis[i[j]]
    ans+=pro
print(ans)