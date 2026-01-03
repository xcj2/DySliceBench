# coding: utf-8
# hello worldと表示する
import sys
#import numpy
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor,pi,factorial
from operator import itemgetter
from copy import deepcopy
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

def ceil(x,y):
    return (-1)*((-x)//y)
    
n=I()
pairs=[LI() for i in range(n)]
x,y=1,1
for i in range(n):
    a=pairs[i][0]
    b=pairs[i][1]
    k=max(ceil(x,a),ceil(y,b))
    x,y=a*k,b*k
print(x+y)





'''def pair_revise(x,y,a,b):
    global p
    global q
    i=max(ceil(x/a),ceil(y/b))
    p,q=a*i,b*i
    return p,q
u,v=1,1
for i in range(n):
    u,v=pair_revise(u,v,pairs[i][0],pairs[i][1])
    print(u,v)
print(u+v)'''

    
    
        



