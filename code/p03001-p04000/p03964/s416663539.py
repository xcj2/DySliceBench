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
from math import floor, ceil,pi,factorial
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

n=I()
pairs=[LI() for i in range(n)]
def pair_revise(x,y,a,b):
    global p
    global q
    #print(x,y,a,b)
    for i in range(max(x//a,y//b),max(x//a,y//b)+2):
        p,q=a*i,b*i
        if p>=x and q>=y:
            break
    return [p,q]
    #return [x*max(ceil(x/a),ceil(y/b)),y*max(ceil(x/a),ceil(y/b))]
    #for i in range(max(ceil(x/a),ceil(y/b)),):
u,v=pairs[0]
for i in range(n-1):
    u,v=pair_revise(u,v,pairs[i+1][0],pairs[i+1][1])
print(u+v)
    
    
        









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

    
    
        



