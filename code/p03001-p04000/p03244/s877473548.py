# coding: utf-8
# hello worldと表示する
#float型を許すな
#numpyはpythonで
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

n=I()//2
lis=LI()
lis1=[]
lis2=[]
for i in range(n):
    lis1.append(lis[2*i])
    lis2.append(lis[2*i+1])
x=Counter(lis1).most_common(2)
y=Counter(lis2).most_common(2)
#print(x)
#print(y)
if len(x)==1:
    x.append((0,0))
if len(y)==1:
    y.append((-1,0))
#print(x)
#print(y)
if x[0][0]!=y[0][0]:
    print(2*n-x[0][1]-y[0][1])
else:
    cands=[]
    #print(2*n-x[0][1]-y[1][]))
    if x[1][0]!=y[0][0]:
        cands.append(2*n-x[1][1]-y[0][1])
    if x[0][0]!=y[1][0]:
        cands.append(2*n-x[0][1]-y[1][1])
    if x[1][0]!=y[1][0]:
        cands.append(2*n-x[1][1]-y[1][1])
    print(min(cands))
    
            
    
    