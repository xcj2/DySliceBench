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
s=SI()
east=[]
west=[]
state=s[0]
count=1
if s[0]=="W":
    east.append(0)
for i in range(1,n):
    if s[i]==state:
        count+=1
    else:
        if state=="W":
            west.append(count)
            count=1
            state="E"
        else:
            east.append(count)
            count=1
            state="W"
if state=="W":
    west.append(count)
else:
    east.append(count)
if s[-1]=="E":
    west.append(0)
#print(east)
#print(west)
x=len(east)
E=sum(east)
W=sum(west)
anse=[]
answ=[]
vale=E-east[0]
for i in range(1,x):
    anse.append(vale)
    vale+=(west[i-1]-east[i])
anse.append(vale)
'''if east[0]==0:
    anse[0]=inf'''
print(min(anse))