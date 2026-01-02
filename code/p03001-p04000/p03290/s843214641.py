# coding: utf-8
# hello worldと表示する
import sys
import numpy
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

d,g=MI()
lis=[LI() for i in range(d)]
answers=[]
for i in product([0,1],repeat=d):
    new_lis=deepcopy(lis)
    point=0
    problems=0
    for j in range(d):
        if i[j]==1:
            point+=lis[j][1]+100*(j+1)*(lis[j][0])
            problems+=lis[j][0]
            new_lis[j][0]=0
        else:
            if new_lis[j][0]>0:
                new_lis[j][0]-=1
    #print(new_lis)
    flag=True
    for j in range(d):
        k=d-j-1
        if point>=g:
            answers.append(problems)
            flag=False
            break
        else:
            req=(g-point)//(100*(k+1))
            #print(req)
            if new_lis[k][0]>=req:
                problems+=req
                point+=req*100*(k+1)
            else:
                problems+=new_lis[k][0]
                point+=new_lis[k][0]*100*(k+1)
    if point>=g and flag==True:
        answers.append(problems)
#print(answers)
print(min(answers))            